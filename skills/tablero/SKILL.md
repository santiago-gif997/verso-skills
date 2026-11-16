---
name: tablero
description: Muestra el panorama de todos los proyectos (o clientes, marcas…) y qué necesita atención primero. Usar cuando el usuario pregunta "¿cómo viene todo?", "¿qué tengo abierto?", "muéstrame el tablero" o "/tablero".
---
# Tablero

## Configuración
Lee `memoria/CONFIG.md` (idioma, `termino_proyecto`, estados válidos).

## Pasos
1. Lee los datos de arriba de **todas** las fichas de `memoria/proyectos/` (no hace falta el historial).
2. Muestra una tabla ordenada por prioridad y luego por `actualizado` (más reciente primero): nombre · estado · próximo paso · a quién se espera · última actualización.
3. Debajo, **3 viñetas como máximo** con lo que pide atención primero:
   - ❗ prioridad alta sin próximo paso;
   - 🔒 trabados esperando a alguien;
   - ⏳ sin actualizar hace más de 14 días.
4. Si una ficha está incompleta o rota (falta el estado, la fecha o el próximo paso), lístala al final y ofrece arreglarla.
5. No escribas ningún archivo: el tablero se calcula cada vez, no se guarda.

## Adáptala a tu caso
- Cambia los criterios del paso 3 (días sin actualizar, qué cuenta como urgente).
- Añade columnas: ingresos esperados, fecha de entrega, responsable.
- Pide la salida como lista corta para leerla en el móvil, o como tabla para pegarla en un documento.
