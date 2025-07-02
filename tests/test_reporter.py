import os
import sys
import json
from datetime import datetime
import pytest

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cloudwarden.reporter import save_report

@pytest.fixture
def findings():
    return [
        {'type': 'No MFA', 'user': 'alice'},
        {'type': 'Inline Policy', 'user': 'bob'}
    ]

def test_save_report_json(findings, tmp_path):
    output_path = tmp_path / "output.json"
    save_report(findings, output_format="json", filename=output_path)

    assert output_path.exists()

    with open(output_path) as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert data == findings

def test_save_report_md(findings, tmp_path):
    output_path = tmp_path / "output.md"
    save_report(findings, output_format="md", filename=output_path)

    assert output_path.exists()

    with open(output_path) as f:
        content = f.read()
        assert "# IAM Audit Report" in content
        assert "**No MFA** for user `alice`" in content
        assert "**Inline Policy** for user `bob`" in content