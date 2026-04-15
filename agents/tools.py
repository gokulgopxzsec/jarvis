import os
import webbrowser
import subprocess
import pygetwindow as gw
import time
from datetime import datetime # <-- NEW IMPORT

# Persistent list to track windows opened by the agent
jarvis_windows = []

def get_time():
    """Reads the local system time and formats it for speech."""
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return f"The current time is {current_time}, Sir."

def open_notepad():
    return open_app_cleanly("notepad.exe", "Notepad")

def open_chrome():
    # Chrome is tricky with titles; using a generic browser call or specific executable
    webbrowser.open("https://www.google.com")
    return "Sir, I've opened a new Chrome tab for you."

def create_file(filename="test.txt"):
    with open(filename, "w") as f:
        f.write("Created by F.R.I.D.A.Y. Monitoring system active.")
    return f"File {filename} has been created on your system, Boss."

def search_web(query):
    url = f"https://www.google.com/search?q={query.strip()}"
    webbrowser.open(url)
    return f"Searching the grid for {query}."

def open_app_cleanly(app_path, window_title):
    """Closes unused windows previously opened by the agent and starts a new one."""
    # 1. Cleanup: Close windows the agent opened that are no longer active
    for win in jarvis_windows[:]: # Use a slice to allow removing during iteration
        try:
            if not win.isActive:
                win.close()
                jarvis_windows.remove(win)
        except Exception:
            continue

    # 2. Execution: Open the new window
    subprocess.Popen(app_path)
    time.sleep(2) # Allow time for window to render
    
    # 3. Tracking: Capture the new window handle
    try:
        new_wins = gw.getWindowsWithTitle(window_title)
        if new_wins:
            jarvis_windows.append(new_wins[0])
            return f"New {window_title} window is active and tracking, Sir."
    except Exception:
        pass
    
    return f"I've opened {window_title}, but I'm having trouble tracking the window state."