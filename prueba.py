import librosa
import soundfile as sf
import numpy as np

from inferencia import score_audio

def cargar_audio(path):
    wav, sr = sf.read(path, always_2d=False)
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    if sr != 16000:
        wav = librosa.resample(wav.astype(np.float32), orig_sr=sr, target_sr=16000)
    return wav.astype(np.float32), 16000

for path in [r".\voz_real.wav", r".\voz_tts.wav"]:
    wav, sr = cargar_audio(path)
    score, p_fake, p_bona, logits = score_audio(wav, sr)
    print(f"{path}")
    print(f"  logits      = {logits}")
    print(f"  score bona  = {score:.4f}")
    print(f"  P(fake)     = {p_fake:.4f}  |  P(bona) = {p_bona:.4f}")
    print()