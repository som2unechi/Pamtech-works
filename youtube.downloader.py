from pytube import Playlist, YouTube
import os

# Playlist URL
playlist_url = "https://youtu.be/dUpyC40cF6Q?si=FFfiktsp_UPSqkTT"

# Download directory
download_directory = "C:\\Users\\user\\Desktop\\videio"

# Ensure the download directory exists
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Function to download a video
def download_video(video_url, path):
    try:
        yt = YouTube(video_url)
        print(f'Downloading: {yt.title}')
        yt.streams.filter(type='video', progressive=True, file_extension='mp4') \
            .order_by('resolution') \
            .desc() \
            .first() \
            .download(path)
        print(f'Successfully downloaded: {yt.title}')
    except Exception as e:
        print(f'Error downloading {video_url}: {e}')

# Main script to download playlist
def download_playlist(playlist_url, download_directory):
    try:
        playlist = Playlist(playlist_url)
        print(f"Total videos to download: {len(playlist.video_urls)}\n")

        for video_url in playlist.video_urls:
            print(f'Video URL: {video_url}')
            download_video(video_url, download_directory)

    except Exception as e:
        print(f'Error processing playlist: {e}')

# Run the script
download_playlist(playlist_url, download_directory)
