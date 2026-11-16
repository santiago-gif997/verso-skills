---
name: retomar
description: Retoma un proyecto (o cliente, marca, curso…) leyendo su ficha, su historial y los archivos que cambiaron, para seguir sin volver a explicar nada. Usar cuando el usuario dice "seguimos con X", "retomemos X", "sigamos con X" o "/retomar X".
---
# Retomar un proyecto

## Configuración (léela primero)
Lee `memoria/CONFIG.md` (o la ruta que indique el `CLAUDE.md` del proyecto). De ahí salen: la carpeta de memoria, el idioma de las respuestas, el tono y cómo llama el usuario a sus cosas (`termino_proyecto`: proyecto, cliente, marca, cuenta…). Usa esas palabras al responder.
Si `memoria/` no existe, dilo en una línea y ofrece crearla (CONFIG.md + `proyectos/` + `inbox.md`, formato en el README del paquete). No sigas sin memoria.

## Pasos
1. **Encuentra la ficha.** Busca en `memoria/proyectos/` por nombre, alias o tema. Si hay varias candidatas, muestra una lista corta y pregunta cuál. Si no hay ninguna, dilo y ofrece crearla.
2. **Lee la ficha:** los datos de arriba (estado, próximo paso, a quién se espera) y las últimas 10 entradas del historial.
3. **Lee las reglas del proyecto:** si la ficha lista `carpetas`, lee ahí el `CLAUDE.md` / `README` si existen. Son reglas duras de ese proyecto.
4. **Mira qué cambió desde la última entrada del historial:** en las `carpetas` de la ficha, los archivos modificados más recientes (por ejemplo, los últimos 7 días). Léelos solo si hacen falta para entender dónde quedó.
5. **Responde corto, en este formato:**
   - **Dónde quedamos:** 1-2 líneas.
   - **Qué falta:** viñetas.
   - **Próximo paso:** uno solo, concreto.
   Después, sigue con lo que el usuario pida.
6. Si algo no está en la ficha ni en los archivos, dilo. No lo supongas.
7. Al terminar la sesión, la skill `cerrar` guarda lo hecho. No lo dupliques aquí.

## Adáptala a tu caso
- Cambia el formato de respuesta del paso 5 (por ejemplo, añade "Riesgos" o "Presupuesto").
- Añade a la ficha los campos que necesites (`cliente`, `fecha_entrega`, `canal`…) y pídele a Claude que los muestre al retomar.
- Si trabajas con varias marcas o clientes, agrupa las fichas en subcarpetas (`proyectos/marca-a/`) y retoma por el nombre de la marca.
