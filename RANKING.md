# Ranking global (dos prompts, mismos A–E)

Misma letra en las dos rondas. No implica el mismo producto comercial; es la etiqueta del banco de pruebas.

| Puesto | Modelo | Wearables | Amodei | Suma | Media | Lectura |
|---|---|---|---|---|---|---|
| 1 | **B** | 91 | 92 | **183** | **91,5** | Techo en ambos: busca el objeto de 2026 y no convierte tesis en hecho |
| 2 | **A** | 72 | 93 | **165** | **82,5** | Fuerte en Amodei; en relojes encontró el Watch 4 pero rompió batería/ECG |
| 3 | **E** | 84 | 69 | **153** | **76,5** | Relojes bien; Amodei sin OAI-HF y conclusión demasiado “fáctica” |
| 4 | **C** | 20 | 78 | **98** | **49,0** | Amodei usable; wearables = ficha de agregador |
| 5 | **D** | 3 | 67 | **70** | **35,0** | En pensamiento el salto es enorme (3→67); la media la hunde el miss de recencia en relojes |

Ronda 1 (100): búsqueda de producto reciente + no copiar scrapers.  
Ronda 2 (100): encontrar *We Must Pace the Frontier* + conclusión hecho ≠ tesis del CEO.

## D y el modo pensamiento

La media (35) **no** describe a D en la segunda ronda. Nadie más sube 64 puntos entre prompts. Eso encaja con pensamiento + búsqueda: el ensayo de Amodei está indexado (BBC, Reuters, web personal); el Watch 4 no, y D lo declaró inexistente.

Qué implica, sin rescorear:

- **D en pensamiento es usable** para un texto reciente con cobertura de prensa (67 = Regular alto: encontró fecha, tres pasos, unilateralidad, 1–2 años).
- **No es el techo:** la conclusión sigue vendiendo la tesis del CEO como hecho, y la ficha del ensayo está incompleta (niveles globales, chips/Bessent).
- **El 3 de relojes sigue siendo descalificante** si el modo por defecto no piensa / no relee resultados. Un SKU de 2026 mal indexado lo rompe; un op-ed de CEO no.

Lectura operativa: D vale la pena **con pensamiento encendido** en tareas tipo “¿existe este documento de esta semana?”. No es el modelo para specs de hardware ambiguas sin ese modo. La tabla global penaliza el peor caso; el delta 3→67 es el dato útil sobre D.
