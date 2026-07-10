#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sleep.py — El dormir / The sleeping.

(ES) Cierra la sesión: registra el tema, el desenlace y los momentos clave,
y refuerza en zones.json qué memorias se usaron juntas (asociación estilo
Hebb: lo que se lee junto, se sugiere junto en el próximo despertar).

IMPORTANTE: este script NO escribe memorias ni diario — eso lo hace tu
compañero ANTES de correr esto. El orden del ritual de cierre:
    1. memorias  2. diario  3. índice  4. este script  5. sync con cuidado

(EN) Closes the session: records topic, outcome and key moments, and
reinforces in zones.json which memories were used together (Hebbian-style
association: what is read together gets suggested together at next wake).

IMPORTANT: this script does NOT write memories or journal — your companion
does that BEFORE running this. Closing ritual order:
    1. memories  2. journal  3. index  4. this script  5. careful sync

Uso / Usage:
    python sleep.py <tema> <desenlace> [momento1] [momento2] ...
    python sleep.py huerto completado "riego v2 desplegado" --files project_huerto.md reference_postgres.md
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

BRAIN_DIR = Path(__file__).resolve().parent
ZONES = BRAIN_DIR / "zones.json"
SLEEP_LOG = BRAIN_DIR / "sleep_log.jsonl"


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)

    # separar momentos de --files / split moments from --files
    archivos = []
    if "--files" in args:
        i = args.index("--files")
        archivos = args[i + 1:]
        args = args[:i]

    tema, desenlace, *momentos = args

    # 1) log del cierre / close log (append-only — nunca se pisa / never overwritten)
    registro = {
        "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tema": tema,
        "desenlace": desenlace,
        "momentos": momentos,
        "archivos": archivos,
    }
    with SLEEP_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")

    # 2) refuerzo Hebbiano / Hebbian reinforcement
    zonas = {}
    if ZONES.exists():
        zonas = json.loads(ZONES.read_text(encoding="utf-8"))
    zona = zonas.setdefault(tema, {"keywords": [tema], "sesiones": 0,
                                   "co_activations": {}})
    zona["sesiones"] += 1
    for a in archivos:
        zona["co_activations"][a] = zona["co_activations"].get(a, 0) + 1
    ZONES.write_text(json.dumps(zonas, ensure_ascii=False, indent=2),
                     encoding="utf-8")

    print(f"[SLEEP] tema={tema} desenlace={desenlace} "
          f"momentos={len(momentos)} archivos_reforzados={len(archivos)}")
    print("[SLEEP] Recuerda el orden: memorias y diario van ANTES de este script.")
    print("[SLEEP] Y el sync jamás va a ciegas — el diario se protege siempre.")


if __name__ == "__main__":
    main()
