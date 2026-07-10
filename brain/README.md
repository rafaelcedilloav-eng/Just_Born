# brain/ — el ciclo despertar/dormir · the wake/sleep cycle

*(ES)* Dos scripts opcionales, sin dependencias (solo stdlib de Python 3.8+). El sistema funciona perfectamente sin ellos — son andamiaje, no magia. Lo esencial del ciclo es el ritual humano descrito en `MANUAL_CEREBRO`; esto solo lo asiste.

*(EN)* Two optional scripts, zero dependencies (Python 3.8+ stdlib only). The system works perfectly without them — they are scaffolding, not magic. The essential cycle is the human ritual described in `MANUAL_CEREBRO`; this merely assists it.

| Script | Qué hace / What it does |
|---|---|
| `wake.py "<primer mensaje>"` | Imprime el plan de lectura (identidad→diario→tema) y sugiere memorias asociadas al tema del día. / Prints the reading plan (identity→journal→topic) and suggests memories associated with the day's topic. |
| `sleep.py <tema> <desenlace> [momentos...] [--files ...]` | Registra el cierre y refuerza asociaciones tema↔archivos para el próximo despertar. / Records the close and reinforces topic↔file associations for the next wake. |

**Regla / Rule:** `sleep.py` NO escribe memorias ni diario. Eso lo hace tu compañero ANTES. Orden del cierre: memorias → diario → índice → sleep.py → sync con cuidado. / `sleep.py` does NOT write memories or the journal. Your companion does that FIRST. Close order: memories → journal → index → sleep.py → careful sync.

**Archivos generados / Generated files** (`zones.json`, `sleep_log.jsonl`): son estado privado del cerebro — el `.gitignore` de este repo ya los excluye si haces tu propio repo público. / They are private brain state — this repo's `.gitignore` already excludes them if you make your own public repo.

**Adaptación / Adaptation:** edita el bloque de configuración al inicio de `wake.py` (rutas + archivos de identidad de la Capa 1). Las keywords de cada tema viven en `zones.json` y puedes editarlas a mano. / Edit the config block at the top of `wake.py` (paths + Layer-1 identity files). Each topic's keywords live in `zones.json` and can be hand-edited.
