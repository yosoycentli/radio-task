import boto3
import socket

from fastapi import FastAPI

app = FastAPI()

client=boto3.resource('s3')
bucket_name = 'boto3-files-bucket-radio-task'

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


@app.get("/")
def documents_files():
    bucket=client.Bucket(bucket_name)
    files = bucket.objects.all()
    file_list = []

    for file in files:
        if file.key.endswith('.png') or file.key.endswith('.jpg') or file.key.endswith('.gif') or file.key.endswith('.jpeg'):
            file_list.append(file.key)
    total=len(file_list)
    total_statement = "Files: " + str(total) + " images"
    ip_total_statement = "IP: " + get_ip_address()
    return f'{ip_total_statement} {total_statement}'

