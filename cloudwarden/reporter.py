import json
from datetime import datetime

def save_report(findings, fmt='json'):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d_%H-%M')

    if fmt == 'json':
        filename = f'iam_audit_{timestamp}.json'
        with open(filename, 'w') as f:
            json.dump(findings, f, indent=2)
        print(f"[✓] Report saved as {filename}")

    elif fmt == 'md':
        filename = f'iam_audit_{timestamp}.md'
        with open(filename, 'w') as f:
            f.write("# IAM Audit Report\n\n")
            for item in findings:
                f.write(f"- **{item['type']}** for user `{item['user']}`\n")
        print(f"[✓] Report saved as {filename}")

    else:
        print("[!] Unsupported format. Use 'json' or 'md'.")
