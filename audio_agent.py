import librosa
import numpy as np

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    variation = np.std(mfcc)

    if variation < 20:
        return {"risk": 0.6, "message": "Synthetic voice detected"}
    else:
        return {"risk": 0.2, "message": "Natural voice"}