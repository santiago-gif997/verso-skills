---
name: anotar
description: Guarda algo al pasar para no olvidarlo. Usar cuando el usuario dice "acuérdate de…", "anota…", "que no se me olvide…" o "/anotar".
---
# Anotar

## Configuración
Lee `memoria/CONFIG.md` para saber la zona horaria (fecha de hoy) y el idioma. Si `memoria/` no existe, créala con un `inbox.md` vacío.

## Pasos
1. Si lo que dice el usuario es claramente un **dato** de un proyecto que ya tiene ficha (no una tarea), añádelo directo al historial de esa ficha: `- AAAA-MM-DD — <texto>`.
2. Si no, añádelo al final de `memoria/inbox.md`: `- [ ] AAAA-MM-DD — <texto tal cual lo dijo>`.
3. Confirma en una línea: "Anotado en el inbox." o "Anotado en <proyecto>.". Nada más.

## Adáptala a tu caso
- Cambia el destino: un archivo por día, una nota por tema, una hoja de cálculo.
- Añade etiquetas (`#urgente`, `#cliente-x`) si quieres filtrar luego.
- Pide que cada lunes te lea el inbox y proponga a qué ficha va cada cosa.
