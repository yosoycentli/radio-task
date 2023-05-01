import boto3

from fastapi import FastAPI

app = FastAPI()

client=boto3.resource('s3')
bucket_name = 'boto3-files-bucket-radio-task'


@app.get("/")
def home():
    return {"Radio": "Station"}

@app.get("/audio")
def audio_files():
    bucket=client.Bucket(bucket_name)
    files = bucket.objects.all()
    file_list = []

    for file in files:
        if file.key.endswith('.wav') or file.key.endswith('.mp3') or file.key.endswith('.flac'): 
            file_list.append(file.key)
    return(file_list)

@app.get("/video")
def audio_files():
    bucket=client.Bucket(bucket_name)
    files = bucket.objects.all()
    file_list = []

    for file in files:
        if file.key.endswith('.mp4') or file.key.endswith('.avi') or file.key.endswith('.mov'): 
            file_list.append(file.key)
    return(file_list)


@app.get("/documents")
def audio_files():
    bucket=client.Bucket(bucket_name)
    files = bucket.objects.all()
    file_list = []

    for file in files:
        if file.key.endswith('.png') or file.key.endswith('.jpg') or file.key.endswith('.gif') or file.key.endswith('.jpeg'): 
            file_list.append(file.key)
    return(file_list)
