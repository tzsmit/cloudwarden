import sys
import os
import argparse

# Ensure cloudwarden is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cloudwarden.audit import audit_iam
from cloudwarden.reporter import save_report

def main():
    parser = argparse.ArgumentParser(description="Run IAM audit and save report.")
    parser.add_argument('--format', choices=['json', 'md'], default='json', help='Output format (json or md)')
    args = parser.parse_args()

    print("[*] Starting IAM audit...")
    findings = audit_iam()

    if not findings:
        print("[✓] No issues found. IAM setup looks good.")
    else:
        save_report(findings, fmt=args.format)

if __name__ == "__main__":
    main()

