#import json

#def lambda_handler(event, context):
    # TODO implement
#    return {
#        'statusCode': 200,
#        'body': json.dumps('Hello from Lambda!')
#    }

import boto3
import datetime
import json
import logging
import os
import urllib.parse
from botocore.exceptions import ClientError

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info('Loading function')

# Environment variables
sqs_queue_url = os.getenv("SQS_QUEUE_URL")
table_name = os.getenv("TABLE_NAME")

# AWS clients
sqs_client = boto3.client('sqs')
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    logger.debug('Received event: {}'.format(event))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'],
        encoding='utf-8'
    )
    messages = read_csv_file(bucket, key)
    logger.debug('Messages: ')
    logger.debug(messages)
    process_messages(messages)
    
    return 0


def read_csv_file(bucket, key):
    """
    Read messages from CSV file.

    :param bucket: S3 Bucket Name
    :param key: CSV file name
    :return: messages
    """
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        logger.debug('CONTENT TYPE: {}'.format(response['ContentType']))
        if response['ContentType'] == 'text/csv':
            messages = response['Body'].read().decode('utf-8').split()
            messages.pop(0)  # remove header row
            return messages
    except Exception as e:
        logger.error(e)
        logger.error('Error getting object {} from bucket {}. '
                     'Make sure they exist and your bucket is in the same region as this function.'
                     .format(key, bucket))
        raise e


def process_messages(messages):
    """
    Process messages.

    :param messages: Messages from CSV file
    :return: 0 or -1
    """
    try:
        for row in messages:
            message = row.split(',')
            message = convert_message(message)
            message = json.dumps(message, separators=(',', ':'))
            logger.debug(message)
            response = send_sqs_message(message)
            if response is not None:
                logger.info('Sent SQS message ID: {}'.format(response['MessageId']))
        return 0
    except Exception as e:
        logger.error(e)
        return -1


def convert_message(message):
    """
    Convert CSV file row to message dictionary object.
    Drop millisecond precision from timestamp conversion.

    :param message: CSV file row containing a message
    :return: Message dictionary object
    """
    #converted_ts = datetime.datetime.fromtimestamp(float(message[0]))
    message = {
        'TableName': table_name,
        'Item':
            {
                'PK':
                    {
                        'S': message[0]
                    },
                'SK':
                    {
                        'S': message[1]
                    },
                'LSI1':
                    {
                        'S': message[2]
                    },
                'Name':
                    {
                        'S': message[3]
                    },
                'Main':
                    {
                        'S': message[4]
                    },
                'Side':
                    {
                        'S': message[5]
                    },
                'Drink':
                    {
                        'S': message[6]
                    }
            }
    }
    return message


def send_sqs_message(message):
    """
    Send JSON-format message to SQS.

    :param message: Dictionary message object
    :return: Dictionary containing information about the sent message. If
        error, returns None.
    """

    try:
        response = sqs_client.send_message(
            QueueUrl=sqs_queue_url,
            MessageBody=message,
            DelaySeconds=0,
            MessageAttributes={
                'Method': {
                    'StringValue': 'POST',
                    'DataType': 'String'
                }
            }
        )
        return response
    except ClientError as e:
        logger.error(e)
        return None