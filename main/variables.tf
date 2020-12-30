variable "region" {
  type = string
  default = "eu-west-3"
}

variable "instance_type" {
  type = string
  default = "t2.micro"
}

variable "instance_count" {
  type = number
  default = 1
}
variable "name" {
  type = string
  default = "test-ec2-instance"
}