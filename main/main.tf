provider "aws" {
  region = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}
module "my_ec2" {
  source = "./terraform_modules/ec2"
  count = var.instance_count
  name = var.name
  instance_type = var.instance_type
}
