import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

def count_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name)

    object_count = 0
    for page in pages:
        if 'Contents' in page:
            object_count += len(page['Contents'])
    print(f"\nTotal number of objects in bucket '{bucket_name}': {object_count}")

if __name__ == "__main__":
    list_s3_buckets()
    bucket_name = input("\nEnter the S3 bucket name to count objects: ").strip()
    count_objects_in_bucket(bucket_name)

