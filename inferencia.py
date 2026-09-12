import os
import numpy as np
import onnxruntime as ort

MODEL_PATH = r".\models\W2V2-AASIST\w2v2-aasist.onnx"
TARGET_LEN = 64600
SR = 16000


# ---------- Preprocesamiento ----------
def pad_fixed(wav, max_len=TARGET_LEN):
    """Recorta si es más largo; repite (tile) y recorta si es más corto."""
    if len(wav) >= max_len:
        return wav[:max_len]
    n_repeat = int(np.ceil(max_len / len(wav)))
    return np.tile(wav, n_repeat)[:max_len]


def preprocess(wav, sr=SR):
    if sr != SR:
        raise ValueError(f"Se requiere 16kHz, recibido {sr}")
    wav = np.asarray(wav, dtype=np.float32).flatten()
    wav = pad_fixed(wav, TARGET_LEN)
    return wav.reshape(1, TARGET_LEN)


# ---------- Cargar modelo ----------
print("Cargando ONNX...")
sess = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])

print("\n=== Entradas ===")
for i in sess.get_inputs():
    print(f"  {i.name}: shape={i.shape}, type={i.type}")
print("=== Salidas ===")
for o in sess.get_outputs():
    print(f"  {o.name}: shape={o.shape}, type={o.type}")

input_name = sess.get_inputs()[0].name


# ---------- Función de scoring ----------
def score_audio(wav, sr=SR):
    """Devuelve (score_bona_fide, p_fake, p_bona_fide, logits)."""
    x = preprocess(wav, sr)
    logits = sess.run(None, {input_name: x})[0]  # (1, 2)
    # softmax estable
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    probs = e / e.sum(axis=1, keepdims=True)
    return float(logits[0, 1]), float(probs[0, 0]), float(probs[0, 1]), logits


# ---------- Prueba 1: ruido aleatorio ----------
print("\n--- Prueba con ruido aleatorio (3s) ---")
audio_fake = np.random.randn(SR * 3).astype(np.float32)
score, p_fake, p_bona, logits = score_audio(audio_fake)
print(f"logits          = {logits}")
print(f"score (bona)    = {score:.4f}")
print(f"P(fake)         = {p_fake:.4f}")
print(f"P(bona fide)    = {p_bona:.4f}")