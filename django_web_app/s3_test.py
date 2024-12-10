# s3_test.py
import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_s3_connection():
    try:
        # Retrieve credentials from environment variables
        print(os.getenv('AWS_SECRET_ACCESS_KEY'))
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('REGION_NAME')
        )
        
        # List buckets to verify connection
        response = s3.list_buckets()
        print("Successful S3 Connection")
        print("Buckets:", [bucket['Name'] for bucket in response['Buckets']])
        
        # Attempt to list objects in the specific bucket
        bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
        objects = s3.list_objects_v2(Bucket=bucket_name)
        print(f"\nObjects in bucket {bucket_name}:")
        for obj in objects.get('Contents', []):
            print(obj['Key'])
        
    except Exception as e:
        print(f"S3 Connection Error: {e}")

if __name__ == '__main__':
    test_s3_connection()