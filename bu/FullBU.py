from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog 

def Download_Vid(URL, Path):
    try:
        yt = YouTube(URL)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=Path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error while downloading video: {e}")

def Select_Folder():
    Selected_Folder = filedialog.askdirectory()
    if Selected_Folder:
        print(f"Selected: {Selected_Folder}")
    return Selected_Folder
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    print("Welcome to the Vidownloader!")
    Running = True
    while(Running):
        Video_URL = input("Enter video URL: ")
        Save_To = Select_Folder()
        if Save_To:
            print("Downloading...")
            Download_Vid(Video_URL, Save_To)
        else:
            print("Nah")

# cls && python c:\Projects\Vidownload\Base.py