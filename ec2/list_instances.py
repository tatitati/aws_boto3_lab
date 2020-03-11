import boto3

aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con=aws_mag_con.resource('ec2')

for each_ec2 in ec2_con.instances.all():
	print(each_ec2.id)
