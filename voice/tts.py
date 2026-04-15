import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Select the Female/Zira voice for Friday
for voice in voices:
    if "Zira" in voice.name or "Female" in voice.name:
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 185) # Balanced for clarity and speed
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"🎙️ F.R.I.D.A.Y.: {text}")
    engine.say(text)
    engine.runAndWait()