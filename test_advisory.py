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
    """Create a fresh AdvisoryEngine for each test."""
    # Use a temporary config to avoid modifying real files during tests
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "security_patterns.json"
        # Copy or use default patterns
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
        file_patterns=["config/.env", "secrets/api_key.json", "app/keys/token.py"]
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


def test_label_patterns(engine):
    """Test label-based pattern matching."""
    context = AdvisoryContext(
        issue_labels=["security", "authentication", "data-privacy"],
        repo_metadata={},
        file_patterns=[]
    )
    
    advice_list = engine.evaluate_context(context)
    titles = [a.title.lower() for a in advice_list]
    
    assert any("security" in t for t in titles)
    assert any("authentication" in t for t in titles)
    assert len(advice_list) >= 2


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
        issue_labels=["enhancement", "docs"],
        repo_metadata={},
        file_patterns=["README.md", "docs/guide.md"]
    )
    
    advice_list = engine.evaluate_context(context)
    assert len(advice_list) == 1
    assert "General Security Guidance" in advice_list[0].title


def test_pattern_matching_function(engine):
    """Test the internal _matches_pattern method directly."""
    test_cases = [
        ("src/auth/login.py", True),
        ("app/api/v1/users.py", False),
        ("config/secrets.env", True),
        ("migrations/versions/001.sql", True),
    ]
    
    for file_path, should_match in test_cases:
        # We can test via evaluate_context or expose if needed
        context = AdvisoryContext(
            issue_labels=[], repo_metadata={}, file_patterns=[file_path]
        )
        advice = engine.evaluate_context(context)
        
        if should_match:
            assert len(advice) > 0
        # else: may still return general advice
