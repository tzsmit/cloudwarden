![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![Tests](https://img.shields.io/badge/tests-passing-green.svg)

# ☁️ CloudWarden

**CloudWarden** is a Python-based AWS IAM audit tool that checks for common misconfigurations such as:
- Users without MFA
- Inline user policies
- And more

It outputs results in **JSON** or **Markdown** formats — perfect for reports, CI pipelines, or security reviews.

---

## 👤 Author

**Traivone Smith**  
Cybersecurity + Cloud Enthusiast  
GitHub: [@tzsmit](https://github.com/tzsmit)  
Website: [https://novatitan.net](https://novatitan.net)  
Location: Texas, USA    
Pronouns: He/Him  

---

## 📦 Project Structure

```
cloudwarden/
│
├── cloudwarden/              ← Core IAM audit logic
│   ├── __init__.py
│   ├── audit.py              ← AWS IAM checks
│   ├── reporter.py           ← Markdown/JSON report generation
│   └── utils.py
│
├── scripts/
│   └── run_audit.py          ← CLI runner script
│
├── tests/
│   └── test_audit.py         ← Unit test for audit logic
│
├── requirements.txt
├── README.md
├── LICENSE
└── venv/                     ← Python virtual environment
```

---

## 🚀 Setup Instructions

### 1. Clone and enter the project
```bash
git clone https://github.com/tzsmit/cloudwarden.git
cd cloudwarden
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure AWS credentials

Create a user in AWS IAM with **programmatic access** and proper read-only permissions (or audit role).  
Then run:

```bash
aws configure
```

✅ Do **not** use root credentials.  
Use IAM roles or IAM Identity Center if you're auditing organizations.

---

## 🛠️ Usage

Run the audit from the root directory with:

```bash
python scripts/run_audit.py --format json
```

or

```bash
python scripts/run_audit.py --format md
```

Results will be saved like:

```
iam_audit_2025-07-02_17-21.md
```

---

## 🧪 Running Tests

Run from the root directory:

```bash
pytest
```

This uses `moto` to mock IAM behavior and tests that CloudWarden detects users without MFA.

---

## ✅ Status

- [x] IAM user audit (no MFA, inline policies)
- [x] Markdown & JSON output
- [x] Unit tested with mocked AWS
- [ ] Coming soon: group/role audit, CI/CD GitHub Action

---

## 📄 License

MIT License – free for personal and commercial use.
