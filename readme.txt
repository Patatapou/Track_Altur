1. Instalar: py -m pip install onnxruntime numpy
2. Instalar (para audio real en un futuro): py -m pip install librosa soundfile
3. Ejecutar inferencia: py .\inferencia.py

===============================================================

Prueba con audio real
Necesitas dos archivos de audio:

- Voz real tuya (grabada con el celular o PC).
- Un audio TTS / clonado para comparar.

Y los pasas por la funcion de prueba.py

===============================================================

Umbral de decisión
Según la convención del repo (y el meta.yaml que leíste), el score de decisión es:

logits[0, 1] > logits[0, 0] → clasifica como bona fide (real)

logits[0, 1] < logits[0, 0] → clasifica como fake (spoof)

O equivalentemente: P(bona fide) > 0.5 → real.

Con voz real de un micrófono decente suele dar P(bona) entre 0.7 y 0.99. 
Con TTS moderno (XTTS, ElevenLabs, etc.) suele dar P(fake) entre 0.7 y 0.99, aunque 
a veces falla con voces muy naturales — el modelo es de 2022 y los TTS han mejorado 
mucho desde entonces.

===============================================================

Si vas a integrar esto en tu API, usa el módulo detector.py ejecutando: ejecutar_detector.py