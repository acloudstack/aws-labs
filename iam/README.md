---
marp: true
---


# IAM

---
Identity Management - Identity in AWS are are required for authentication 
Access Management deals with authorization. What the users can access once they are authenticated to AWS.

Access control is a mechanism of accessing a secured resource

The IAM service manage and control the security permissions in AWS.

IAM Components: User, Group, Role, Policy, Access Control mechansims(sts, mfa, key)

IAM is a global service

AWS Services can be accessed through Console, CLI and via REST API calls.

IAM - 
  - Gateway to your aws account
  - It is as robust as you configure it
  - The responsibility if maintaining IAM is yours.
    - You define how your user access your user accounts
    - You decide what is your password policy - number of characters, rotation
    - What is your restriction policy - least previlege

---

User represent Identity. Idenitty can be a real person or an Application. 

User
Group
Policy
Role

---

IAM Policy - 
  - Version
  - Statements - can have multiple statements
    - sid - statement id, unique identifier for a statement
    - Effect
    - Action 
    - Resource
    - Condition
    - Principal - needed for bucket policy

---

## Help
- https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html
