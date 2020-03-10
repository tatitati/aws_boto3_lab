
# How can I run these scripts?

These scripts use your configured credentials under ~/.aws, so you don't need to ssh at all into an EC2 to run them
You will need only to install boto3 into your laptop

For example: 
```
$ python ec2_list__script.py
i-0cc0c62f210aa08ca
i-03c8dc3da12945031
i-0770d584ca891fb8f
```
You can also create a lambda and paste the content of (for instance) ec2_list__lambda.py, and then run the lambda

