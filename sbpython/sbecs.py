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
        return res
    except IOError:
        print("File not accessible")



def listtasks(env: str="dev"):
    bnwname = getbnwname(env).decode('UTF-8')
    region = 'eu-west-1'
    sess = boto3.session.Session(region_name=region, profile_name='dev-production')
    client = sess.client('ecs')
    runOnCluster=client.list_clusters()['clusterArns'][0]

    response = client.list_tasks(
        cluster=runOnCluster,
        family=bnwname,
        desiredStatus='RUNNING'
    )

    if len(response['taskArns']) > 0:
        tasks = response['taskArns']

        response = client.describe_tasks(
            cluster=runOnCluster,
            tasks=tasks
        )

        for task in response['tasks']:
            containers=task['containers']
            overrides=task['overrides']['containerOverrides'][0]
            print("Container")
            print("=========")
            pprint(containers[0])
            print("\n")
            print("Command")
            print("=======")
            print(overrides['command'])
            print("\n\n===========================================\n\n")
    else:
        print("No tasks")

if __name__ == "__main__":
    listtasks()
