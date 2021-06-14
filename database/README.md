---
marp: true
---

## RDS and DynamoDB

---
## Topics
- **Usecases for Database**
- **Create a RDS(MySQL) Instance**
- **Connect to RDS using MySQL Client**
- **Create a Database**
- **Connect to RDS from WebServer**
- **Create a DynamoDB Table**
- **Create a DynamoDB Global Table**
- **Create Items**
	
---

## What is RDS
## RDS Usecases
## What is DynamoDB
## DynamoDB Usecases

---

## Web Application
![alt text right](./assets/api.png "Web Application")

---

## RDS
![alt text right](./assets/rds.png "RDS")

---
## DynamoDB

![alt text right](./assets/dynamodb.png "DynamoDB")

---

      sudo yum -y install mysql
      mysql -h rds-lab.czazhlxuipph.us-west-2.rds.amazonaws.com -u admin -p
      CREATE DATABASE employee;