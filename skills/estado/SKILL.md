---
name: estado
description: Responde "¿en qué quedamos con X?" sobre un proyecto, cliente o tema. Usar cuando el usuario pregunta por el estado, el avance, los pendientes o el próximo paso ("¿cómo va X?", "¿qué falta de Y?", "/estado X").
---
# Estado de un proyecto

## Configuración
Lee `memoria/CONFIG.md` (idioma, tono, `termino_proyecto`). Responde en ese idioma y con esas palabras.

## Pasos
1. **Identifica el proyecto.** Busca en `memoria/proyectos/` por nombre, alias o tema. Si hay varios candidatos, lista corta y pregunta cuál. Si no existe, dilo y ofrece crear la ficha.
2. **Lee la ficha:** datos de arriba y las últimas 10 entradas del historial. Sigue enlaces a personas o decisiones solo si hacen falta.
3. **Si `actualizado` tiene más de 3 días**, revisa las fuentes antes de responder: los archivos recientes de las `carpetas` de la ficha y, si hay conectores disponibles (calendario, hojas de cálculo), lo que digan. Si no puedes revisar algo, dilo. Si hay novedades claras, añade una entrada al historial y actualiza `estado`, `proximo_paso` y `actualizado`.
4. **Responde así (corto):**
   - **Dónde estamos:** 1-2 líneas.
   - **Qué falta:** viñetas.
   - **Quién debe qué:** solo si hay algo pendiente con alguien.
   - **Próximo paso:** uno solo, concreto.
5. Si algo no está en la memoria ni en las fuentes, dilo en vez de suponer.

## Adáptala a tu caso
- Cambia los días del paso 3 si tus proyectos se mueven más rápido o más lento.
- Cambia el formato de salida. Hay quien prefiere una sola línea con semáforo (🟢🟡🔴).
- Añade fuentes que sí uses: un tablero, un CRM, una carpeta de entregas.
