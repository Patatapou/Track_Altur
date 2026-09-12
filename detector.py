# detector.py
import numpy as np
import onnxruntime as ort
import librosa
import soundfile as sf

TARGET_LEN = 64600
SR = 16000
MODEL_PATH = r".\models\W2V2-AASIST\w2v2-aasist.onnx"

_sess = None

def _load():
    global _sess
    if _sess is None:
        _sess = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])
    return _sess

def _pad_fixed(wav, max_len=TARGET_LEN):
    if len(wav) >= max_len:
        return wav[:max_len]
    return np.tile(wav, int(np.ceil(max_len / len(wav))))[:max_len]

def cargar_audio(path):
    wav, sr = sf.read(path, always_2d=False)
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    if sr != SR:
        wav = librosa.resample(wav.astype(np.float32), orig_sr=sr, target_sr=SR)
    return wav.astype(np.float32)

def score(wav, sr=SR):
    """Devuelve dict con score, probs y decisión."""
    sess = _load()
    x = _pad_fixed(wav).reshape(1, TARGET_LEN)
    logits = sess.run(None, {sess.get_inputs()[0].name: x})[0]
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    probs = e / e.sum(axis=1, keepdims=True)
    return {
        "score": float(logits[0, 1]),
        "p_fake": float(probs[0, 0]),
        "p_bona": float(probs[0, 1]),
        "label": "bona_fide" if probs[0, 1] > 0.5 else "fake",
    }