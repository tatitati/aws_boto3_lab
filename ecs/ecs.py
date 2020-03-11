import os
import time
import json
import boto3
from datetime import datetime, timedelta

sess = boto3.session.Session(region_name='eu-west-1', profile_name='dev-production')
ecs = sess.client('ecs')
cluster = ecs.list_clusters()['clusterArns'][0]
print(cluster)
