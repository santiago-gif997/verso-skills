# Requisitos de ver-video

Se instalan una sola vez.

**Mac (con Homebrew):**
```
brew install ffmpeg yt-dlp
python3 -m venv ~/.venv-ver-video
~/.venv-ver-video/bin/pip install faster-whisper
```
Luego ejecuta el script con ese Python:
`~/.venv-ver-video/bin/python ver_video.py "<url>" --destino ./ver/tema`

**Windows / Linux:** instala ffmpeg y yt-dlp con tu gestor de paquetes y `pip install faster-whisper`.

Sin `faster-whisper` el script funciona igual, pero no transcribe la voz: solo saca el texto del post y los fotogramas.
La primera vez que transcribe, descarga el modelo de voz (unos cientos de MB).
