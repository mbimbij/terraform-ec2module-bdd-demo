from python_terraform import *
import uuid


def before_all(context):
  context.correlation_id = str(uuid.uuid4())
  context.terraform_client = Terraform()


def after_all(context):
  context.terraform_client.destroy()
