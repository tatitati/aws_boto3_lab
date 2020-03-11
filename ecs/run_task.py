import os
import time
import json
import boto3
from pprint import pprint
from datetime import datetime, timedelta

sess = boto3.session.Session(profile_name='default')
client = sess.client('ecs')
response = client.run_task(
    cluster='mycluster',
    taskDefinition='my-httpd',
    overrides={
         'containerOverrides': [
             {
                 'name': 'httpd',  # name of an existing container already defined inside of the task definition
                 'command': [
                     'whoami'
                 ]
             }
         ]
     }
    )

pprint(response)
# arn = response["tasks"][0]['taskArn']
# waiter = client.get_waiter('tasks_stopped')
# waiter.wait(cluster='default', tasks=[arn])
