import pytube
import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import AudioFileClip

def convert_audio():
    url = url_entry.get()
    file_name = file_name_entry.get()  # Отримуємо введене ім'я для файлу

    if url and file_name:  # Перевірка на введення всіх необхідних даних
        try:
            youtube = pytube.YouTube(url)
            audio_stream = youtube.streams.filter(only_audio=True).first()
            
            download_path = filedialog.askdirectory()  
            if download_path:  
                audio_path = os.path.join(download_path, f"{file_name}.mp3")
                audio_stream.download(output_path=download_path, filename=f"{file_name}_temp.mp3")
                
                os.rename(os.path.join(download_path, f"{file_name}_temp.mp3"), audio_path)
                
                result_label.config(text="Done!")
            else:
                result_label.config(text="Please select a folder.")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="Please fill in all fields.")

root = tk.Tk()
root.title("YouTube Audio to MP3 Converter")

url_label = tk.Label(root, text="Paste video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

file_name_label = tk.Label(root, text="Enter file name:")
file_name_label.pack()

file_name_entry = tk.Entry(root, width=50)
file_name_entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert_audio)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
