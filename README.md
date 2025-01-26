
# Voice Typing Project

A Python-based voice typing application with a floating GUI. The application uses `speech_recognition` for voice-to-text conversion and `pynput` for simulating keystrokes.

---

## Features
- Floating GUI window with a minimalistic design.
- Automatically listens to the microphone for speech and types it in the active window.
- Works on Linux and Windows systems.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
  - [For Linux](#for-linux)
  - [For Windows](#for-windows)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [License](#license)

---

## Project Structure
```
voice_typing_project/
├── gui/
│   ├── __init__.py
│   ├── gui.py              # Code for GUI window
├── speech/
│   ├── __init__.py
│   ├── speech_recognition.py # Code for speech recognition and keyboard simulation
├── .env/                   # Virtual environment (generated after installation)
├── requirements.txt        # Python dependencies
├── main.py                 # Entry point for the project
└── README.md               # Project documentation
```

---

## Dependencies

### Python Libraries
- `speech_recognition` - For voice recognition.
- `pynput` - To simulate keyboard input.
- `tkinter` - For the GUI interface (default in Python).
- `pyaudio` - Backend for capturing microphone input.

### System Dependencies
- **Linux**: `portaudio19-dev` for PyAudio support.
- **Windows**: Precompiled PyAudio wheel for your Python version.

---

## Installation

### Prerequisites
1. Ensure Python 3.8 or later is installed.
2. Install `pip` for managing Python packages.

### For Linux

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/voice_typing_project.git
   cd voice_typing_project
   ```

2. Install system-level dependencies:
   ```bash
   sudo apt update
   sudo apt install portaudio19-dev
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv .env
   source .env/bin/activate
   ```

4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### For Windows

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/voice_typing_project.git
   cd voice_typing_project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .env
   .env\Scripts\activate
   ```

3. Install Python dependencies:
   - Install `pyaudio` from a precompiled wheel:
     1. Download the `.whl` file for your Python version from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
     2. Install it:
        ```bash
        pip install path/to/pyaudio‑*.whl
        ```
   - Install other dependencies:
     ```bash
     pip install -r requirements.txt
     ```

---

## How to Run

1. Activate the virtual environment:
   - **Linux**:
     ```bash
     source .env/bin/activate
     ```
   - **Windows**:
     ```bash
     .env\Scripts\activate
     ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

- Once the application starts, the floating window will appear.
- Speak into the microphone, and the text will be typed in the currently active window.
- To stop the application, click the "Close" button in the GUI.

---

## Troubleshooting

1. **PyAudio not found**:
   - Ensure `portaudio19-dev` is installed on Linux.
   - Install a precompiled `pyaudio` wheel on Windows.

2. **Microphone access error**:
   - Check if your microphone is connected and functional.
   - Ensure necessary permissions are granted.

3. **Speech not recognized**:
   - Ensure you are speaking clearly and the microphone is close.

For further assistance, feel free to create an issue on the GitHub repository.

---

## Author

**Akash Mondal**

Feel free to contribute by submitting pull requests or issues!
