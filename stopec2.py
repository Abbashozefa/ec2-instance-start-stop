import boto3
region='us-east-1'
instances=['i-093707358e6bd9261']
ec2=boto3.client('ec2',region_name=region)
def lambda_handler(event, context):
    # TODO implement
    ec2.stop_instances(InstanceIds=instances)
    print("stopped your instances"+str(instances))