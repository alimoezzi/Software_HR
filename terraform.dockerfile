FROM  alpine

RUN apk add ca-certificates
RUN wget -O /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.14.7/terraform_0.14.7_linux_amd64.zip
RUN unzip /tmp/terraform.zip -d /

ENTRYPOINT [ "/terraform" ]

USER nobody
