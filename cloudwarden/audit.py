import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Connect to AWS IAM using credentials from .env
iam = boto3.client(
    'iam',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

def audit_iam():
    findings = []

    try:
        users = iam.list_users()['Users']

        for user in users:
            username = user['UserName']

            # ✅ Check MFA
            mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
            if not mfa_devices:
                findings.append({
                    'type': 'No MFA',
                    'user': username
                })

            # ✅ Check inline policies
            inline_policies = iam.list_user_policies(UserName=username)['PolicyNames']
            if inline_policies:
                findings.append({
                    'type': 'Inline Policy',
                    'user': username,
                    'policies': inline_policies
                })

    except Exception as e:
        findings.append({
            'type': 'Error',
            'message': str(e)
        })

    return findings
