from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog 
from dataclasses import dataclass

@dataclass
class VideoResponse:
    video: YouTube | None = None
    error: Exception | None = None


def Download_VidTemp(URL, Path):
    try:
        yt = YouTube(URL, client='WEB')
        videostream = (yt.streams.filter(only_video=True, file_extension="mp4").get_highest_resolution())
        audiostream = (yt.streams.filter(only_audio=True, file_extension="mp4").first())
        if videostream is None:
            return VideoResponse(error=Exception("Could not find a suitable video stream"))
        if audiostream is None:
            return VideoResponse(error=Exception("Could not find a suitable audio stream"))
        videostream.download(output_path=Path)
        audiostream.download(output_path=Path)
        return VideoResponse(video=yt)
    except Exception as e:
        return VideoResponse(error=e)

def Download_Vid(URL, Path):
    try:
        yt = YouTube(URL, client="WEB")

        print("All streams:")
        print(yt.streams)

        print("\nVideo streams:")
        video_streams = yt.streams.filter(only_video=True)
        print(video_streams)

        print("\nMP4 video streams:")
        mp4_video_streams = yt.streams.filter(
            only_video=True,
            file_extension="mp4"
        )
        print(mp4_video_streams)

        return VideoResponse(video=yt)

    except Exception as e:
        return VideoResponse(error=e)


def Select_Folder():
    Selected_Folder = filedialog.askdirectory()
    if Selected_Folder:
        return Selected_Folder
    return None

if __name__ == "__main__":
    print("Welcome to the Vidownloader!!")
    root = tk.Tk()
    root.withdraw()
    Running = True
    while(Running):
        Video_URL = input("Enter video URL: ")
        if Video_URL.lower() in ("q", "e", "quit", "exit"):
            print("Ok, exiting :)")
            Running = False
            break
        Save_To = Select_Folder()
        if Save_To:
            print(f"Downloading to {Save_To}...")
            response = Download_Vid(Video_URL, Save_To)
            if response.error:
                print(f"Error downloading video: {response.error}")
            else:
                print(f"Succesfully downloaded {response.video.title}")
        else:
            print("No output path selected")

# Fix note: it started working after running python -m pip install --upgrade pip && python -m pip install -U pytubefix inside venv
