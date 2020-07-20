#!/usr/local/bin/python3

import os
import sys
import time
import json
import boto3
from pprint import pprint
from datetime import datetime, timedelta


region = 'eu-west-1'
sess = boto3.session.Session(region_name=region, profile_name='dev-production')
client = sess.client('ecs')
runOnCluster=client.list_clusters()['clusterArns'][0]
family=sys.argv[1]

response = client.list_tasks(
    cluster=runOnCluster,
    family=family,
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
        overrides=task['overrides']
        pprint(containers[0]['containerArn'])
        pprint(overrides)
        print("\n\n===========================================\n\n")
else:
    print("No tasks")
