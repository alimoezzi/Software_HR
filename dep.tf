provider "aws" { 
  profile = "default"
  region = "us-east-2"
}

resource "aws_s3_bucket" "prod_tf_sample_aws_bucket" {
  bucket = "sarme-tf-sample-2021"
  acl = "private"
}

resource "aws_default_vpc" "default" {
  
}
resource "aws_security_group" "prod_web" {
  name = "prod_web"
  description = "Allow usual http https ports inboud only and all allowed for outbound" 

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # allow all ranges
  }

  egress { # outbound traffic
    from_port = 0 # allow all ports
    to_port = 0
    protocol = "-1" # allow all protocols
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    "Terraform": "true"
  }
}

/*resource "aws_instance" "prod_web"{
  instance_count = 2

  ami = "ami-03e2ce3ac31c06bff"
  instance_type = "t2.nano"

  vpc_security_group_ids = [ aws_security_group.prod_web.id ]
  
  tags = {
    "Terraform": "true"
  }
}*/

module "ec2_cluster" {
  source                 = "terraform-aws-modules/ec2-instance/aws"
  version                = "~> 2.0"

  name                   = "my-cluster"
  instance_count         = 2

  ami                    = "ami-03e2ce3ac31c06bff"
  instance_type          = "t2.micro"
  subnet_id = aws_default_subnet.default_az1.id 

  vpc_security_group_ids = [ aws_security_group.prod_web.id ]

  provisioner "file" {
    source      = "./"
    destination = "/app"
  }

  provisioner "local-exec" {
    command = "python3 -m pip install docker-compose >> private_ips.txt"
  }

  provisioner "local-exec" {
    command = "cd /app && docker-compose up"
  }
  
  tags = {
    Terraform   = "true"
  }
}

resource "aws_default_subnet" "default_az1" {
  availability_zone = "us-east-2a"
  tags = {
    Terraform   = "true"
  }
}

resource "aws_default_subnet" "default_az2" {
  availability_zone = "us-east-2b"
  tags = {
    Terraform   = "true"
  }
}

resource "aws_eip_association" "prod_web"{
  instance_id = module.ec2_cluster.id[0] #.* refer to all isntances
  allocation_id = aws_eip.prod_web.id
}

resource "aws_eip" "prod_web" {
  
  tags = {
    "Terraform": "true"
  }
}

resource "aws_elb" "prod_web" {
  name = "prod-web" # only -
  instances = module.ec2_cluster.id.*
  subnets = [aws_default_subnet.default_az1.id, aws_default_subnet.default_az2.id]
  security_groups = [ aws_security_group.prod_web.id ]
  listener {
    instance_port = 80
    instance_protocol = "http"
    lb_port = 80
    lb_protocol = "http"
  }

  tags = {
    "Terraform": "true"
  }
}
