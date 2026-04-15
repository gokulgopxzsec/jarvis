import os
import webbrowser


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