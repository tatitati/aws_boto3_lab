import os
import time
import json
import boto3
from pprint import pprint
from datetime import datetime, timedelta

sess = boto3.session.Session(profile_name='default')
client = sess.client('ecs')

response = client.list_container_instances(
    cluster='mycluster'
)

pprint(response)
