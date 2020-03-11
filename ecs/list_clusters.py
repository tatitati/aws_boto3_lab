import os
import time
import json
import boto3
from pprint import pprint
from datetime import datetime, timedelta

sess = boto3.session.Session(profile_name='default')
ecs = sess.client('ecs')

clusters = ecs.list_clusters()

pprint(clusters)
