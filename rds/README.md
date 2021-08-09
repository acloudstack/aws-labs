---
marp: true
---

## RDS
- Relational
  - Engines
    - MySQL
    - Oracle
    - SQLServer
    - PostgreSQL
  - Structure:
    - Rows and Columns
    - Fixed Schema
    - SQL Query
    - Vertical Scalable Read/Write
    - Horizontal Scalability for Read
  - Consideration
    - Compute Type - R is preferred
    - Compute Size
    - EBS Volume 
      - SSD
        - General Purpose
        - Provisioned IOPS
    - Durablity
    - Availability
- AWS Managed


---
## Topics
- **Usecases for Database**
- **Create a RDS(MySQL) Instance**
- **Connect to RDS using MySQL Client**
- **Create a Database**
- **Connect to RDS from WebServer**
- **Create Items**
	
---

## What is RDS
## RDS Usecases
## What is DynamoDB
## DynamoDB Usecases

---

## RDS
![alt text right](./assets/rds.png "RDS")

---

      sudo yum update -y
      sudo yum -y install mysql
      mysql -h <DB_CONNECTION_STRING -u <DB_USER> -p
      CREATE DATABASE employee;

---

## Help

- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html
