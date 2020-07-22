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

def listtasks(env: str, status: str, bnw_name: str):
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
            overrides=task['overrides']['containerOverrides'][0]
            print("\n" + str(idx) + ") Task " + status + ":")
            print(task["taskArn"])
            # print("=========")
            # pprint(containers[0])

            if 'startedAt' in task:
                print("started at:")
                print(task["startedAt"])

            if 'command' in overrides:
                print("Command:")
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
    # example sb-airflow-worker-master-285e152-a-dev-production-eu-west-1-app-container
    bnwname=sys.argv[1]    
    
    for status in ["RUNNING", 'PENDING']:
        listtasks("dev", status, bnwname)
