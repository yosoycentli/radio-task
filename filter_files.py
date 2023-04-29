import boto3

bucket_name = 'boto3-files-bucket-radio-task'

client=boto3.resource('s3')
bucket=client.Bucket(bucket_name)

files = bucket.objects.all()
file_list = []

for file in files:
  if file.key.endswith('.png') or file.key.endswith('.jpg') or file.key.endswith('.gif') or file.key.endswith('.jpeg'): 
    file_list.append(file.key)

print(file_list)
