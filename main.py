from utils.audio import record_audio
from voice.stt import speech_to_text
from voice.tts import speak
from agents.agent import decide_and_act


def run_jarvis():
    speak("Jarvis is online")

    while True:
        try:
            audio_path = record_audio()
            text = speech_to_text(audio_path)

            if not text:
                continue

            if "exit" in text.lower() or "stop" in text.lower():
                speak("Shutting down")
                break

            response = decide_and_act(text)
            speak(response)

        except KeyboardInterrupt:
            speak("Goodbye")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_jarvis()