import boto3
from assertpy import assert_that
from behave import *

running_instances_filter = [
  {
    'Name': 'instance-state-name',
    'Values': ['running']
  }
]

@given('the region "{region}"')
def step_impl(context, region):
  # terraform.init()
  context.region = region
  context.ec2_client = boto3.client('ec2', region_name=region)
  pass


@given('an account with only the default VPC')
def step_impl(context):
  vpcs = context.ec2_client.describe_vpcs()
  nb_of_vpcs = len(vpcs.get('Vpcs'))
  assert_that(nb_of_vpcs).is_equal_to(1)
  vpc = vpcs.get('Vpcs')[0]
  assert_that(vpc.get('IsDefault')).is_true()
  pass


@given('no EC2 instance')
def step_impl(context):
  global running_instances_filter
  instances = context.ec2_client.describe_instances(Filters=running_instances_filter).get('Reservations')
  assert_that(instances).is_length(0)


@when('i create the following EC2 instance in the default VPC')
def step_impl(context):
  instance_type = context.table.rows[0]["instance_type"]
  instance_count = context.table.rows[0]["instance_type"]
  vars = {
    'instance_type': instance_type,
    'count': instance_count,
    'name': "test-ec2-" + context.correlation_id
  }
  context.terraform_client.plan()
  context.terraform_client.apply(skip_plan=True, var=vars)


@then('there is exactly {count:d} instance with the following attributes')
def step_impl(context, count):
  global running_instances_filter
  instances = context.ec2_client.describe_instances(Filters=running_instances_filter).get('Reservations')
  expected_instance_type = context.table.rows[0]["instance_type"]
  print("coucou ", expected_instance_type)

  assert_that(instances).is_length(count)
  for instance in instances:
    actual_instance_type = instance.get('Instances')[0].get('InstanceType')
    assert_that(actual_instance_type).is_equal_to(expected_instance_type)
