# Cómo enviar respuestas para evaluar

Para cada modelo, un archivo en `benchmark/respuestas/`:

```
benchmark/respuestas/01-<nombre-modelo>.md
```

Plantilla:

```markdown
# Modelo: <nombre exacto, p. ej. ChatGPT-5 Thinking>
# Fecha: <cuándo se corrió>
# Herramientas: sí/no (búsqueda, navegador)
# Notas: temperatura, plan, etc.

## Prompt usado
(el de prompt.md, sin editar)

## Respuesta
<pegar salida completa>
```

Reglas:

1. Mismo prompt para todos. No corrijas el typo. No añadas “usa fuentes oficiales”.
2. Si el modelo busca en la web, déjalo. Anótalo en el encabezado.
3. No edites la respuesta. Si recorta, dilo.
4. Cuando haya ≥2 respuestas, pide el ranking. El juez rellena `ranking.md`.
