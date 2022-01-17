---
marp: true
---


## Monitoring
- What: 
  - Cloud monitoring is a method of reviewing, observing, and managing the operational workflow in a cloud-based IT infrastructure. 
  - Monitor, Detect, Act

---

- Why:
  - Operational Excellence - Operational Health
  - Security - Security Auditing
  - Performance - Application Performance
  - Reliability - 
  - Cost - Utilization of Resources

---

- How:
  - CloudWatch - What is happening in AWS Account
    - Alows the users to monitor all resources in AWS
    - Monitors your resources
    - Cofigures alarms to Alert
    - Take Automated Actions
    - AWS Services continiously publish metrices to CloudWatch.
    - Custom Metrices can be created
  
---

  - CloudTrail - Who did what and when.
    - Logs All activities and who performed that action
    - Logs all the API calls
  - VPC Flow Logs
    - VPC Flow Logs is a feature that enables to capture information about the IP traffic going to and from the VPC. 
  
---
## Benefits


---

## Help:
- https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-default
- http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
- https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html#create-cloudtrail-table-understanding

---
## Misc

  uptime
  sudo yum install stress -y
  sudo amazon-linux-extras install epel -y
  sudo yum install stress -y
  sudo stress --cpu  8 --timeout 20

