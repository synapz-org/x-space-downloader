import pytest
from unittest.mock import Mock, patch
from src.downloader import download_space


def test_download_space_basic(tmp_path):
    """Test basic download functionality."""
    space_url = "https://x.com/i/spaces/1ZkKzZWnVRRKv"

    with patch('src.downloader.yt_dlp.YoutubeDL') as mock_ytdl_class:
        # Mock the YoutubeDL instance
        mock_ytdl = Mock()
        mock_ytdl_class.return_value.__enter__.return_value = mock_ytdl
        mock_ytdl.extract_info.return_value = {'id': '1ZkKzZWnVRRKv'}

        # Call download_space
        result = download_space(
            space_url=space_url,
            output_dir=str(tmp_path),
            cookies_file=None
        )

        # Verify YoutubeDL was called
        mock_ytdl.extract_info.assert_called_once_with(space_url, download=True)

        # Verify result contains expected filename
        assert "space_1ZkKzZWnVRRKv" in result
