import boto3

def lambda_handler(event, context):
   ec2_con = boto3.resource("s3", "eu-central-1")
   for ec2 in ec2_con.buckets.all():
       print ec2.name