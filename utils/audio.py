import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd
#print(sd.query_devices())

def record_audio(filename="input.wav", duration=7, fs=16000): # Increased to 7s
    print("🎙️ Listening... Speak now")
    
    # Optional: explicitly set device=index if you found one in step 1
    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    # Boost volume slightly before saving
    audio_int16 = np.int16(recording * 32767 * 1.5) 
    write(filename, fs, audio_int16)
    
    print("✅ Recorded")
    return filename