---
marp: true
---


# Advanced Networking Lab

---

## Recap:
  - VPC
  - Subnets - Public, Private
  - Routing - Routing Table
  - Security - NACL, Security Group
  - Governance - Flow Logs
---
## Use Cases:
  - Internet Gateway
  - VPC Peering
  - Transit Gateways
  - Private Link
  - VPN 
  
---

## Lab - VPC Peering
  - Create VPC-1 - 10.1.0.0
    - Create Public Subnet - 10.1.1.0/24 
    - Create Private Subnet - 10.1.0.0/24
  - Create VPC-2 - 10.2.0.0
    - Create Private Subnet - 10.2.0.0/24
  - Create VPC-3 - 10.3.0.0
    - Create Private Subnet - 10.3.0.0/24
---

![alt text right](./assets/vpc-peering.png "VPC Peering")

---

## Lab - Transit Gateway
---

![alt text right](./assets/transit_gateway.png "Transit Gateway")

---

## AWS Private Link - S3

      aws s3 ls --region us-east-1 --endpoint-url https://bucket.vpce-0014109cef9cac25b-x62xe7yw.s3.us-east-1.vpce.amazonaws.com
      

      aws s3 ls s3://acloudbucket-12345-accesslogs --region us-east-1 --endpoint-url https://bucket.vpce-0014109cef9cac25b-x62xe7yw.s3.us-east-1.vpce.amazonaws.com



---

## Help
  - https://www.davidc.net/sites/default/subnets/subnets.html
  - https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html
  - https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html
