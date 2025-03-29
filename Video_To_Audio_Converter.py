import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip
from tkinter import ttk

def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv;*.flv")])
    if file_path:
        entry_video_path.delete(0, tk.END)
        entry_video_path.insert(0, file_path)

def convert_to_audio():
    video_path = entry_video_path.get()
    if not video_path:
        messagebox.showerror("Error", "Please select a video file")
        return
    
    try:
        status_label.config(text="Converting... Please wait.")
        root.update_idletasks()
        clip = VideoFileClip(video_path)
        audio_path = os.path.splitext(video_path)[0] + ".mp3"
        clip.audio.write_audiofile(audio_path)
        clip.close()
        status_label.config(text="Conversion Completed!")
        messagebox.showinfo("Success", f"Audio saved as: {audio_path}")
    except Exception as e:
        status_label.config(text="Conversion Failed!")
        messagebox.showerror("Error", f"Failed to convert: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Video to Audio Converter")
root.geometry("450x250")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack(expand=True, fill=tk.BOTH)

ttk.Label(frame, text="Select Video File:").pack(pady=5)
entry_video_path = ttk.Entry(frame, width=50)
entry_video_path.pack(pady=5)

ttk.Button(frame, text="Browse", command=select_video).pack(pady=5)
ttk.Button(frame, text="Convert to Audio", command=convert_to_audio).pack(pady=10)

status_label = ttk.Label(frame, text="", foreground="blue")
status_label.pack(pady=5)

root.mainloop()
