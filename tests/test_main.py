import pytest
from click.testing import CliRunner
from unittest.mock import patch, Mock
from src.main import cli


def test_cli_valid_url(tmp_path):
    """Test CLI with valid URL."""
    runner = CliRunner()

    with patch('src.main.validate_space_url') as mock_validate, \
         patch('src.main.download_space') as mock_download:

        mock_validate.return_value = (True, "1ZkKzZWnVRRKv", None)
        mock_download.return_value = str(tmp_path / "space_1ZkKzZWnVRRKv.mp3")

        result = runner.invoke(cli, ['https://x.com/i/spaces/1ZkKzZWnVRRKv'])

        assert result.exit_code == 0
        assert "Successfully downloaded" in result.output
        assert "space_1ZkKzZWnVRRKv.mp3" in result.output
