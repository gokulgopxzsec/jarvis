from faster_whisper import WhisperModel

# Faster model for better UX
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int16"
)


def speech_to_text(audio_path):
    # Added initial_prompt to give the model context about the project
    segments, info = model.transcribe(
        audio_path, 
        language="en", 
        beam_size=5,
        vad_filter=True,
        initial_prompt="Jarvis, open notepad, search Google, create file." 
    )
    
    valid_text = []
    for seg in segments:
        # Only accept segments where the model is confident
        if seg.no_speech_prob < 0.1: 
            valid_text.append(seg.text)

    text = " ".join(valid_text).strip()

    if not text:
        print("⚠️ No speech detected or confidence too low")
        return ""

    print(f"🧠 You said: {text} (Language: {info.language})")
    return text