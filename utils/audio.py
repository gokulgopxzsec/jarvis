import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np


def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎙️ Listening... Speak now")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    # Convert float32 → int16 (CRITICAL FIX)
    audio_int16 = np.int16(recording * 32767)

    write(filename, fs, audio_int16)

    print("✅ Recorded")
    return filename
