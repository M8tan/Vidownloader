from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog 

def Download_Vid(URL, Path):
    try:
        yt = YouTube(URL, client='WEB')
        print(yt.streams)
        ys = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        if ys is None:
            print("Could not find a suitable stream")
            return
        ys.download(output_path=Path)
        print(f"Video {yt.title} downloaded successfully!")
    except Exception as e:
        print(f"Error while downloading video: {e}")

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
            Download_Vid(Video_URL, Save_To)
        else:
            print("No output path selected")

