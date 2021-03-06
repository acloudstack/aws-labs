---
marp: true
---
# Demo
1. Create a S3 bucket
2. Create Folder
3. Create/Read/Update/Delete Objects
4. Access from Console and CLI
5. Bucket Policy to Allow/Deny access
6. Host Static WebSite
7. S3 Notification
8. S3 Versioning 
9. Cross Region Replication
10. S3 Access Log
11. Analyze Data

---

## bucket policy
    {
        "Version": "2012-10-17",
        "Id": "Policy1628168355828",
        "Statement": [
            {
                "Sid": "Stmt1628168351212",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": [
                    "arn:aws:s3:::test-bucket-9876543210",
                    "arn:aws:s3:::test-bucket-9876543210/*"
                ]
            },
            {
                "Sid": "SourceIP",
                "Effect": "Deny",
                "Principal": "*",
                "Action": "s3:*",
                "Resource": "arn:aws:s3:::test-bucket-9876543210/test/*",
                "Condition": {
                    "NotIpAddress": {
                        "aws:SourceIp": "1.2.3.4/32"
                    }
                }
            }
        ]
    }

---

## static website 
- index.html
- error.html

## pre-signed url 
    - aws s3 --profile devuser-mycloudstack presign s3://test-bucket-9876543210/s3.png

    - aws s3 --profile devuser-mycloudstack ls s3://test-bucket-9876543210 --recursive

---

## Help
- https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/
- https://www.thegeekstuff.com/2019/04/aws-s3-cli-examples/
- https://docs.aws.amazon.com/cli/latest/reference/s3/
- https://www.redhat.com/en/topics/data-storage/file-block-object-storage


