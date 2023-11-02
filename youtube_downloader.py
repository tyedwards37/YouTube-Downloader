# @file youtube_downloader.py
# @brief - This will prompt the user for a URL then download that video as either an MP3, MP4, or both, depending on the user's specifications.
# @author Tyler Edwards - tk.edwards2003@gmail.com

import os
import subprocess
from pytube import YouTube

parent_dir = r"YoutubeDownloads"

try:
    url = input("Please put the YouTube URL here: ")
    # url = "[URL]"
    video = YouTube(url)
    video_title = video.title
except Exception as e:
    print("Invalid URL or an error occurred:", e)
    exit(1)


fileType = input("File type: MP3, MP4, or Both\n").lower()

if (fileType == "mp3"):
    fileName = input("Enter filename: ") + ".mp3"
    
    try:
        video.streams.filter(only_audio=True).first().download(output_path=parent_dir)
        input_file = os.path.join(parent_dir, video_title + ".mp4")
        output_file = os.path.join(parent_dir, fileName)
        subprocess.run(['ffmpeg', '-i', input_file, output_file])

        os.remove(input_file)
    except Exception as e:
        print("Conversion to MP3 failed:", e)
        exit(1)
    
elif (fileType == "mp4"):
    video.title = input("Enter filename: ") 
    try:
        video = video.streams.get_highest_resolution().download(output_path=parent_dir)
    except Exception as e:
        print("Download of YouTube video failed:", e)
        exit(1)

elif (fileType == "both"):
    fileName = input("Enter filename: ") 
    videoFileName = fileName + ".mp4"
    audioFileName = fileName + ".mp3"
    try:
        video = video.streams.get_highest_resolution().download(output_path=parent_dir)
        input_file = os.path.join(parent_dir, video_title + ".mp4")
        output_file = os.path.join(parent_dir, videoFileName)
        os.rename(input_file, output_file)
        subprocess.run(['ffmpeg', '-i', output_file, os.path.join(parent_dir, audioFileName)])
    except Exception as e:
        print("One of the downloads failed:", e)
        exit(1)




else:
    fileType = input("Please enter a valid file type: MP3 or MP4.")



