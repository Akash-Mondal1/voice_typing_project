import time
import speech_recognition as sr
from pynput.keyboard import Controller

listening = True  # Start listening by default
recognizer = sr.Recognizer()
microphone = sr.Microphone()
keyboard = Controller()
was_speaking = False  # Tracks if user was speaking previously


def type_text(text):
    """Simulates typing the given text at the cursor location."""
    global was_speaking

    # Add a leading space if resuming after a pause
    if was_speaking:
        keyboard.type(" ")  # Insert a space before new speech
    for char in text:
        keyboard.type(char)
    was_speaking = True  # Set speaking status to True


def start_listening(update_status):
    """Start the voice recognition and typing process."""
    global listening, was_speaking

    update_status("Listening...")

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Listening...")
            start_time = time.time()  # Record the start time
            while listening:
                try:
                    audio = recognizer.listen(source, timeout=10)
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    type_text(text)  # Type directly at the cursor
                    start_time = time.time()  # Reset start time after speaking
                except sr.UnknownValueError:
                    print("Sorry, could not understand the audio.")
                except sr.WaitTimeoutError:
                    # Check if 10 seconds of silence have passed
                    if time.time() - start_time >= 10:
                        print("No speech detected for 10 seconds. Exiting...")
                        update_status("Stopped (Inactivity)")
                        listening = False
                        break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        update_status("Stopped")
