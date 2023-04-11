import os
from pytube import YouTube

# Prompt user for YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Define the download directory
download_dir = r'C:/Downloads'

# Create a YouTube object and get the available streams
yt = YouTube(video_url)
stream = yt.streams

# Ask user if they want a audio or video file
file_type = input("Do you want to download a video or audio file? Enter 'v' for video or 'a' for audio: ")

# Choose the appropriate stream based on the user's choice
if file_type == 'v':
    stream = stream.get_highest_resolution()
else:
    stream = stream.get_audio_only()

# Check if the download directory exists, create it if it doesn't
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Download the video and save to the download directory
try:
    video_title = yt.title
    print(f"Downloading '{video_title}'...")
    stream.download(download_dir)
    print("Video downloaded successfully!")
except Exception as e:
    print("Error:", str(e))