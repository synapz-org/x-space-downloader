import pytest
from src.validator import validate_space_url


def test_validate_space_url_valid():
    """Test that valid X Space URL is accepted."""
    url = "https://x.com/i/spaces/1ZkKzZWnVRRKv"
    is_valid, space_id, error = validate_space_url(url)

    assert is_valid is True
    assert space_id == "1ZkKzZWnVRRKv"
    assert error is None
