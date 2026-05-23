import pytest
import os
import sys
import tempfile
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from advisory_engine.core import AdvisoryEngine, AdvisoryContext


@pytest.fixture
def engine():
    """Create a fresh AdvisoryEngine for each test using default patterns."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "security_patterns.json"
        # Engine will fall back to defaults if file doesn't exist
        engine = AdvisoryEngine(config_path=str(config_path))
        yield engine


def test_file_patterns_authentication(engine):
    """Test authentication related file patterns."""
    context = AdvisoryContext(
        issue_labels=[],
        repo_metadata={},
        file_patterns=["src/auth/login.py", "app/services/user_auth.py", "backend/session.py"]
    )

    advice_list = engine.evaluate_context(context)

    assert len(advice_list) >= 1
    assert any("authentication" in a.title.lower() for a in advice_list)
    assert any(a.severity == "critical" for a in advice_list)


def test_file_patterns_secrets(engine):
    """Test detection of potential secret/API key files."""
    context = AdvisoryContext(
        issue_labels=[],
        repo_metadata={},
        file_patterns=["config/.env", ".env", "secrets/api_key.json", "app/keys/token.py"]
    )

    advice_list = engine.evaluate_context(context)
    assert any("api_keys" in a.title.lower() for a in advice_list)
    assert any(a.severity == "critical" for a in advice_list)


def test_file_patterns_database(engine):
    """Test database related patterns."""
    context = AdvisoryContext(
        issue_labels=[],
        repo_metadata={},
        file_patterns=["models/user.py", "migrations/001_add_users.sql", "db/schema.sql"]
    )

    advice_list = engine.evaluate_context(context)
    assert any("database" in a.title.lower() for a in advice_list)
    assert any(a.severity == "high" for a in advice_list)


def test_file_patterns_encryption(engine):
    """Test encryption/crypto related patterns."""
    context = AdvisoryContext(
        issue_labels=[],
        repo_metadata={},
        file_patterns=["utils/crypto.py", "services/encrypt_data.py", "ssl/cert.pem"]
    )

    advice_list = engine.evaluate_context(context)
    assert any("encryption" in a.title.lower() for a in advice_list)
    assert any(a.severity == "critical" for a in advice_list)


def test_file_patterns_file_upload(engine):
    """Test file upload related patterns."""
    context = AdvisoryContext(
        issue_labels=[],
        repo_metadata={},
        file_patterns=["uploads/image.py", "storage/file_handler.py", "media/upload.py"]
    )

    advice_list = engine.evaluate_context(context)
    assert any("file_upload" in a.title.lower() for a in advice_list)
    assert any(a.severity == "high" for a in advice_list)


def test_file_patterns_api_endpoints(engine):
    """Test API endpoints patterns."""
    context = AdvisoryContext(
        issue_labels=[],
        repo_metadata={},
        file_patterns=["api/v1/users.py", "routes/auth.py", "controllers/payment.py"]
    )

    advice_list = engine.evaluate_context(context)
    assert any("api_endpoints" in a.title.lower() for a in advice_list)
    assert any(a.severity == "high" for a in advice_list)


def test_label_patterns(engine):
    """Test label-based pattern matching."""
    context = AdvisoryContext(
        issue_labels=["security", "authentication", "data-privacy", "vulnerability"],
        repo_metadata={},
        file_patterns=[]
    )

    advice_list = engine.evaluate_context(context)
    titles = [a.title.lower() for a in advice_list]

    assert any("security" in t for t in titles)
    assert any("authentication" in t for t in titles)
    assert len(advice_list) >= 3


def test_combined_file_and_label(engine):
    """Test when both files and labels trigger patterns."""
    context = AdvisoryContext(
        issue_labels=["api"],
        repo_metadata={},
        file_patterns=["src/auth/login.py"]
    )

    advice_list = engine.evaluate_context(context)
    assert len(advice_list) >= 2


def test_no_patterns_triggered(engine):
    """Test fallback to general advice when no patterns match."""
    context = AdvisoryContext(
        issue_labels=["enhancement", "docs", "refactor"],
        repo_metadata={},
        file_patterns=["README.md", "docs/guide.md", "utils/helper.py"]
    )

    advice_list = engine.evaluate_context(context)
    assert len(advice_list) == 1
    assert "General Security Guidance" in advice_list[0].title


def test_pattern_matching_function(engine):
    """Test the internal _matches_pattern method with globstar support."""
    test_cases = [
        ("src/auth/login.py", True),           # Should match authentication
        ("config/.env", True),                 # Should match api_keys
        ("migrations/001.sql", True),          # Should match database
        ("api/v1/users.py", True),             # Should match api_endpoints
        ("uploads/profile.jpg", True),         # Should match file_upload
        ("random/file.txt", False),            # Should NOT match any specific pattern
        ("docs/README.md", False),
    ]

    for file_path, should_match_specific in test_cases:
        context = AdvisoryContext(
            issue_labels=[], 
            repo_metadata={}, 
            file_patterns=[file_path]
        )
        advice_list = engine.evaluate_context(context)

        if should_match_specific:
            assert len(advice_list) > 1 or any(
                cat in a.title.lower() 
                for a in advice_list 
                for cat in ["auth", "api", "database", "upload", "encrypt"]
            )
        else:
            # Should only return general advice
            assert len(advice_list) == 1
            assert "General Security Guidance" in advice_list[0].title


def test_generate_report(engine):
    """Test report generation with multiple severity levels."""
    context = AdvisoryContext(
        issue_labels=["security", "authentication"],
        repo_metadata={},
        file_patterns=[".env", "api/login.py"]
    )

    advice_list = engine.evaluate_context(context)
    report = engine.generate_report(advice_list)

    assert "# 🛡️ BLT Preflight Security Advisory" in report
    assert "Critical Security Considerations" in report
    assert "authentication" in report.lower()
    assert "api_keys" in report.lower()
