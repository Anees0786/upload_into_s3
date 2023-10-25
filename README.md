# upload_into_s3
# Upload to S3 Script

This Python script allows users to upload a file to an Amazon S3 bucket.

## Prerequisites

1. Install the `boto3` library:

    ```bash
    pip install boto3
    ```

2. Replace the placeholders `'AWS ACCESS KEY'`, `'AWS SECRET KEY'`, and `'sidimagebucket'` with your actual AWS credentials and S3 bucket name.

## Usage

1. Save the script as `upload_to_s3.py`.

2. Run the script:

    ```bash
    python upload_to_s3.py
    ```

3. Enter the path of the file to upload when prompted.

4. Ensure that the AWS credentials have the necessary permissions to upload to the specified S3 bucket.

**Note:** It is crucial to handle AWS credentials securely. In a production environment, consider using AWS IAM roles, AWS credentials file, or environment variables.
