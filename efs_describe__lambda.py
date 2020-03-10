import boto3

def lambda_handler(event, context):
   resource = boto3.client('efs')
   print(resource.describe_file_systems())
