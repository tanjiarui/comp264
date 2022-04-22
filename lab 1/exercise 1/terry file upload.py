import boto3, logging, datetime

# Set up our logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

AWS_SERVER_PUBLIC_KEY = 'AKIAVPRXNHVE3Z7UU3AQ'
AWS_SERVER_SECRET_KEY = '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'

client = boto3.client('s3', aws_access_key_id=AWS_SERVER_PUBLIC_KEY, aws_secret_access_key=AWS_SERVER_SECRET_KEY)

logging.info('start time {}'.format(datetime.datetime.now()))
for file_name in ['test_text1.txt', 'test_text2.txt', 'test_text3.txt']:
    try:
        logging.info('start to upload %s' % file_name)
        response = client.upload_file(file_name, 's3-bucket-terry', file_name)
    except client.exceptions.ClientError as e:
        logging.error(e)
logging.info('end time {}'.format(datetime.datetime.now()))