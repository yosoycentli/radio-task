import boto3
from boto3.session import Session


sess = Session(region_name='us-west-2')

s3client = sess.client('s3')

bucket_name = 'boto3-files-bucket-radio-task'
s3_location = {
    'LocationConstraint': 'us-west-2'
}

s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
