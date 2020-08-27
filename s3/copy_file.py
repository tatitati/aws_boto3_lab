#!/usr/bin/env python3
import boto3
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
prefix="myfolder/copy/com_simplybusiness_rfq_created_2"
file_to_reingest = "mycsv_pipe"
extension=".csv"

session=boto3.session.Session(profile_name="default")
s3=session.resource('s3')

bucket_name='tatitatibucket'
# source = {'Bucket': bucket_name, 'Key': f"snowpipe/copy/com_simplybusiness_rfq_created_2/smyfolder/{file}"}
source = {'Bucket': bucket_name, 'Key': f"{prefix}/{file_to_reingest}{extension}"}
dest = s3.Bucket(bucket_name)
dest.copy(source, f"{prefix}/reingested/{file_to_reingest}--reingested--{now}{extension}" )


# List reingested folder
for object in dest.objects.filter(Prefix=f"{prefix}/reingested/"):
    print(object.key)
