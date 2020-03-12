import os
import time
import json
import boto3
from pprint import pprint
from datetime import datetime, timedelta

sess = boto3.session.Session(profile_name='default', region_name='eu-central-1')
client = sess.client('ecs')
response = client.run_task(
    cluster='mycluster',  # my already existing cluster
    taskDefinition='tdcentos', # my already existing task definition
    overrides={
         'containerOverrides': [
             {
                 'name': 'ccentos',  # name of an existing container already defined inside of my existing task definition
                 # Until now I specified cluster->task_definition->container. Now
                 # I can speicify what I want to override from this container (I cannot everything)
                 # for the new container that I'm going to spin up
                 'environment': [{
                    'name': 'MYCUSTOMVARIABLE',
                    'value': 'TUMADREEEEEEE'
                 }],
                 'command': ['date'] # like when we do: docker run -it centos:latest date
             }
         ]
     }
    )

pprint(response)
arn = response["tasks"][0]['taskArn']
waiter = client.get_waiter('tasks_stopped')
waiter.wait(cluster='mycluster', tasks=[arn])
