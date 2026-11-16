# Cómo adaptar las skills a tu caso

No hace falta programar. Edita `memoria/CONFIG.md` o pídele a Claude: *"adapta la skill `retomar` para que…"*.

## 1. Cambia las palabras (CONFIG.md)
```
termino_proyecto: cliente
idioma: español
tono: cercano y breve
```
Las skills responderán "¿en qué quedamos con este cliente?" en vez de "proyecto".

## 2. Añade campos a la ficha
Las fichas aceptan los campos que quieras. Dile a Claude: *"añade a las fichas el campo `fecha_entrega` y muéstralo en `retomar` y `tablero`"*.

## 3. Ejemplos por tipo de uso

**Freelance con varios clientes**
- `termino_proyecto: cliente`
- Campos nuevos: `fecha_entrega`, `importe`, `facturado: sí/no`.
- En `tablero`: ordena por fecha de entrega y marca ❗ lo que vence esta semana.

**Tienda online**
- `termino_proyecto: línea de producto`
- Campos nuevos: `stock`, `proveedor`.
- En `cerrar`: añade el paso "actualizar la hoja de pedidos".

**Creador de contenido**
- `termino_proyecto: serie`
- Campos nuevos: `plataforma`, `próxima publicación`.
- En `anotar`: guarda cada idea en `memoria/ideas.md` con etiqueta `#reel` o `#carrusel`.

**Trader**
- `termino_proyecto: cuenta`
- Campos nuevos: `instrumento`, `riesgo_por_operación`.
- En `cerrar`: añade "anota las 3 decisiones del día y si seguí mi plan".

## 4. Una marca, varias voces
Si gestionas varias marcas, crea `memoria/marcas/<marca>.md` con su tono, sus palabras prohibidas y su idioma. En `retomar` añade el paso: *"si la ficha tiene `marca`, lee `memoria/marcas/<marca>.md` y respeta su voz"*.

## 5. Pide cambios pequeños
Lo que mejor funciona es pedir cambios concretos: *"cuando cierres, no escribas en el diario"*, *"el tablero en una línea por proyecto"*, *"responde siempre en italiano"*.
