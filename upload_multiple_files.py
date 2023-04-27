import os
import boto3
from boto3.session import Session
from create_s3_bucket import bucket_name


sess = Session(region_name='us-west-2')

s3client = sess.client('s3')

files_folder_path = 'radio-task/files/'

files_list = os.listdir(files_folder_path)

for file in files_list:
    s3client.upload_file(files_folder_path+file, bucket_name, file)
