provider "aws" {
  region = var.region
}
module "my_ec2" {
  source = "../.."
  count = var.instance_count
  name = var.name
  instance_type = var.instance_type
}
