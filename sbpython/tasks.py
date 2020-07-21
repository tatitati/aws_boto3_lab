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

def getbnwname(env: str="dev", forApp: str = None):
    try:
        res = ""
        if forApp == None:
            f = open("_pipeline/config.sh")
            text=f.read()
            f.close()

            matches = re.findall(r"export APP_NAME='(.*)'",text)
            appname = matches[0]
            res = subprocess.check_output("bnw_name " + appname + " master " + env + " production eu-west-1", shell=True)
        else:
            res = subprocess.check_output("bnw_name " + forApp + " master " + env + " production eu-west-1", shell=True)

        print(res.decode('UTF-8'))
        return res.decode('UTF-8')

    except IOError:
        sys.exit(0)



def listtasks(env: str, status: str, forApp: str = None):
    bnwname = getbnwname(env, forApp)
    sess = boto3.session.Session(region_name='eu-west-1', profile_name='dev-production')
    client = sess.client('ecs')
    runOnCluster=client.list_clusters()['clusterArns'][0]

    response = client.list_tasks(
        cluster=runOnCluster,
        family=bnwname,
        desiredStatus=status
    )    

    if len(response['taskArns']) > 0:
        response = client.describe_tasks(
            cluster=runOnCluster,
            tasks=response['taskArns']
        )



        for idx, task in enumerate(response['tasks']):
            containers=task['containers']
            overrides=task['overrides']['containerOverrides'][0]
            print("\n" + str(idx) + ") Task " + status + ":")
            print(task["taskArn"])
            # print("=========")
            # pprint(containers[0])
            # print("Command:")
            if 'startedAt' in task:
                print("started at:")
                print(task["startedAt"])

            if 'command' in task:
                print(overrides['command'])

            # this code might be useful to have more useful information
            # containerInstance = task["containerInstanceArn"]
            # response = client.describe_container_instances(
            #     cluster=runOnCluster,
            #     containerInstances=[
            #         containerInstance
            #     ]
            # )
            # instance = response["containerInstances"]

            # print("\nResources")
            # print("=============")
            # print("\nRegistered resources")
            # print(instance[0]["registeredResources"])
            # print("\nRemaining resources")
            # print(instance[0]["remainingResources"])

    else:
        print("\n\n* No tasks " + status)




if __name__ == "__main__":
    env = "dev"
    if len(sys.argv) > 1:
        env = sys.argv[1]

    forApp = None
    if len(sys.argv) > 2:
        forApp = sys.argv[2]

    for status in ["RUNNING", 'PENDING']:
        listtasks(env, status, forApp)
