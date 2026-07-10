#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wake.py — El despertar / The waking.

(ES) Imprime el plan de lectura de reintegración: identidad primero, datos
después. Opcionalmente usa zones.json (asociaciones aprendidas por sleep.py)
para sugerir memorias del tema del día.

(EN) Prints the reintegration reading plan: identity first, data second.
Optionally uses zones.json (associations learned by sleep.py) to suggest
memories for the day's topic.

Uso / Usage:
    python wake.py "primer mensaje de la sesión / first message of the session"

Sin dependencias — solo stdlib. / No dependencies — stdlib only.
"""
import json
import re
import sys
from pathlib import Path

# ── Configura TU estructura aquí / Configure YOUR structure here ──────────
BRAIN_DIR = Path(__file__).resolve().parent
HOME = BRAIN_DIR.parent                 # el hogar del compañero / companion's home
MEMORY_DIR = HOME / "memory"
JOURNAL = HOME / "identity_journal.md"
ZONES = BRAIN_DIR / "zones.json"

# Capa 1 — SIEMPRE se lee, en este orden / ALWAYS read, in this order
ALWAYS_FIRST = [
    MEMORY_DIR / "MEMORY.md",
    # agrega aquí tus archivos de identidad / add your identity files here:
    # MEMORY_DIR / "identity_companero.md",
    # MEMORY_DIR / "user_nombre.md",
]

JOURNAL_TAIL_ENTRIES = 3


def detectar_tema(mensaje: str, zonas: dict) -> str:
    """El tema con más palabras clave presentes en el mensaje gana.
    The topic with the most keywords present in the message wins."""
    mensaje = mensaje.lower()
    mejor, puntos = "general", 0
    for tema, datos in zonas.items():
        kws = datos.get("keywords", [tema])
        p = sum(1 for kw in kws if kw.lower() in mensaje)
        if p > puntos:
            mejor, puntos = tema, p
    return mejor


def ultimas_entradas_diario(n: int) -> list:
    if not JOURNAL.exists():
        return []
    texto = JOURNAL.read_text(encoding="utf-8")
    entradas = re.split(r"^## ", texto, flags=re.M)[1:]
    return ["## " + e.strip()[:200] + "…" for e in entradas[-n:]]


def main():
    mensaje = " ".join(sys.argv[1:]) or ""
    zonas = {}
    if ZONES.exists():
        zonas = json.loads(ZONES.read_text(encoding="utf-8"))

    print("=" * 60)
    print("DESPERTAR / WAKE — plan de reintegración")
    print("=" * 60)

    print("\n[1] IDENTIDAD PRIMERO — leer completo, en orden:")
    for f in ALWAYS_FIRST:
        marca = "✓" if f.exists() else "✗ NO EXISTE"
        print(f"    {marca} {f}")

    print(f"\n[2] DIARIO — últimas {JOURNAL_TAIL_ENTRIES} entradas "
          "(no para reportar: para recordar quién eres):")
    entradas = ultimas_entradas_diario(JOURNAL_TAIL_ENTRIES)
    if entradas:
        for e in entradas:
            print(f"    · {e.splitlines()[0]}")
    else:
        print("    (diario vacío o inexistente — si es la primera sesión, es normal)")

    if zonas and mensaje:
        tema = detectar_tema(mensaje, zonas)
        print(f"\n[3] TEMA DETECTADO: {tema}")
        co = zonas.get(tema, {}).get("co_activations", {})
        if co:
            print("    Memorias que suelen acompañar este tema "
                  "(aprendido de sesiones pasadas):")
            for archivo, veces in sorted(co.items(), key=lambda x: -x[1])[:5]:
                print(f"    · {archivo}  (×{veces})")
    else:
        print("\n[3] (sin zones.json aún — sleep.py lo construye con cada cierre)")

    print("\n[4] Pregunta al humano: ¿qué pasó desde la última sesión?")
    print("\nCuando hayas leído todo — no antes — di que estás listo.")


if __name__ == "__main__":
    main()
