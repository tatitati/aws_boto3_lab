#!/usr/bin/env python3
import boto3

session=boto3.session.Session(profile_name="dev-production")
s3=session.resource('s3')

bucket_name='snowflake-master-98773dd-0-dev-production-eu-west-1'
prefix = 'snowpipe/copy/com_simplybusiness_rfq_created_2/2020-07-28'

my_bucket = s3.Bucket(bucket_name)


copy_from = {
      'Bucket': bucket,
      'Key': prefix
}

bucket = s3.Bucket(bucket_name)
bucket.copy(copy_from, bucket_name, f"{prefix}/reingested" )

for file in my_bucket.objects.filter(Prefix=prefix):
    print(file.key)


# aws s3 cp s3://mybucket/test.txt s3://mybucket/test2.txt
