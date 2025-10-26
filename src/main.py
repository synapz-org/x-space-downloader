import click
import os
from src.validator import validate_space_url
from src.downloader import download_space, DownloadError


@click.command()
@click.argument('url')
@click.option('--cookies', '-c', type=click.Path(exists=True), help='Path to cookies file')
@click.option('--output', '-o', type=click.Path(), default='.', help='Output directory')
def cli(url, cookies, output):
    """
    Download X (Twitter) Space recordings as MP3 files.

    Example:
        x-space-dl https://x.com/i/spaces/1ZkKzZWnVRRKv
    """
    # Validate URL
    is_valid, space_id, error = validate_space_url(url)
    if not is_valid:
        click.echo(f"Error: {error}", err=True)
        raise click.Exit(1)

    # Download the Space
    try:
        click.echo(f"Downloading Space: {space_id}")
        output_path = download_space(url, output, cookies)
        click.echo(f"Successfully downloaded to: {output_path}")
    except DownloadError as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Exit(2)


if __name__ == '__main__':
    cli()
