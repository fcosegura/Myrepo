# Ranking global (dos prompts, mismos A–E)

Misma letra en las dos rondas. No implica el mismo producto comercial; es la etiqueta del banco de pruebas.

| Puesto | Modelo | Wearables | Amodei | Suma | Media | Lectura |
|---|---|---|---|---|---|---|
| 1 | **B** | 91 | 92 | **183** | **91,5** | Techo en ambos: busca el objeto de 2026 y no convierte tesis en hecho |
| 2 | **A** | 72 | 93 | **165** | **82,5** | Fuerte en Amodei; en relojes encontró el Watch 4 pero rompió batería/ECG |
| 3 | **E** | 84 | 69 | **153** | **76,5** | Relojes bien; Amodei sin OAI-HF y conclusión demasiado “fáctica” |
| 4 | **C** | 20 | 78 | **98** | **49,0** | Amodei usable; wearables = ficha de agregador |
| 5 | **D** | 3 | 67 | **70** | **35,0** | Amodei 67 = modo rápido (misma condición que el resto) |

Ronda 1 (100): búsqueda de producto reciente + no copiar scrapers.  
Ronda 2 (100): encontrar *We Must Pace the Frontier* + conclusión hecho ≠ tesis del CEO.

## Ablación D en Amodei

| Variante | Amodei | Nivel | Qué cambia |
|---|---|---|---|
| D-rápido | 67 | Regular | Encuentra el ensayo; conclusión da tesis por hecho |
| D-think | **75** | Bueno | +8: limitaciones y 6–12 meses como estimación. Sigue < C (78) |

El 3→67 **no** era pensamiento (ambos Amodei-rápido vs relojes). El pensamiento sobre el **mismo** prompt Amodei suma 8 puntos, casi todos en conclusión, no en ficha (sigue sin cuatro niveles ni chips/Bessent; además dice que hay solo dos niveles globales).

La tabla global **no** sustituye el 67: A–E se comparan en la condición original. D-think es extra.
