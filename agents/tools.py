import os
import webbrowser
import subprocess
import pygetwindow as gw
import time

# List to track windows opened by Jarvis
jarvis_windows = []

def open_notepad():
    os.system("notepad")
    return "Opened Notepad"


def open_chrome():
    webbrowser.open("https://www.google.com")
    return "Opened Chrome"


def create_file(filename="test.txt"):
    with open(filename, "w") as f:
        f.write("Created by Jarvis")
    return f"File {filename} created"


def search_web(query):
    url = f"https://www.google.com/search?q={query.strip()}"
    webbrowser.open(url)
    return f"Searching for {query}"

def open_app_cleanly(app_path, window_title):
    # 1. Close any existing unused windows the agent previously opened
    for win in jarvis_windows:
        if win.isActive == False: # Only close if it's not being used
            win.close()
            jarvis_windows.remove(win)

    # 2. Open a new window
    subprocess.Popen(app_path)
    time.sleep(2) # Give it a moment to render
    
    # 3. Track the new window
    new_win = gw.getWindowsWithTitle(window_title)[0]
    jarvis_windows.append(new_win)
    return f"New {window_title} window opened and tracking."