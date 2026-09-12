from huggingface_hub import snapshot_download

ruta = snapshot_download(
    repo_id="SpeechAntiSpoofingBenchmarks/W2V2-AASIST",
    local_dir=r".\models\W2V2-AASIST",
    local_dir_use_symlinks=False,
)
print("Descargado en:", ruta)