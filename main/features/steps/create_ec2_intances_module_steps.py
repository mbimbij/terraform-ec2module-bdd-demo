from behave import *
import boto3
import json
from assertpy import assert_that

client = None


@given('the region "{region}"')
def step_impl(context, region):
  global client
  client = boto3.client('ec2', region_name='eu-west-3')
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


@when('we implement a test')
def step_impl(context):
  assert True is False
