import os
import yt_dlp
from typing import Optional


def download_space(
    space_url: str,
    output_dir: str,
    cookies_file: Optional[str] = None
) -> str:
    """
    Downloads X Space recording using yt-dlp.

    Args:
        space_url: URL of the X Space recording
        output_dir: Directory to save the MP3 file
        cookies_file: Optional path to cookies file for authentication

    Returns:
        Path to the downloaded MP3 file
    """
    # Extract space ID from URL for filename
    space_id = space_url.split('/')[-1]

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f'space_{space_id}.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': False,
        'no_warnings': False,
    }

    # Add cookies if provided
    if cookies_file:
        ydl_opts['cookiefile'] = cookies_file

    # Download with yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(space_url, download=True)

    # Return the expected output path
    return os.path.join(output_dir, f'space_{space_id}.mp3')
