# Verso Skills

Skills para Claude Code que dan **memoria de trabajo** a tu asistente: retomar un proyecto sin volver a explicar nada, cerrar la sesión guardando todo, anotar al vuelo y ver vídeos como si los hubiera visto una persona.

Son genéricas. Sirven para un proyecto, para varios clientes, para una marca o para tu propio negocio. Tú decides cómo se llaman las cosas, en qué idioma responde y qué guarda.

| Skill | Qué hace | Frase para activarla |
|---|---|---|
| `retomar` | Lee la ficha de un proyecto y te dice dónde quedaron, qué falta y el próximo paso | "seguimos con X" |
| `estado` | Responde "¿en qué quedamos con X?" en 4 líneas | "¿cómo va X?" |
| `cerrar` | Guarda en la memoria lo hecho en la sesión | "cerramos" |
| `anotar` | Guarda una cosa al vuelo | "acuérdate de…" |
| `tablero` | Panorama de todos tus proyectos y qué atender primero | "¿cómo viene todo?" |
| `ver-video` | Baja un vídeo, lo transcribe con tiempos y lee el texto en pantalla | "mira este vídeo: <enlace>" |

## Instalar (2 minutos)

1. Copia las carpetas de `skills/` que quieras a `~/.claude/skills/` (para todos tus proyectos) o a `.claude/skills/` dentro de un proyecto.
2. Copia `memoria-plantilla/` a la carpeta de trabajo y renómbrala a `memoria/`.
3. Abre `memoria/CONFIG.md` y pon tu nombre, tu idioma y cómo llamas a tus cosas.
4. Abre Claude Code en esa carpeta y escribe: `seguimos con mi primer proyecto`.

`ver-video` necesita además ffmpeg, yt-dlp y faster-whisper: mira `skills/ver-video/requisitos.md`.

## Cómo funciona la memoria

Todo son archivos de texto en `memoria/`, sin base de datos ni servicios. Puedes leerlos, editarlos y guardarlos en git.

```
memoria/
  CONFIG.md          tu configuración (idioma, tono, zona horaria, nombres)
  inbox.md           lo anotado al pasar
  proyectos/         una ficha por proyecto: estado, próximo paso, historial
  diario/            opcional
  decisiones/        opcional
  personas/          opcional
```

La ficha de un proyecto es un archivo con datos arriba (estado, próximo paso, a quién se espera, fecha, carpetas) y un historial abajo. Hay un ejemplo en `memoria-plantilla/proyectos/ejemplo.md`.

## Adáptalas

Cada `SKILL.md` es un texto que puedes editar, y termina con una sección **"Adáptala a tu caso"** con ideas. Mira `PERSONALIZAR.md` para ejemplos por tipo de uso (freelance, tienda online, creador de contenido, trader).

## Privacidad

Todo se queda en tus archivos locales. `ver-video` descarga vídeos a tu equipo y los transcribe en tu equipo; no envía nada a ningún servicio. Si usas `--cookies-de`, yt-dlp lee las sesiones de tu navegador solo para bajar ese vídeo.

## Licencia

MIT: úsalas, cámbialas y compártelas. Mira `LICENSE`.

Hechas por Verso (versojournal.app), el diario de trading cifrado.
