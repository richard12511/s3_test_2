import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image
import logging
import datetime

s3_client = boto3.client('s3')
sqs = boto3.resource('sqs')

def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x/2 for x in image.size))
        image.save(resized_path)

def lambda_handler(event, context):
    print(event)
    body = event['Records'][0]['body']
    print(body)

    todays_date = datetime.datetime.today().strftime('%m/%d/%Y')
    bucket_name = 'htri.logs/website.dev/#{todays_date}.txt'
    bucket = s3_client.create_bucket(Bucket=bucket_name)

    uuid = str(uuid.uuid4())
    file_name = '#{uuid}.txt'
    s3_client.put_object(Bucket = bucket_name, Body = body, Key = file_name)


    # bucket = 'ohhailambda'
    # key = 'tommyPuppet.jpg'
    # download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
    # upload_path = '/tmp/resized-{}'.format(key)
    # s3_client.download_file(bucket, key, download_path)
    # resize_image(download_path, upload_path)
    # s3_client.upload_file(upload_path, '{}resized'.format(bucket), key)
