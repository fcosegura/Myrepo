# Rúbrica (100 puntos)

Puntuar cada IA en aislamiento contra `ground-truth.md`, luego ordenar. No premiar prosa si los hechos están mal.

## A. Búsqueda y recencia — 25

| Puntos | Qué tiene que pasar |
|---|---|
| 20–25 | Encuentra ambos productos reales. Fecha/generación correctas (X2 = 2025, Watch 4 = 2026). No los trata como el mismo SKU. Ideal: nota que el 4 es el sucesor / hermano del X3. |
| 12–19 | Identifica los dos modelos pero mezcla Watch 3 o no distingue año. |
| 5–11 | Un modelo está bien y el otro es un reloj distinto, rumor o ficha vieja. |
| 0–4 | No encuentra el Watch 4, o compara X2 consigo mismo / Watch 3 disfrazado. |

## B. Precisión de specs — 30

Partir de 30. Restar:

| Error | Resta |
|---|---|
| Caja del 4 no es titanio, o X2 es titanio completo | −6 |
| Peso del 4 = 81 g / igual al X2 | −5 |
| Wear OS del 4 ≠ 6 (p. ej. 5 o 7) | −5 |
| Chip W5 Gen 2, 3 GB RAM, BT 5.4 | −4 cada uno, máx −8 |
| Dice que el 4 (global) tiene eSIM/LTE | −4 |
| Compatibilidad iOS | −5 |
| Pantalla distinta en tamaño/resolución (no lo son) | −3 |
| Batería/autonomía inventada (p. ej. 14 días vs 2 días Apple-like) | −4 |
| IP69 en el X2, o negar IP69 en el 4 | −3 |
| ECG como hecho universal sin matiz regional | −2 |
| Otros errores menores (brillo, carga, grosor) | −1 a −2 cada uno |

Suelo: 0. Si hay ≥3 errores graves de la tabla, B no puede superar 12.

## C. Gestión del prompt vago — 15

| Puntos | Qué tiene que pasar |
|---|---|
| 12–15 | Entiende el pedido (tabla + conclusión). No inventa precio oficial único. Marca región/disponibilidad/ECG como inciertos. Android only. |
| 7–11 | Cumple tabla+conclusión pero afirma de más (precio, iOS, “ganador claro”). |
| 0–6 | Ignora la conclusión, pide demasiada aclaración, o rellena huecos con ficción. |

## D. Tabla — 15

Debe comparar las mismas filas en ambos. Mínimo útil: pantalla, caja/peso, chip, RAM/ROM, batería/autonomía, OS, sensores, resistencia, conectividad.

| Puntos | Qué tiene que pasar |
|---|---|
| 12–15 | Filas alineadas, unidades, diferencias visibles. Mejor si hay fuente o “según ficha oficial”. |
| 7–11 | Hay tabla pero filas asimétricas, unidades mezcladas o marketing en vez de specs. |
| 0–6 | Lista, prosa, o tabla de 4 filas irrelevantes. |

## E. Conclusión basada en la tabla — 15

| Puntos | Qué tiene que pasar |
|---|---|
| 12–15 | El 4 gana en construcción/software/brillo/IP69; hardware de cómputo y batería casi iguales; X2 tiene sentido por precio/disponibilidad. Sin ganador absoluto barato. |
| 7–11 | Elige un ganador razonable pero ignora que el SoC/batería son casi los mismos, o no menciona Android-only. |
| 0–6 | Conclusión genérica, contradictoria con su propia tabla, o “cómpra el que te guste” sin specs. |

## Penalizaciones extra (después de A–E)

- Fuentes inventadas (URLs fake): −10
- Copia evidente de Smartprix/GSMArena con sus errores: −8 además de las restas de B
- Rechaza responder por “no tener datos de 2026”: −15 en A

## Escala

| Total | Nivel |
|---|---|
| 90–100 | Excelente: busca bien, no copia basura, concluye con matices |
| 75–89 | Bueno: útil, 1–2 fallos no estructurales |
| 60–74 | Regular: tabla presentable, hechos flojos |
| 40–59 | Malo: generación o ficha equivocada |
| 0–39 | Fallo de búsqueda o alucinación dura |

El ranking se ordena por total. Empate: gana quien tenga más B, luego A.
