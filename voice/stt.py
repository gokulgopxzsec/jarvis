from faster_whisper import WhisperModel

# Faster model for better UX
model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)


def speech_to_text(audio_path):
    segments, _ = model.transcribe(audio_path)
    text = " ".join([seg.text for seg in segments]).strip()

    if not text:
        print("⚠️ No speech detected")
        return ""

    print(f"🧠 You said: {text}")
    return text
