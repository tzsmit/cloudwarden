import sys
import os
import boto3
from moto import mock_aws

# Add project root to path so we can import cloudwarden.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cloudwarden.audit import audit_iam

def test_user_without_mfa_detected():
    with mock_aws():
        iam = boto3.client('iam')
        iam.create_user(UserName='testuser')

        findings = audit_iam()

        assert any(
            f['type'] == 'No MFA' and f['user'] == 'testuser'
            for f in findings
        )


