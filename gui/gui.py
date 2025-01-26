import tkinter as tk
from threading import Thread
from speech.speech_recognition import start_listening

status_label = None  # Global status label to be shared across functions


def update_status(status):
    """Update the status in the GUI."""
    status_label.config(text=f"Status: {status}")


def create_gui():
    """Create a simple floating GUI."""
    root = tk.Tk()
    root.title("Voice Typing")

    # Make the window float and always stay on top
    root.overrideredirect(True)  # Remove window borders
    root.attributes('-topmost', True)  # Keep the window on top

    # Make the window draggable
    def start_move(event):
        root.x = event.x
        root.y = event.y

    def do_move(event):
        x = root.winfo_x() + (event.x - root.x)
        y = root.winfo_y() + (event.y - root.y)
        root.geometry(f"+{x}+{y}")

    root.bind("<Button-1>", start_move)
    root.bind("<B1-Motion>", do_move)

    # Create the status label
    global status_label
    status_label = tk.Label(root, text="Status: Listening...", font=("Arial", 14))
    status_label.pack(pady=10, padx=20)

    # Create the exit button
    exit_button = tk.Button(
        root, text="Close", font=("Arial", 12), command=lambda: root.destroy()
    )
    exit_button.pack(pady=10)

    # Start the listening thread
    Thread(target=start_listening, args=(update_status,), daemon=True).start()

    root.mainloop()
