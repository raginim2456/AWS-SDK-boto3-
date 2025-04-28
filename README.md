
1. Install boto3 (if not already installed)

pip install boto3
2. Python Script to List S3 Buckets

import boto3

# Create a session using your AWS credentials
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Check if there are any buckets
if 'Buckets' in response:
    print("List of S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")
else:
    print("No S3 buckets found.")
Explanation:
boto3.client('s3'): This creates a client object to interact with the S3 service.

list_buckets(): This API call fetches the list of buckets in your AWS account.

The script then iterates over the buckets and prints their names.

3. Run the Script
Make sure your AWS credentials are configured (aws configure) before running the script. You can also use an IAM role with the required permissions if you are running this on an EC2 instance.

To run the script, execute it from the command line like this:


python aws_s3_script.py
