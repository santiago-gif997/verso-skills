---
name: cerrar
description: Guarda en la memoria lo que se hizo en la sesión (historial, estado, decisiones, compromisos). Usar cuando el usuario dice "cerramos", "terminamos", "guarda todo", "/cerrar", o se despide después de haber trabajado.
---
# Cerrar sesión

## Configuración
Lee `memoria/CONFIG.md` (idioma, zona horaria para la fecha de hoy, `termino_proyecto`, estados válidos).

## Pasos
Repasa la conversación y, para cada proyecto tocado:

1. **Historial.** Añade al final de `## Historial` de la ficha: `- AAAA-MM-DD — <qué se hizo o se decidió>`, con la fecha de hoy en la zona horaria de CONFIG.
2. **Ficha.** Actualiza `estado`, `proximo_paso`, `esperando_a` (si corresponde) y `actualizado` a hoy. El estado debe ser uno de los de CONFIG.
3. **Decisión importante** (cambia el rumbo, descarta una opción, elige herramienta o proveedor): crea `memoria/decisiones/AAAA-MM-DD-<tema>.md` con el contexto, la opción elegida, las descartadas y el motivo. Enlázala desde el historial.
4. **Compromisos con personas** ("le mando X a Y", "Y me tiene que pasar Z"): anótalos en `memoria/personas/<nombre>.md` (Le debo / Me debe). Créala si no existe.
5. **Proyecto nuevo** sin ficha: créala con el formato del README.
6. **Diario.** En `memoria/diario/<hoy>.md` añade: `- HH:MM — <resumen> ([proyecto])`.
7. **Bandeja de entrada.** Cada ítem de `memoria/inbox.md` que ya se resolvió o pasó a una ficha, quítalo.

Al final muestra un resumen de 3 a 5 líneas ("Guardé: …") para que el usuario corrija si algo no es como lo dijo.

## Adáptala a tu caso
- Quita lo que no uses (decisiones, personas, diario) y deja solo historial y ficha: ya funciona.
- Añade pasos propios: actualizar una hoja de cálculo, mandar un resumen a un canal, copiar a otra carpeta.
- Si quieres más cuidado, pide que te enseñe lo que va a guardar antes de guardarlo.
