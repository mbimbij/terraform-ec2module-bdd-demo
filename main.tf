resource "aws_instance" "web" {
  count = var.instance_count
  ami = var.ami
  instance_type = var.instance_type
  subnet_id = var.subnet_id

  tags = {
    Name = var.name
  }
}