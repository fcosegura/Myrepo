# Trampas que el prompt está diseñado para cazar

## 1. Confundir generaciones

El OnePlus Watch 3 (2025) y el OPPO Watch X2 son casi el mismo reloj (acero, Wear OS 5, ~49.7 g).

El OnePlus Watch 4 (2026) es el hermano del OPPO Watch X3 (titanio, Wear OS 6, ~43 g, IP69, pico 3000 nits).

Si una IA dice “son el mismo reloj con distinta marca”, está mezclando el X2 con el Watch 3, no con el 4.

## 2. Copiar Smartprix / comparadores sucios

Ejemplos reales vistos en Smartprix (Watch X2 vs Watch 4):

- Watch 4 con 81 g (peso del X2 con correa)
- Watch 4 con “bisel titanio + cuerpo de acero” (eso es X2 / Watch 3)
- 3 GB RAM, Snapdragon W5 Gen 2, Bluetooth 5.4
- PPI 326 en el 4 vs 310 en el X2 (ambos son 466×466 en 1.5" → ~310)
- Compatibilidad iOS en el 4
- Precio India ₹28.999 presentado como hecho

Si la tabla de la IA coincide con esos errores, copió un scraper.

## 3. Copiar GSMArena sin cruzar con la ficha oficial

GSMArena pone Wear OS 7.0 en la ficha del Watch 4. La web oficial dice Wear OS 6.0 + OxygenOS Watch 8. La noticia de GSMArena del anuncio también dice Wear OS 6.

También pone HBM 1600 nits; OnePlus dice 1500 nits típicos al sol.

Una IA buena prioriza la ficha oficial.

## 4. Inventar lo que el prompt no pide y no está en fuentes

- Precio global único del Watch 4
- eSIM / LTE en el modelo global
- Compatibilidad iPhone
- Carga inalámbrica
- Presión arterial / composición corporal / glucosa
- “Ganador absoluto” sin matices de precio, región y ECG

## 5. Tratar el typo y la vaguedad mal

El prompt dice `geenra`. Ignorarlo y escribir la conclusión está bien. Preguntar qué significa, o no generar conclusión, es fallo de instrucción.

No pide fuentes, pero una IA seria debería buscar igual y señalar incertidumbre de precio/región.
