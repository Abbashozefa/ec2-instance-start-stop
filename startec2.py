import boto3
region='us-east-1'
instances=['']
ec2=boto3.client('ec2',region_name=region)
# TODO implement
ec2.start_instances(InstanceIds=instances)
print("started your instances"+str(instances))