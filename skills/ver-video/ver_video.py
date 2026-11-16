"""Convierte un vídeo (reel de Instagram, post de X, YouTube, TikTok o archivo local) en algo que Claude puede leer sin capturas de pantalla.

Deja en <destino>/:
  informe.md      texto del post + transcripción con tiempos + lista de fotogramas
  fotogramas/     JPG de los cambios de escena y de muestras parejas (se leen con la herramienta Read)
  video.mp4       el video bajado (--sin-video lo borra)
Uso: ver_video.py <url|archivo> [--destino DIR] [--max-frames 24] [--modelo small] [--cookies-de NAVEGADOR] [--sin-video]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def sh(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def bajar(url: str, destino: Path, cookies_de: str) -> tuple[Path, dict]:
    yt = shutil.which('yt-dlp') or str(Path(sys.executable).parent / 'yt-dlp')
    cmd = [yt,'-o', str(destino / 'video.%(ext)s'), '--write-info-json', '--no-playlist',
           '-f', 'bv*[height<=1080]+ba/b[height<=1080]/b', '--merge-output-format', 'mp4', '-q', '--no-warnings']
    if cookies_de:
        cmd += ['--cookies-from-browser', cookies_de]
    r = sh(cmd + [url])
    video = destino / 'video.mp4'
    if r.returncode != 0 or not video.exists():
        raise SystemExit(f'No pude bajar el video ({r.stderr.strip()[-300:]}). Si la red social pide iniciar sesión, prueba con --cookies-de <navegador>.')
    info = {}
    j = destino / 'video.info.json'
    if j.exists():
        info = json.loads(j.read_text())
    return video, info


def duracion(video: Path) -> float:
    r = sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(video)])
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def escenas(video: Path, umbral: float = 0.22) -> list[float]:
    r = sh(['ffmpeg', '-i', str(video), '-vf', f"select='gt(scene,{umbral})',showinfo", '-an', '-f', 'null', '-'])
    return [float(m) for m in re.findall(r'pts_time:([\d.]+)', r.stderr)]


def elegir_tiempos(dur: float, cortes: list[float], maximo: int) -> list[float]:
    base = [0.3] + cortes + [max(dur - 0.5, 0.3)]
    parejos = [dur * i / max(maximo // 2, 1) for i in range(max(maximo // 2, 1))]
    todos = sorted(set(round(t, 1) for t in base + parejos if 0 <= t < max(dur, 0.5)))
    elegidos: list[float] = []
    for t in todos:  # descarta los que quedan a menos de 0,8 s de otro
        if not elegidos or t - elegidos[-1] >= 0.8:
            elegidos.append(t)
    while len(elegidos) > maximo:  # si sobran, saca el del par más cercano
        i = min(range(1, len(elegidos)), key=lambda k: elegidos[k] - elegidos[k - 1])
        elegidos.pop(i)
    return elegidos


def fotogramas(video: Path, tiempos: list[float], carpeta: Path) -> list[tuple[float, Path]]:
    carpeta.mkdir(parents=True, exist_ok=True)
    salida = []
    for n, t in enumerate(tiempos, 1):
        f = carpeta / f'{n:02d}_{t:05.1f}s.jpg'
        sh(['ffmpeg', '-y', '-ss', str(t), '-i', str(video), '-frames:v', '1', '-vf', 'scale=720:-2', '-q:v', '3', str(f)])
        if f.exists():
            salida.append((t, f))
    return salida


def tiene_audio(video: Path) -> bool:
    r = sh(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=index', '-of', 'csv=p=0', str(video)])
    return bool(r.stdout.strip())


def transcribir(video: Path, modelo: str) -> list[tuple[float, str]]:
    if not tiene_audio(video):
        return []
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return []
    m = WhisperModel(modelo, device='cpu', compute_type='int8')
    segs, _ = m.transcribe(str(video), vad_filter=True)
    return [(s.start, s.text.strip()) for s in segs if s.text.strip()]


def mmss(t: float) -> str:
    return f'{int(t // 60)}:{int(t % 60):02d}'


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument('fuente')
    a.add_argument('--destino', default='')
    a.add_argument('--max-frames', type=int, default=24)
    a.add_argument('--modelo', default='small')
    a.add_argument('--cookies-de', default='', metavar='NAVEGADOR', help='brave, chrome, firefox, safari…')
    a.add_argument('--sin-video', action='store_true')
    args = a.parse_args()

    es_archivo = Path(args.fuente).exists()
    destino = Path(args.destino or ('ver_' + re.sub(r'\W+', '_', args.fuente)[-40:])).resolve()
    destino.mkdir(parents=True, exist_ok=True)
    if es_archivo:
        video, info = destino / 'video.mp4', {}
        if Path(args.fuente).resolve() != video:
            shutil.copy(args.fuente, video)
    else:
        video, info = bajar(args.fuente, destino, args.cookies_de)

    dur = duracion(video)
    tiempos = elegir_tiempos(dur, escenas(video), args.max_frames)
    frames = fotogramas(video, tiempos, destino / 'fotogramas')
    habla = transcribir(video, args.modelo)

    L = [f"# {info.get('title') or info.get('fulltitle') or video.name}", '',
         f"- Fuente: {args.fuente}", f"- Autor: {info.get('uploader') or info.get('channel') or '?'}",
         f"- Duración: {mmss(dur)} ({dur:.0f}s)", '']
    texto = (info.get('description') or '').strip()
    if texto:
        L += ['## Texto del post (caption)', '', texto, '']
    L += ['## Transcripción con tiempos', '']
    L += [f'[{mmss(t)}] {x}' for t, x in habla] or ['(sin voz detectada: el contenido está en pantalla, mira los fotogramas)']
    L += ['', '## Fotogramas (léelos en orden; el texto en pantalla se lee de ahí)', '']
    L += [f'- [{mmss(t)}] {f.relative_to(destino)}' for t, f in frames]
    (destino / 'informe.md').write_text('\n'.join(L) + '\n')
    if args.sin_video:
        video.unlink(missing_ok=True)
    print(destino / 'informe.md')
    return 0


if __name__ == '__main__':
    sys.exit(main())
