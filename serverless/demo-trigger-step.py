import json
import logging
import boto3
import uuid
import time
import os

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	logger.debug('Event: ')
	logger.debug(event)
	data = {'user_id': ''}
	
	#if 'params' in event.keys():debug
	#	if 'querystring' in event['params'].keys():	return (json.loads(response1['output']))
	
	#		if 'user' in event['params']['querystring'].keys():
	#			data['user_id'] =  event['params']['querystring']['user_id']
	
	if 'queryStringParameters' in event.keys():
		if event['queryStringParameters'] is not None:
			if 'user_id' in event['queryStringParameters'].keys():
				data['user_id'] =  event['queryStringParameters']['user_id']
				
	
	
	STEP_FUNCTION_ARN = os.environ['STEP_FUNCTION_ARN']
	print(STEP_FUNCTION_ARN)
	transactionId = str(uuid.uuid1())

	response = client.start_execution(
		stateMachineArn=STEP_FUNCTION_ARN,
		name=transactionId,
		input=json.dumps(data)	
	)
	
	print(response)
	
	time.sleep(10)
	
	response1 = client.describe_execution(
    	executionArn=response['executionArn']
	)
	
	return (json.loads(response1['output']))