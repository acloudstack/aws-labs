# Demo

- Demo
- 
- Store:
- Distribute:
- Analyze:
- Secure:
- Use Case:
- 

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
                        "aws:SourceIp": "49.37.41.95/32"
                    }
                }
            }
        ]
    }

## static website 
- refer to the index.html and error.html