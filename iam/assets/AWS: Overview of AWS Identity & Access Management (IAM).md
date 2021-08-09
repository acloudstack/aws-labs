# AWS: Overview of AWS Identity & Access Management (IAM)

Description
This course looks at one of the key Security services within AWS, Identity & Access Management, commonly referred to as IAM. This service manages identities and their permissions that are able to access your AWS resources and so understanding how this service works and what you can do with it will help you to maintain a secure AWS environment. IAM is an important step in ensuring your resources are secure.

Within this course, we will look at the following topics:

What is Identity & Access Management? This lecture will explain what IAM means and why it’s necessary to implement and maintain control of this service.
Groups, Users & Roles: This lecture will define the differences between Groups, Users and Roles and how each of these objects are typically used
IAM Policies: This lecture we will discuss what IAM Policies are, how to create, modify and apply them within your AWS environment
Multi-Factor Authentication: This lecture will explain what MFA is and the best practices
Identity Federation: This lecture will explain how external identities (users who do not have IAM user accounts) can access your AWS resources through the use of identity providers
IAM Features: This lecture will focus on the information contained within IAM Account settings, the credential report and also how IAM integrates with KMS
Learning Objectives
Setup and configure users, groups, and roles to control which identities have the authorization to access specific AWS resources
Implement Multi-Factor Authentication
Create and implement IAM Policies allowing you to grant or restrict very granular and specific permissions across a range of resources
Implement a Password policy to align with your internal security controls
Understand when and why you may use Identity federation access
Understand how the Key Management Service (KMS) is used in conjunction with IAM
Intended Audience
This course has been designed for AWS administrators, security engineers, security architects or anyone who is looking to increase their knowledge of the IAM service in preparation for an AWS certification.

Prerequisites
To get the most from this course, it would be good if you already had some basic hands-on experience of AWS and its services, although it's not essential.

This course contains
8 lectures
Over 70 minutes of high definition video
Live demonstrations on key components within the course

## Introduction
Hello and welcome to this course where I shall be discussing the AWS Identity and Access Management Service, commonly referred to as I-AM or IAM. This is a key security service within AWS and is likely to be the first security service you will use and come across allowing you to configure specific access controls within your environment.

Before we start I would like to introduce myself. My name is Stuart Scott. I am one of the trainers here at Cloud Academy and I specialize in AWS, Amazon Web Services. Feel free to connect with me with any questions using the detail shown on the screen. Alternatively, you can always get in touch with us here at Cloud Academy using the community forum where one of our cloud experts will reply to your question.

This course has been designed for AWS administrators, security engineers, security architects or anyone who is looking to increase their knowledge of the IAM service in preparation for an AWS certification. This course will cover all features and elements of IAM which will include:

- What is Identity and Access Management: This lecture will explain what IAM means and why it's necessary to implement and maintain control of the service.
- Groups, Users and Roles: This lecture will define the differences between groups, users and roles and how each of these objects are typically used.
- IAM Policies: This lecture will discuss what IAM policies are, how to create, modify and apply them within your AWS environment.
- Multi-Factor Authentication: MFA. This lecture will explain what MFA is and its best practices.
- Identity Federation: This lecture will look at how to access your AWS resources using identities outside of the IAM service.
- IAM Features: This lecture will focus on the information contained with the IAM account settings, the credential report and also how IAM integrates with KMS, the Key Management Service.

By the end of this course you will be able to set up and configure users, groups and roles to control which identities have authorization to access specific resources. You will be able to implement Multi-Factor Authentication, create and implement IAM policies, allowing you to grant or restrict very granular and specific permissions across a range of resources, implement a password policy to align with your internal security controls, understand when and why you may use identity federation access and you'll understand how the Key Management Service, KMS, is used in conjunction with IAM.

Although this course will explain everything from the ground up to do with IAM, having some basic hands-on experience of AWS and awareness of other services may help, but it's not essential. Feedback on our courses here at Cloud Academy are valuable to both us as trainers and any students looking to take the same course in the future.

If you have any feedback, positive or negative, it would be greatly appreciated if you could use the comments section found in the landing page of this course. That brings us to the end of this lecture. Coming up next we're going to look at what is Identity and Access Management and what it actually means.

## What is Identity & Access Management?
Hello and welcome to this lecture where I shall provide an overview of what the Identity and Access Management service is and what IAM actually means. Firstly, I want to define what is meant by Identity and Access Management. I shall break this down into two parts, starting with identity management.

Identities such as AWS usernames are required to authenticate to your AWS account. Authentication is the process of presenting an identity, in this case, a username, and providing verification of the identity such as entering the correct password associated. The second part, access management, relates to authorization and access control.

Authorization determines what an identity can access within your AWS account once it's been authenticated to it. An example of this authorization would be the identity's list of permissions to access specific AWS resources. Access control can be classed as a mechanism of accessing a secured resource. For example a username and password, multi-factor authentication, MFA, or federated access. MFA and federated access will all be explained in greater detail as we go through the rest of this course.

So essentially IAM can be defined by its ability to manage, control and govern authentication, authorization and access control mechanisms of identities to your resources within your AWS account.

We do have an existing course dedicated to AWS Authentication, Authorization and Access Control mechanisms which goes into great detail on each topic. This course can be found here. Having an understanding of the different security controls from an authentication and authorization perspective can help you design the correct level of security for your infrastructure.

Now we know what IAM relates to, let me explain what the service actually does. As I just explained, the AWS IAM service is used to centrally manage and control security permissions for any identity requiring access to your AWS account and its resources. This is achieved by using different features within IAM consisting of:

- Users: These are objects within IAM identifying different users.
- Groups: These are objects that contain multiple users.
- Roles: These are objects that different identities can adopt to assume a new set of permissions.
- Policy Permissions: These are JSON policies that define what resources can and can't be accessed.
- And Access Control Mechanisms: These are mechanisms that govern how a resource is accessed.

Each of these features will be discussed in detail as I take you through this course.

Within AWS some services are regional and some are global. IAM is a global service, meaning that you do not have to create different users or groups within each AWS region that you have resources.

IAM covers all regions. IAM is the first service a user will interact with when using AWS, the reason being the identity needs to be authenticated by IAM before accessing any AWS resource. This could be via the AWS management console within your browser or via the AWS command line interface using an API call trying to gain access to a resource.

It's critical to understand how IAM works and what can be achieved via the service, but it's even more important to know how to implement its features. Without IAM there would be no way of maintaining security or control of who or what could access your resources and what they could do with them, both internally and externally.

IAM provides the components to maintain this management of access, but it's only as strong and secure as you configure it. The responsibility of implementing secure, robust and tight security within your AWS account using IAM is yours, the owners of the AWS account. You must define how secure your access control procedures must be, how much you want to restrict users from accessing certain resources, how complex a password policy must be and if users should be using multi-factor authentication.

All of this and much more is down to you to architect and implement and much of it will likely depend on your own security standards and policies within your information security management systems.

From within the AWS management console, the IAM service can be found under the Security, Identity & Compliance category and when accessed it will take you to the IAM dashboard.

From here and if you have the correct permissions, you will be able to administer all security from an IAM perspective. The initial dashboard of the IAM console will display information relating to the IAM uses sign-in link and this is a URL link that you can send to users who will need to gain access to your AWS management console.

This link can be customized by clicking on the customize button to make it easier to remember and read. If you have multiple AWS accounts, this customization will help you distinguish between your accounts.

IAM Resources. This section provides an overview of your IAM resources using a simple count of the number of users, groups, roles, customer manage policies and identity providers you have configured within IAM.

Security Status. This is populated with five best practices from a security perspective that AWS IAM recommends you configure when using IAM which may include activate MFA on your root account, create individual IAM users, use groups to assign permissions, apply an IAM password policy and rotate your access keys.

When you implement any of the list of best practices, the status of them will change from an orange warning sign to a green tick to show you have achieved and implemented a recommended best practice. I recommend you try to adopt these best practices at your earliest opportunity. Maintaining tight security is paramount when working with an IAM solution.

That brings us to the end of this lecture where we looked at what is meant by IAM, what the AWS IAM service is and does, where the service is located within the management console and what information is held on the IAM dashboard within the management console. In the next lecture I'm going to introduce you to users, groups and roles and the part they play within IAM.

## Users, Groups & Roles
Hello, and welcome to this lecture, where I am going to define the user, group and role objects within AWS IAM, and the differences between them. Following this, I'll provide a demonstration on how to set up and configure all three. Let's start with users.

Users are objects created to represent an identity. This could be a real person within your organization who requires access to operate and maintain your AWS environment. Or it could be an account to be used by an application that may require permissions to access your AWS resources programmatically. Users are simply objects representing an identity which are used in the authentication process to your AWS account.

When creating a new user, you have the option to create it via the AWS Management Console, or programmatically via the AWS CLI, Tools for Windows Powershell, or using the IAM HTTP API. For this and other lectures, I shall be using the AWS Management Console to demonstrate how to configure various elements of AWS IAM.

User object creation involves the following seven steps. Setting user details, by creating a user name, which can be up to 64 characters in length. Next, you'll select the AWS Access Type, either AWS Management Console Access, or programmatic access. To use the AWS Management Console Access, the user will need to be issued with a password.

For programmatic access, an access key ID and secret access key ID will be issued to be used with the AWS CLI SDKs or other development tools. You'll then need to define a password, if AWS Management Console Access was requested. Then, permission assignment for the use of policies attached to the user itself, or inherited from a group that the user can be assigned to, and you'll then need to review and confirm the information.

After this point, the creation of the user will take place, then you can download the security credentials within a CSV file, that will contain the user name, keys required for programmatic access, and the console login link, etc. These details can also be emailed to the new user, using the send email link.

I just want to cover a point I mentioned in step two. Access keys, which are required for programmatic access for authentication. These access keys are comprised of two elements, an access key ID, and a secret access key ID. The access key ID is made up of 20 random uppercase alphanumeric characters, such as the one on the screen.

The secret access key ID is made up of 40 random upper and lowercase alphanumeric and non-alphanumeric characters, such as the one displayed on the screen. During the creating of a user who requires programmatic access, you are prompted to download and save the details, as the secret access key ID will only be displayed once, and if you lose it, you will then have to delete the associated access key ID and recreate new keys for the user.

It's not possible to retrieve lost access key IDs as AWS does not retain copies. These access keys must then be applied and associated with the application that you are using, that requires the relevant access. For example, if you are using the AWS CLI to access AWS resources, you would first have to instruct the AWS CLI to use these access keys to authenticate and provide authorization.

The method of performing this association varies based on the application and system that you're using. However, once this association has taken place, it ensures that all API requests made to AWS are signed with this digital signature.

Once your user identity is created, you can view a summary of the object by selecting user, from within the user page of the console. This will show the user ARN, which is the Amazon Resource Name, which is a unique identifier of the object, the creation time of the user object, any attached policies that are associated with the user, any group memberships that the user belongs to, the details of the security credentials of the user, which also allows you to manage the current password, which enables you to change the password of the user.

You can also manage Multi Factor Authentication. Configuring MFA allows for an additional level of security to be applied, and this should be used for the AWS account owner, and any other users who have administrative access as a minimum. You can manage any signing certificates, and signing certificates are used for secure access to certain AWS product interfaces, and you can create new access keys for programmatic access, and it's a good practice to rotate and change your access keys periodically.

From here, you can also upload SSH public keys for AWS CodeCommit. These are used to authenticate access to AWS CodeCommit repositories, and you can also generate HTTPS Git credentials for AWS CodeCommit, and this allows you to authenticate HTTPS connections to AWS CodeCommit repositories.

Also on this screen, an access advisor shows a list of services that the user has permissions for, and the last time that those services were used with those assigned permissions. This is great to help you refine and revise the user permissions.

For those unaware of AWS CodeCommit is, it's a managed source control service that allows you to host secure and scalable private Git repositories. For more information on AWS CodeCommit, try our lab, which can be found here.

You may notice that on point four, when I mentioned permission assignments, that these can either be assigned to the user, or inherited from being a member of a group. Now, you may also remember from the previous lecture, when I explained about the security status on the IAM dashboard screen, that one of the best practices listed was use groups to assign permissions. With this in mind, and as best practice, you should consider using groups for permission assignment over assigning permission to individual users.

So let's now take a look at groups to help explain why. IAM Groups are objects much like user objects. However, they are not used in any authentication process. However, they are used to authorize access to AWS resources, through the use of AWS Policies. IAM Groups contain IAM Users, and these groups will have IAM Policies associated that will allow or explicitly deny access to AWS resources.

These policies are either AWS managed policies, that can be selected from within IAM, or customer managed policies, that are created by you, the customer. More information on IAM Policies will be discussed in a lecture devoted to this element.

Groups are normally created, that relate to a specific requirement or job role. Any users that are a member of that group inherit the permissions applied to the group. By applying permissions to the group instead of individual users, it makes it easy to modify permissions for multiple users at once. All you would need to do is modify the permissions of a group, and all users associated with the group would inherit the new access.

The alternative would be to update permissions for each and every user, which is time-intensive and prone to human error, which is why it's best practice to assign permissions to groups rather than individual users, especially in an enterprise environment. Creating a group is very simple, and is essentially a three step process.

Firstly, you give your group a meaningful name, you'll then assign permissions via policies, and finally, review your group. Once created, you can then assign users to the group.

From a limitation perspective, your AWS account has a default maximum limit of a hundred groups. To increase this, you'll need to contact AWS using the appropriate limit increase forms. Also, a user can only be associated to 10 groups, so do bear this in mind when assigning permissions.

Now we have looked at users and groups, let me now explain what an IAM role is. IAM Roles allow users and other AWS services and applications to adopt a set of temporary IAM permissions to access AWS resources.

This could be required to enforce security best practices. Firstly, let's look at an example of how the Amazon EC2 service uses an IAM role. Consider the following scenario. You have an EC2 instance running an application that requires access to Amazon S3 to Put and Get objects using the relevant API calls.

To allow access to S3, a set of credentials could be stored on the EC2 instance itself, allowing any application to use those credentials to gain access to the relevant bucket for any Put or Get API requests. However, in this scenario, you would need to manage these credentials manually, including the rotation of access keys, which is obviously an administrative burden.

To alleviate this issue, the EC2 instance could be assigned an IAM role that would contain the relevant permissions granting the EC2 instance and its applications access to S3 to perform the Put and Get API calls. This assignment can be made during the EC2 instant creation by selecting the role to be associated, or once the EC2 instance is up and running, a role could also be applied.

An existing role associated to an EC2 instance can also be replaced by a different role if required. From a security best practice perspective, you should always associate a role to an EC2 instance for accessing AWS resources over storing local credentials on the instance itself.

There are many advantages to roles, the IAM roles themselves do not have any access keys or credentials associated to them. Instead, when used, these credentials are dynamically assigned by AWS. Also, imagine you have a fleet of EC2 instances, all performing the same task, and using the same role. Now, consider that your existing application, which was used to perform Put and Get requests was now only required to perform Put requests only and Get requests must be denied.

To make the change, all you would need to do is to alter the permissions assigned to the IAM role, and all EC2 instances associated with that role would now have the correct access. If this same scenario happened by embedding credentials locally on the EC2 instance, then again, this would take a long time to replicate the change on every instance.

Let's now look at how IAM roles can be used with IAM users. There may be circumstances where you'll need to grant temporary access to AWS resources for a particular user. Instead of adopting their group permissions, or granting permissions to the individual user, which, as we know, is not best practice, we could simply allow the user to assume a role, temporarily replacing their existing permissions.

To do this, the user must first be given permission to adopt the role via an access policy. Let's take a deeper look at roles, to see how they are constructed and the different types of roles that are available.

There are currently four different types of roles that can be created, all of which serve a different purpose.

Firstly, the AWS Service Role. This role would be used by other services that would assume the role to perform specific functions based on a set of permissions associated with it. Some examples of AWS Service Role would be Amazon EC2, AWS Directory Services, and AWS Lambda, etc Once you have selected your service role, you would then need to attach a policy with the required permissions, and set a role name to complete its creation.

Secondly, the AWS Service-Linked Role. These are very specific roles that are associated to certain AWS services. They are pre-defined by AWS, and the permissions can't be altered in any way, as they are set to perform a specific function. Examples of these AWS Service-Linked Roles are Amazon Lex-Bots, and Amazon Lex-Channels. Once you have selected your service-linked role, you simply need to assign it a name and complete the creation. Remember, these roles do not allow you to modify the permissions assigned.

Thirdly, roles for Cross-Account Access. This role type offers two options. Providing access between AWS accounts that you own, and providing access between an account that you own and a third party AWS account.

This access is managed by policies that establish trusting and trusted accounts that explicitly allow a trusted principal to access specific resources. Many services use roles to allow cross-account access to resources. At a high level, these roles are configured as follows.

The trusting account is the account that has the resources that need to be accessed.

The trusted account contains the users that need to access the resources in the trusting account. A role is created in the trusting account. A trust is then established with the role by entering the AWS acount number of the trusted account. Permissions are then applied to the role via policies. And the group of users in the trusted account then need to have permissions to allow them to assume the role in the trusting account. These group of users would have a policy attached to the group, which would look something like the following, where the red text would be modified appropriately, with the relevant information.

Lastly, role for Identity Provider Access. This role type offers three different options. Grant access to web identity providers. This is used to create a trust for users using Amazon Cognito, Amazon, Facebook, Google, or any other open ID connect provider. Grant web single sign on to SAML providers. This allows access for users coming from a SAML provider, which stands for Security Assertion Markup Language. Grant API access to SAML providers.

This is similar to the previous option, but it allows access via the AWS CLI, SDKs, or API calls. For these options, a trust relationship is set up between the external identity providers to allow access to your AWS account's resources, using their existing identity provider login information. I shall be covering more on identity federation in greater depth in a lecture later in this course.

Now we have covered users, groups and roles. Let me provide a demonstration showing how each of these are created. Within the demonstration, I shall perform the following steps: 
- I will start by creating a group, 
- I will then attach permissions to this group by using an existing AWS managed IAM policy, 
- then I shall create a new user, as a part of this process, 
- I shall assign this user to the group, as per best practice.
- I shall then set up a new service role to be associated to an EC2 instance, 
- and I will then assign this role to an EC2 instance at creation.

Okay, so I'm at the home screen of the AWS Management Console, if I just type in IAM, it's the service, now I'll bring it up. And it'll take us to the dashboard.

Now, from here, to create our group, we'll need to go along to the left and select groups. Click on create new group. Give this group a name. Cloud Academy Course. Click on next step. And here, we can attach a policy to this group. So, this is where we attach a list of permissions that we want the group to have.

Let's filter this list by typing in S3, and that will just bring up all the policies that are S3 related. So, if we select this AWS Managed Policy, you can tell this is AWS Managed because it has the little AWS icon here, and any custom policies are, just blank here. But later in the course, I'll explain the difference between AWS Managed and custom managed.

But for now, let's just select the Amazon S3 full access. And you go down to next step, and that's pretty much it, so here we just need to review what, the settings we've made, so we've given it a group name and we've given it a policy as well for permissions. And then click on create group. And that's our group created, now, if you want to take a look at that, if we select it here, CA Course, and then we can see we have three tabs, user, permissions, and access advisor.

So the users tab, we can use this to add users to the group, but at the minute it doesn't have any users, and we can see up here, users in this group is zero. If we want to look at permissions, this is the policy that we applied, and then we can have a look at this policy. And it's very simple, it simply allows all actions within S3 to any resource. But we'll cover more of the policies later in the course. And then, access advisor, and this simply shows the service permissions granted to the group, and when they were last accessed.

So, what we need to do now is add some, add a user to the group.

So, let's create a new user, and for this, we go over to users. Add user, let's give it a user name, so we'll call it CA user one. And then down here, we can select the access type, and we can have programmatic access, which will give the user an access key ID and secret access key, or we can just allow them to the AWS Management Console, which will give them a password to sign in, or they can in fact have both.

For this example, I'm going to give them programmatic access and also management console access as well. So we can allow the console to auto-generate a password, or we can type in a custom password here. I'm going to leave it as auto-generated, and we can set this tick box here to ensure the user creates a new password the next time they sign in.

So next, if we go to permissions, now from here we've got a few options, we can add this user to a group directly from here, we can copy permissions from another user, or we can attach an existing policy directly to the user. Now, attaching policies directly to a user is not best practice, it's always best to add users to a group, and then attach policy to that group.

So, what we can do here, we can attach the user directly to a group. So, as that's already selected, we have the options down here of the different groups, now we created the CA Course group, so we're going to attach it to that, and as we can see, that gives him S3 full access. Click on next to review.

And now we can see the details that we've entered here, so we have the user name of CA user one, the access type, which is programmatic and console access, the password is auto-generated, and it requires a password reset, and permissions we've given them is via this group here, this CA Course, which we created just a few minutes ago. And you've created a user, and that's it.

The user has been created, and here we can have the access key ID, and also the password as well, so we can send an email directly to the user that will give them the credentials, you can also show the access key and password here as well, so you can make a note of those, if you need to.

You can also download these credentials as a CSV file, so I'll show you what that looks like. The same credentials, the username, the password and the access key et cetera. And also, a console link to allow them to sign in. So let's go back to the user, so that's created we have the credentials, let's click close, and now if we go back to our groups, click on our CA Course group, we can see that this now has one user attached.

So, this user will inherit the permissions from this group. Okay, so what we've done is we've created a group, we assigned that group permissions, using an AWS Managed Policy, we then created a user, and added that user to the group, so that user now inherits the permissions that's applied to that group.

Now, the last part of this demonstration, I just want to show you how to create a role, and we're going to create a role and assign it to an EC2 instance. So I've come across to the, the role section here. Here's a list of existing roles, click on new role. Now I want this to be an AWS Service Role, and here we have Amazon EC2, which allows EC2 instances to call aid of its services on your behalf.

So I'm going to select that role, I'm going to apply permissions, this time I want to look for RDS, and allow RDS full access. Click on next step. Give this role a name. Call this Cloud Academy RDS Full access. There's a description that you can change there, if you need to, I'm just going to leave that as default for this demonstration.

We can see our policy here, that we just added. Then click on create role. Okay, so now what we want to do is create an EC2 instance and associate that role with the instance. So, let's go across to EC2, just going to very quickly launch a new instance. So, Linux, AMI, D2 Nano, okay, cross to configure, just going to leave all that as default, and then down here, we can see we have an IAM role.

Now if we click on this drop-down list, we can see that we have two roles, this is the one that we just created just a moment ago, and then we can, review and launch, and we can see here that in our summary, if we go to our instance details, we can see that we have the IAM role there as well. And if we launch the instance, click on launch, go across to view, and again, we can see in the instance details down here, that it has that role associated.

So this EC2 instance has full access to RDS, so this EC2 instance can contact RDS and carry out any API calls relating to it. Now what I just want to quickly show you as well, recently, AWS allowed you to change the role once it was associated to an EC2 instance, before this, the only way you could attach a role to an EC2 instance was on creation, but now you can change it once it's up and running.

So, let's go across to actions, I've got the instance selected here, actions, and if we go down to instance settings, and we can say, attach/replace IAM role. And now again, we can select our role, and we have this other one here, S3 full access, simply change it there, click on apply, and then you get a message says, operation succeeded.

And we can now look down at the instance details, and we can change that the role permissions for this instance has changed, it now has S3 full access permissions. So, which means, this EC2 instance can perform any API call to S3. And that brings us to the end of this demonstration. Thank you.

We have now come to the end of this lecture. Coming up next, I will be discussing IAM policies, like the one we just attached to our group and role in the previous demonstration.

## IAM Policies
Hello and welcome to this lecture. Where we will be taking a deeper look at IAM policies and how these are created, modified, and constructed. I will also show you the syntax and structure of these policies.

So as we already know, IAM policies are used to assign permissions to users, groups, and roles. But what do these policies look like? IAM policies are formatted as JSON documents, Javascript objectmentation. And each policy will have at least one statement, where the structure may look like this example. Let me break the structure of this policy down to allow you to understand each element.

- Version: This going to the policy language version and at the time of writing this course, the current policy version is 2012-10-17.
- Statement: This defines the main element of the policy, which will also include other sub-elements, including Sid, Action, Effect, Resource, and Condition. These elements will identify the level of access, granted or denied, and to which resource.

So let's now understand what each of these are for. Sid. 
- The Sid Statement ID is simply a unique identifier within the Statement array. As you add more permissions, you will have multiple Sids within the Statement. 
- Action. This is the action that will either be allowed or denied, depending on the value entered for the Effect element. Actions are effectively API calls for different services. As a result, different Actions are used for each service. For example, for delete bucket action is available for s3, but not for ec2. And likewise, the create key pair action is available for ec2 but not s3. The Action is prefixed with the associated AWS service.

For example, you can see on the screen here we have two Actions for cloudtrail, one is to CreateTrail and the other is to DeleteTrail. Or you could, as seen on screen, use an asterisk as a wild card which represents all Actions for the cloudtrail service, essentially granting full access to the service.

- Effect: This element can either be set to allow or deny, which will either grant or restrict access for the previous Actions defined in the statement. These two options are explicit. By default, access to your resources are denied and, so therefore, if this is set to allow, it replaces the default deny. Similarly, if this was set to deny, it would override any previous allow.

- Resource: This element specifies the actual resource you wish the "Action" and "Effect" to be applied to. AWS uses unique identifiers, known as ARNs, Amazon Resource Names to specify specific resources. Typically, these ARNs follow a syntax of.

- Partition: This relates to the partition that the resource is found in. For standard AWS regions, this section would be AWS. 
- Service: This reflects the specific AWS service. For example, s3 or ec2. 
- Region: This is the region that the resource is located. Some services do not need the region specified, so this can sometimes be left blank.
- Account-id: This is your AWS account-id, without hyphens. Again, some services do not need this information, and so it can be left blank.
- Resource: The value of this field will depend on the AWS service you are using. For example, if I were using the Action "s3:PutObject", then I could use the bucket then I wanted those permissions to apply to using the following ARN.
- Condition: This is an option element that allows you to control when the permissions will be effective based upon set criteria. The element itself is made up of a condition and a key-value pair. And all elements of the condition must be met for the permissions to be effective. In the example, the IP address is the condition itself, which the key-value pair will be effective against.

The AWS Source IP is the key and the IP address is the value of the key. So effectively, what this is saying is if the Source IP address of the user who is using the policy is within their 10. 10. 0. 0/16 network range, then allow the permissions to be used.

As I mentioned previously, you can have multiple Sids within a statement, each granting a different level of access.

The example below demonstrates this and I have highlighted each a different color to show the separation.

The first Sid allows any resource full access to "cloudtrail" as long as their Source IP address is within the 10. 10. 0. 0/16 range.

The second Sid allows any resource to have full access to "autoscaling".

The third Sid allows the creation and deletion of s3 buckets within the "iam-course-ca" bucket on s3.

Typically, IAM policy will have these elements that we have just discussed. But sometimes, additional elements are and can be used. A full listing of these elements can be found here. Now we know what an IAM policy looks like, I want to talk to you about two different types of IAM policies available.

These being Managed Policies and In-line Policies. Managed policies come in two different flavors, AWS Managed Policies and Customer Managed Policies. These managed IAM policies can be associated with a Group, Role, or User. Although assigning to a User is not best practice, the difference between AWS and Customer Managed is as you would expect.

The AWS Managed policy have been pre-configured by AWS and made availble to you to help with some of the most common permissions that you may wish to assign. For example, these two AWS Managed policies covering s3. By selecting one of these policies, the necessary IAM JSON policy and its permissions will already be configured.

The two policies are configured as follows. The difference between the two separating full access from ready only is made clear in the "Action" element. The great thing about these AWS Managed policies is that you are able to edit them and make tweaks and changes before saving it as a new policy. This then becomes a Customer Managed policy.

This is great when an AWS Managed policy is almost as you need it, as it saves you time creating the policy from scratch. Let's look at a scenario.

A user requires read only access to everything on s3, plus the ability to create new buckets for management purposes. To create the appropriate policy for this user, we should consider using the AWS Managed policy "AmazonS3ReadOnlyAccess", which would give us the "ReadOnly" permission. But it would need to be copied and altered to allow the creation of buckets too.

Therefore, during the creation of this policy, the AWS Managed "AmazonS3ReadOnlyAccess" policy would be selected and then edited, as shown in red, to grant the additional "CreateBucket" permissions. So Customer Managed policies are any IAM policies that do not follow a pre-defined AWS Managed policy.

There are a number of ways to create a Customer Managed policy. These being the following: 
- Copy an AWS Managed policy. This is what we just covered, where an existing AWS Managed policy is used and then edited to create new Customer Managed policy. 
- The Policy Generator. This allows you to create a Customer Managed policy by selecting options from a series of dropdown boxes.
- And you can create your own policy. If you are proficient in JSON and the syntax of IAM policy writing, then you can create your own policies from scratch or paste in a JSON policy from another source.

I now want to give you a quick demonstration of how to create a policy in each of these three ways. The demonstration will include: how to create a Customer Managed policy by editing an existing AWS Managed policy; how to create a Customer Managed policy using the Policy Generator; how to create a Customer Managed Policy from scratch; and how to validate your policies and why this is important.

Okay, I'm at the AWS Managed console and if I just go across to "IAM", and then across to "Policies", and "Create Policy", and here we have three options: "Copy an AWS Managed Policy", "Policy Generator", or "Create Your Own Policy". So I'm going to cover each option, but start with I'm going to copy an AWS Managed Policy and create a Customer Managed Policy by doing so.

So if we click on "select", we can see here a list of AWS Managed policies. Now for my policy, I want to have a policy that allows s3 Full Access and also ec2 Full Access within the same policy. So if I search for s3, we can see here that we have an AWS Managed policy that provides full access to all buckets for the AWS Management Console.

So, that's what I want, but I also want to add ec2 Full Access as well. So if I select that, and we can see here that this is the policy, the JSON policy for these permissions, we can see the Effect is "Allow", the Action is "s3" and the Resource is "all". So I want to edit this to also include ec2 Full Access.

So I can copy that section there, paste that in, and change the Action here to "ec2". So now what we have IR two elements within the statement one that allows full access to s3 and another allows full access to ec2. Now to verify that I have entered this correctly, there is a "Validate Policy" button down here.

Now always worth clicking on that when you're creating your policies 'cause it'll let you know if there's any errors within the policy document that you need to correct. So if I click on "Validate Policy", we can see here there's an error on line 8, that's expected comma instead of a bracket. So if we go down to line 8 and add our comma in, go down to "Validate Policy" again, we can see that the policy is now valid.

So let's give this policy a name. So we've got "s3", let's say and "ec2FullAccess", click on "Create Policy". And our policy has now been created. Now if we go to filter here on "Policy Type" and select "Customer Managed" we can see here that this has filtered all the Customer Managed policies that I have and the latest one here is the "Amazons3andec2FullAccess".

Now we can have a look at that. Now we can see that is allows two services ec2 and s3, Full Access, to All Resources. And if you want to see the policy document, then we can just view it there and we can also edit the policy again. So let's create that same policy but for a different method. So, if we go "Create Policy", this time use the Policy Generator.

So click on "Select". And this uses a number of dropdown boxes to make it easier if you're not too familiar with JSON and editing policies, etc. So our Effect is "Allow", we can select our service, so first of all we want "AmazonS3". Actions, we want "Full Access", so it's "All Actions", but you can select different ones here if you just want to create or delete buckets, etc.

Or delete objects. But for this demonstration we want "Full Access". And the Amazon Resource Name we want "All Resources", so just put in the asterisks. Click on "Add Statement". Now we want to also allow "ec2" as well, so let's find that. "Amazon EC2" Actions. "All Actions", "All Resources", "Add Statement".

So here you can see the statements that we've added so the Effect is to both allow the action of "s3" and "ec2" and to all resources. We've gone to next step. We can see that the policy have been created for us it's laid out slightly differently but the Effect is still the same. So we can see we have the statement ID, the Effect of "allow", the Action is "s3", with "all resources".

And if we have a look down here, we have another statement ID with Effect of "Allow" and the Action of "ec2" and "all resources". We click on "Validate Policy". Policy is valid. We give the policy a name, "S3andEC2FullAccessFromThePolicyGenerator". Create Policy. And again, if we go down to "Policy Type", "Customer Managed", we can see that we have our policy here.

"Customer Managed", and again full access for EC2 and S3 to All Resources. So let's create the policy for the third time. Exactly the same. But this time creating your own policy. So this will simply open up a blank policy editor document. And here you can write your own policy as you need to or paste it in from another document, which is exactly what I'm going to do.

So all I need to do is paste it into this document here, and as you can see, I have the Action of "s3" for everything Effect "Allow", Resource "Everything", and the same for "ec2". Now if I "Validate Policy" to make sure I've created it correctly, we can see I need a policy name. So let's give this "EC2andS3Custom", "Validate Policy", and we can see the policy is valid.

Go to "Create Policy". And again, one final time, "Customer Managed", and we can see "EC2andS3Custom". And again we can see that services EC2 and S3 has Full Access to All Resources. So that's the three different ways that you can create a Customer Managed Policy. You can select whichever way is easier for you.

If you're not too familiar with writing your own policies then the Policy Generator is probably easiest. Or if you want to use the bulk of an existing AWS Managed Policy to create your own, then the top option is probably best. So each of those policies that we created were all the same. They all gave full access to ec2 and s3, it was just different ways to create them.

That brings us to the end of this demonstration. Thank you.

Now we have covered Managed Policies, I want to go back to Inline Policies. Whereas a Managed Policy could be attached to multiple users, groups, and roles, Inline Policies cannot. An Inline Policy is directly embedded into a specific User, Group, or Role, and as a result, it is not available to be used by multiple identities.

To add an Inline policy for within the AWS Management Console, you must select the User, Group, or Role, select the "Permissions" tab, and click on "Click Here" to add an Inline policy. You will then be given two options in creating your Inline policy: one, using the Policy Generator, or two, writing your own custom policy.

When the policy is being created, it is then associated to your IAM object. As a result, Inline policies do not show up under the Policies list with IAM, as they are not publicly available for other Users, Groups, or Roles to use with your account like Managed Policies are. Inline policies are typically used when you don't want to run the risk of the permissions being used in the policy for any other identity.

When the User, Group, or Role is deleted, Inline policy is also deleted, as this is the only place where the policy exists. With the ability to attach multiple Managed and Inline policies to an identity object in IAM, what happens when there are conflicting permissions assigned to the same User for example?

The rules for reviewing for permissions is very simple and can be summarized as follows: By default, all access to a resource is denied. Access will only be allowed if an explicit "Allow" has been specified within a policy associated with an identity. If a single "Deny" exists within any policy associated to the same identity against the same resource, then that "Deny" will override any previous "Allow" that may exist for the same resource and action.

An explicit "Deny" will always take precedence over an explicit "Allow".

That now brings us to the end of this lecture covering IAM Policies. Coming up next, I am going to give you an overview of Multi Factor Authentication, MFA.