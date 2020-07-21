#!/usr/local/bin/python3

import os
import sys
import time
import json
import re
import boto3
from pprint import pprint
import subprocess
from datetime import datetime, timedelta

def getbnwname(env: str="dev"):
    try:
        f = open("_pipeline/config.sh")
        text=f.read()
        f.close()

        matches = re.findall(r"export APP_NAME='(.*)'",text)
        appname = matches[0]
        res = subprocess.check_output("bnw_name " + appname + " master " + env + " production eu-west-1", shell=True)
        return res.decode('UTF-8')
    except IOError:
        sys.exit(0)


def runtask(taskdefinition: str):
    sess = boto3.session.Session(region_name="eu-west-1", profile_name='dev-production')
    client = sess.client('ecs')
    cluster=client.list_clusters()['clusterArns'][0]
    

    response = client.run_task(
        cluster=cluster,
        taskDefinition=taskdefinition,
        overrides={
            'containerOverrides': [
                {
                    'name': taskdefinition,
                    'command': ['date']
                }
            ]
        }
        )

    pprint(response)
    arn = response["tasks"][0]['taskArn']
    waiter = client.get_waiter('tasks_stopped')
    waiter.wait(cluster='mycluster', tasks=[arn])


if __name__ == "__main__":    
        command = sys.argv[1:]   
        print(command)     
        taskdefinition = getbnwname("dev")
        runtask(taskdefinition)
