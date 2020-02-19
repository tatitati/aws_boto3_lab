import boto3

def lambda_handler(event, context):
   ec2_con = boto3.resource("ec2", "eu-central-1")
   for ec2 in ec2_con.instances.all():
       print ec2.id