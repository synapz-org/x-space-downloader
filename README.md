# X Space Downloader

A Python CLI tool that downloads X (Twitter) Space recordings and outputs them as MP3 files.

## Features

- Download X Space recordings as MP3 files
- Support for authenticated downloads using cookies
- Simple command-line interface
- Clear error messages

## Installation

### Prerequisites

- Python 3.8 or higher
- ffmpeg (required by yt-dlp for audio conversion)

Install ffmpeg:
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Install the tool

```bash
git clone https://github.com/synapz-org/x-space-downloader.git
cd x-space-downloader
pip install -e .
```

## Usage

### Basic usage

```bash
x-space-dl https://x.com/i/spaces/1ZkKzZWnVRRKv
```

This will download the Space recording and save it as `space_1ZkKzZWnVRRKv.mp3` in the current directory.

### With authentication (recommended)

For better reliability and access to private Spaces, provide cookies from your logged-in X session:

```bash
x-space-dl --cookies cookies.txt https://x.com/i/spaces/1ZkKzZWnVRRKv
```

### Specify output directory

```bash
x-space-dl --output ~/Downloads https://x.com/i/spaces/1ZkKzZWnVRRKv
```

### Full options

```bash
x-space-dl --help
```

## Exporting Cookies

To download Spaces that require authentication, you need to export cookies from your logged-in X session.

### Method 1: Browser Extension (Easiest)

1. Install a cookie export extension:
   - Chrome/Edge: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - Firefox: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

2. Log in to X (twitter.com or x.com)
3. Click the extension icon and export cookies
4. Save as `cookies.txt`

### Method 2: Manual Export (Advanced)

1. Log in to X
2. Open Developer Tools (F12)
3. Go to Application/Storage → Cookies
4. Copy cookies in Netscape format to a file

## Requirements

- Python 3.8+
- yt-dlp
- click
- ffmpeg (system dependency)

## Supported URLs

The tool supports X Space URLs in these formats:

- `https://x.com/i/spaces/{SPACE_ID}`
- `https://twitter.com/i/spaces/{SPACE_ID}`

**Note:** Only recordings are supported. Live Spaces must be recorded before downloading.

## Error Messages

| Error | Meaning |
|-------|---------|
| "Invalid URL format" | URL doesn't match X Space format |
| "Failed to download Space" | Recording not found or network error |
| "Authentication required" | Space requires login (use --cookies) |

## Development

### Running tests

```bash
pip install pytest pytest-mock
pytest
```

### Project structure

```
x-space-downloader/
├── src/
│   ├── main.py          # CLI entry point
│   ├── downloader.py    # yt-dlp wrapper
│   └── validator.py     # URL validation
├── tests/
│   ├── test_main.py
│   ├── test_downloader.py
│   └── test_validator.py
└── docs/
    └── plans/           # Design documents
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Troubleshooting

### "ffmpeg not found"
Install ffmpeg using your system's package manager (see Installation section).

### "Video unavailable"
The Space recording may have been deleted or is private. Try using the --cookies option.

### "Authentication required"
Export cookies from your logged-in X session and use the --cookies option.

## Acknowledgments

Built with:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Media downloader
- [Click](https://click.palletsprojects.com/) - CLI framework
