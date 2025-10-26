import pytest
from click.testing import CliRunner
from unittest.mock import patch, Mock
from src.main import cli
from src.downloader import DownloadError


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


def test_cli_invalid_url():
    """Test CLI with invalid URL."""
    runner = CliRunner()

    result = runner.invoke(cli, ['https://invalid.com/spaces/123'])

    assert result.exit_code == 1
    assert "Invalid URL format" in result.output


def test_cli_download_failure():
    """Test CLI when download fails."""
    runner = CliRunner()

    with patch('src.main.validate_space_url') as mock_validate, \
         patch('src.main.download_space') as mock_download:

        mock_validate.return_value = (True, "1ZkKzZWnVRRKv", None)
        mock_download.side_effect = DownloadError("Video unavailable")

        result = runner.invoke(cli, ['https://x.com/i/spaces/1ZkKzZWnVRRKv'])

        assert result.exit_code == 2
        assert "Video unavailable" in result.output


def test_cli_with_cookies(tmp_path):
    """Test CLI with cookies file."""
    runner = CliRunner()

    # Create a fake cookies file
    cookies_file = tmp_path / "cookies.txt"
    cookies_file.write_text("# Netscape HTTP Cookie File\n")

    with patch('src.main.validate_space_url') as mock_validate, \
         patch('src.main.download_space') as mock_download:

        mock_validate.return_value = (True, "1ZkKzZWnVRRKv", None)
        mock_download.return_value = str(tmp_path / "space_1ZkKzZWnVRRKv.mp3")

        result = runner.invoke(cli, [
            'https://x.com/i/spaces/1ZkKzZWnVRRKv',
            '--cookies', str(cookies_file)
        ])

        assert result.exit_code == 0
        mock_download.assert_called_once()
        # Check that cookies file was passed as third positional argument
        assert mock_download.call_args[0][2] == str(cookies_file)
