from behave import *
import boto3
from bson import json_util
import json
from assertpy import assert_that

client = None
region = None

@given('the region "{_region}"')
def step_impl(context, _region):
  global client
  global region
  region = _region
  client = boto3.client('ec2', region_name=_region)
  pass


@given('an account with only the default VPC')
def step_impl(context):
  global client
  vpcs = client.describe_vpcs()
  nb_of_vpcs = len(vpcs.get('Vpcs'))
  assert_that(nb_of_vpcs).is_equal_to(1)
  vpc = vpcs.get('Vpcs')[0]
  assert_that(vpc.get('IsDefault')).is_true()
  pass


@given('no EC2 instance')
def step_impl(context):
  filters = [
    {
      'Name': 'instance-state-name',
      'Values': ['running']
    }
  ]
  instances = client.describe_instances(Filters=filters).get('Reservations')
  # print("coucou ", instances.get('Reservations'))
  print("coucou ", json.dumps(instances, indent=2, sort_keys=True, default=json_util.default))
  assert_that(instances).is_length(0)