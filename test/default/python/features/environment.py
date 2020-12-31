from python_terraform import *
import uuid

target_dir = '../../../examples/default'


def before_all(context):
  context.correlation_id = str(uuid.uuid4())
  context.terraform_client = Terraform(working_dir=target_dir)


def after_all(context):
  context.terraform_client.destroy()
