import boto3
import json

# for launching new instances see: http://boto3.readthedocs.io/en/latest/guide/migrationec2.html#launching-new-instances
# ec2 managment
ec2 = boto3.resource('ec2')
sqs = boto3.client('sqs')

def list_running():
   instances = ec2.instances.filter(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
   for instance in instances:
       print(instance.id, instance.instance_type)

def list_ips():
   instances = ec2.instances.filter(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
   for instance in instances:
       print(instance.id, instance.public_ip_address)

def list_health():
    for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
       print(status)

def list_by_label():
    instances = ec2.instances.filter(
       Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
       print(instance.id, instance.public_ip_address, instance.tags)
