from detector import cargar_audio, score

wav = cargar_audio(r".\audio.wav")
print(score(wav))

# Si se desea acceder a valores individuales:
resultado = score(wav)
print(f"Score: {resultado['score']}")
print(f"P(fake): {resultado['p_fake']}")
print(f"P(bona): {resultado['p_bona']}")
print(f"Label: {resultado['label']}")