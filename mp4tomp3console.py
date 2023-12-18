import pytube
import moviepy.editor as mp
import os
import time

url = input("Посилання на відео з ютубу: ")
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()

download_path = "path to save files"
video.download(output_path=download_path, filename="temp_video.mp4")

video_path = os.path.join(download_path, "temp_video.mp4")
while not os.path.exists(video_path):
    time.sleep(1)

video_clip = mp.VideoFileClip(video_path)
output_path = os.path.join(download_path, "output_audio.mp3")
video_clip.audio.write_audiofile(output_path)

print("---end---")
