import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
from scipy.io.wavfile import write
import wave
import numpy as np
import pyaudio
import threading
import os

# Global variables
is_recording = False
audio_frames = []
record_duration = 0
current_file = "recording.wav"
timer_thread = None

# Record Audio Functions
def start_recording():
    global is_recording, audio_frames, record_duration, timer_thread
    is_recording = True
    audio_frames = []
    record_duration = 0
    duration_label.config(text="Recording... 0 seconds")
    microphone_label.config(text="🎤 Recording...")
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.start()
    threading.Thread(target=record_audio).start()
    start_button.config(state="disabled")
    stop_button.config(state="normal")

def stop_recording():
    global is_recording
    is_recording = False
    microphone_label.config(text="Recording stopped.")
    duration_label.config(text=f"Recording stopped. Duration: {record_duration} seconds.")
    messagebox.showinfo("Voice Recorder", f"Recording saved as {current_file}")
    save_recording()
    file_display.config(state="normal")
    file_display.delete(0, tk.END)
    file_display.insert(0, current_file)
    file_display.config(state="readonly")
    start_button.config(state="normal")
    stop_button.config(state="disabled")

def record_audio():
    global audio_frames
    freq = 44100
    audio_frames = []
    def callback(indata, frames, time, status):
        audio_frames.extend(indata.copy())
    with sd.InputStream(samplerate=freq, channels=1, callback=callback):
        while is_recording:
            sd.sleep(100)

def save_recording():
    freq = 44100
    audio_np = np.array(audio_frames, dtype=np.float32)
    audio_scaled = np.int16(audio_np * 32767)  # Scale float data to 16-bit PCM
    write(current_file, freq, audio_scaled)
   
def update_timer():
    global record_duration
    while is_recording:
        record_duration += 1
        duration_label.config(text=f"Recording... {record_duration} seconds")
        root.update_idletasks()
        root.after(1000)

# Playback Function
def play_recording():
    if os.path.exists(current_file):
        wf = wave.open(current_file, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)
        stream.stop()
        p.terminate()
    else:
        messagebox.showerror("Error", "No file to play.")

# Delete Recording Function
def delete_recording():
    if os.path.exists(current_file):
        os.remove(current_file)
        file_display.config(state="normal")
        file_display.delete(0, tk.END)
        file_display.config(state="readonly")
        messagebox.showinfo("Voice Recorder", "Recording deleted successfully.")
    else:
        messagebox.showerror("Error", "No file to delete.")

# Hover effects
def on_enter(button, text_color, bg_color):
    button.config(fg=text_color, bg=bg_color)

def on_leave(button, text_color, bg_color):
    button.config(fg=text_color, bg=bg_color)

# GUI Setup
root = tk.Tk()
root.title("Voice Recorder")
root.geometry("400x400")
root.config(bg="#f7f7f7")

# Controls Frame
controls_frame = tk.Frame(root, bg="#f7f7f7")
controls_frame.pack(pady=10)
# Start Button
start_button = tk.Button(
    controls_frame, text="Start Recording", bg="#D4E157", fg="black",
    font=("Arial", 12), command=start_recording, width=20
)
start_button.grid(row=0, column=0, padx=10)
start_button.bind("<Enter>", lambda event: on_enter(start_button, "Green", "#4CAF50"))
start_button.bind("<Leave>", lambda event: on_leave(start_button, "black", "#D4E157"))

# Stop Button
stop_button = tk.Button(
    controls_frame, text="Stop Recording", bg="#FF7043", fg="black",
    font=("Arial", 12), command=stop_recording, state="disabled", width=20
)
stop_button.grid(row=0, column=1, padx=10)
stop_button.bind("<Enter>", lambda event: on_enter(stop_button, "black", "#FF5733"))  # Lighter Red-Orange
stop_button.bind("<Leave>", lambda event: on_leave(stop_button, "black", "#FF7043"))  # Original red

# Play Button
play_button = tk.Button(
    root, text="Play Recording", bg="#1E88E5", fg="white",
    font=("Arial", 12), command=play_recording, width=20
)
play_button.pack(pady=5)

# Delete Button
delete_button = tk.Button(
    root, text="Delete Recording", bg="#D32F2F", fg="white",
    font=("Arial", 12), command=delete_recording, width=20
)
delete_button.pack(pady=5)
delete_button.bind("<Enter>", lambda event: on_enter(delete_button, "white", "#B71C1C"))  # Darker red hover
delete_button.bind("<Leave>", lambda event: on_leave(delete_button, "white", "#D32F2F"))  # Original red

# Microphone Label
microphone_label = tk.Label(root, text="🎤", font=("Arial", 24), bg="#f7f7f7")
microphone_label.pack(pady=10)

# Duration Label
duration_label = tk.Label(root, text="Press 'Start' to begin recording.", font=("Arial", 12), bg="#f7f7f7")
duration_label.pack(pady=5)

# File Display
file_display = tk.Entry(root, font=("Arial", 12), state="readonly", justify="center")
file_display.pack(pady=5, fill="x", padx=35)

# Run the GUI
root.mainloop()
