import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Find a female voice (usually index 1 on Windows)
for voice in voices:
    if "Zira" in voice.name or "Female" in voice.name:
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 200) # Friday speaks quickly and efficiently
engine.setProperty('volume', 0.9)

def speak(text):
    print(f"🎙️ F.R.I.D.A.Y.: {text}")
    engine.say(text)
    engine.runAndWait()