Setup:
Place this file in a folder and do `chmod +x <file.py>`. Then add this folder to the PATH


Example use:

```
bnw_login --team dna-devs --environment dev
cd /projects/dockerized_project
<file.py>
```

Output show you that we have 2 containers running of this project (/projects/dockerized_project) in dev:
```
Container
=========
{'containerArn': 'arn:aws:ecs:eu-west-1:089169401626:container/c1db7ad2-e21a-4c60-a87c-3f36cf83980b',
 'cpu': '2',
 'healthStatus': 'UNKNOWN',
 'image': '......dkr.ecr.eu-west-1.amazonaws.com/snowflake-merge......',
 'lastStatus': 'PENDING',
 'memory': '300',
 'name': 'snowflake-merge-master-5b5ee79-0-dev-production-eu-west-1',
 'networkInterfaces': [],
 'taskArn': 'arn:aws:ecs:eu-west-1:.....:task/ecs-cluster-master-a90a1f4-0-dev-production-eu........'}


    Command
    =======
    ['/bin/bash', '-c', 'cd /opt/project/snowflake && python3 merge.py']

===========================================

Container
=========
{'containerArn': 'arn:aws:ecs:eu-west-1:.......:container/75446e63.......',
 'cpu': '2',
 'healthStatus': 'UNKNOWN',
 'image': '........dkr.ecr.eu-west-1.amazonaws.com/snowflake-merge.....',
 'lastStatus': 'PENDING',
 'memory': '300',
 'name': 'snowflake-merge-master-5b5ee79-0-dev-production-eu-west-1',
 'networkInterfaces': [],
 'taskArn': 'arn:aws:ecs:eu-west-1:............/ecs-cluster-master-a90a1f4-0-dev-production-eu-west-1-...../......'}


    Command
    =======
    ['/bin/bash', '-c', 'cd /opt/.......']


===========================================

* No tasks PENDING
```