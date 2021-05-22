1. Lambda Function - Pilot Light
   
        import boto3
        import json

        def lambda_handler(event, context):
            # TODO implement
            
            sts_connection = boto3.client('sts')
            acct_b = sts_connection.assume_role(
                RoleArn="arn:aws:iam::697752106569:role/ec2-full-access-can-be-assumed-by-acloudstack",
                RoleSessionName="cross_acct_lambda"
            )
            
            ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
            SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
            SESSION_TOKEN = acct_b['Credentials']['SessionToken']
            
            # print("sts successful:")
            # create service client using the assumed role credentials, e.g. ec2    
            ec2_client = boto3.client(
                'ec2', 
                region_name='us-east-2',
                aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY,
                aws_session_token=SESSION_TOKEN
            )
            instance_id = 	"i-0de30c00743bb4ce1"
            ec2_client.start_instances(InstanceIds=[instance_id])
            print("The instance is started:" + instance_id)  
            return {
                'statusCode': 200,
                'body': json.dumps('Hello from Lambda!')
            }


2. Lambda Function - Warm Standby

        import boto3
        import json

        def lambda_handler(event, context):
            # TODO implement
            
            sts_connection = boto3.client('sts')
            acct_b = sts_connection.assume_role(
                RoleArn="arn:aws:iam::697752106569:role/ec2-full-access-can-be-assumed-by-acloudstack",
                RoleSessionName="cross_acct_lambda"
            )
            
            ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
            SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
            SESSION_TOKEN = acct_b['Credentials']['SessionToken']
            
            # print("sts successful:")
            # create service client using the assumed role credentials, e.g. ec2    
            asg_client = boto3.client(
                'autoscaling', 
                region_name='us-east-1',
                aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY,
                aws_session_token=SESSION_TOKEN
            )
            response = asg_client.set_desired_capacity(
                AutoScalingGroupName='asg_1',
                DesiredCapacity=1,
                HonorCooldown=True
            )

            return {
                'statusCode': 200,
                'body': json.dumps('Hello from Lambda!')
            }
