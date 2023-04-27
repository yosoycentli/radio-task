import boto3
from boto3.session import Session


sess = Session(region_name='us-west-2')

s3client = sess.client('s3')

bucket_name = 'boto3-files-bucket-radio-task'

upload_file = s3client.upload_file('radio-task/files/podcast.mp3', bucket_name, 'podcast.mp3')
