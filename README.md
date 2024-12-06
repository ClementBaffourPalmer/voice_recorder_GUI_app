# Voice Recorder GUI App 🎤

A Python-based graphical user interface (GUI) application that allows users to record and save audio with ease. Built using **Tkinter** for the GUI and other powerful libraries for audio processing, this app is simple, intuitive, and functional.

---

## Features ✨
- 🎙 **Record Audio**: Start and stop audio recording with a click.
- 💾 **Save Recordings**: Save audio recordings in `.wav` format.
- 🕰 **Real-Time Timer**: Displays recording duration in real-time.
- 📂 **File Management**: Allows users to specify filenames and save locations.
- 🔄 **Threading**: Ensures smooth GUI operation during recording.

---

## Requirements 🛠

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Python Libraries
This application uses the following libraries:
- **Tkinter**: For building the graphical user interface (built into Python).
- **sounddevice**: For recording audio.
- **scipy**: For handling `.wav` file formats.
- **numpy**: For numerical operations on audio data.
- **pyaudio**: For additional audio processing and playback.
- **wave**: For manipulating `.wav` files (built into Python).
- **os**: For file and directory handling (built into Python).
- **threading**: For managing background tasks (built into Python).
- **messagebox**: For displaying pop-up messages in the GUI (part of Tkinter).

---

## Platform-Specific Instructions 📋

Depending on your operating system, you may need to install some additional dependencies before proceeding with the project.

### Windows 🖥️
On Windows, you might face issues installing **pyaudio** via `pip`. To install it, follow these steps:
1. Install **Microsoft Visual C++ Build Tools**:
   - Download and install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

2. Install **pyaudio**:
   - You can install **pyaudio** by running:
     ```bash
     pip install pipwin
     pipwin install pyaudio
     ```

### macOS 🍏
On macOS, you may need to install **portaudio** for **pyaudio**. Here's how to do it:
1. Install **Homebrew** (if you don’t have it):
   - Open the terminal and run:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   
2. Install **portaudio**:
   - Run the following to install **portaudio**, which is a dependency for **pyaudio**:
     ```bash
     brew install portaudio
     ```

3. Then install **pyaudio**:
   ```bash
   pip install pyaudio
