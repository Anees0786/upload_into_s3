

import boto3
import os

AWS_ACCESS_KEY = 'AWS ACCESS KEY'
AWS_SECRET_KEY = 'AWS SECRET KEY'
BUCKET_NAME = 'sidimagebucket'

if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
    print("Error: AWS credentials not provided.")
    exit()

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def upload_to_s3(file_path):
    try:
        file_name = os.path.basename(file_path)
        # Upload the file to S3
        with open(file_path, 'rb') as file_data:
            s3.upload_fileobj(file_data, BUCKET_NAME, file_name)
        print(f"File '{file_name}' uploaded successfully to '{BUCKET_NAME}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def main():
    print("Upload a file to Amazon S3")

    file_path = input("Enter the path of the file to upload: ")

    if not os.path.exists(file_path):
        print("Error: File not found.")
        return

    upload_to_s3(file_path)

if __name__ == "__main__":
    main()
