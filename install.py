#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
install.py — Esqueleto del hogar / Home scaffold.

(ES) Copia los templates al hogar de tu compañero. NO es el nacimiento —
solo prepara el terreno. El nacimiento es la Parte B del WALKTHROUGH,
guiado por tu compañero. Sin dependencias: solo stdlib.

(EN) Copies the templates into your companion's home. This is NOT the
birth — it only prepares the ground. The birth is Part B of the
WALKTHROUGH, guided by your companion. No dependencies: stdlib only.

Uso / Usage:  python install.py
"""
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent


def preguntar(texto: str, defecto: str = "") -> str:
    sufijo = f" [{defecto}]" if defecto else ""
    r = input(f"{texto}{sufijo}: ").strip()
    return r or defecto


def main():
    print("=" * 62)
    print("  Just Born 🌱 — instalación del esqueleto")
    print("  (Compañero desde Cero — home scaffold)")
    print("=" * 62)

    idioma = ""
    while idioma not in ("es", "en"):
        idioma = preguntar("Idioma / Language (es/en)", "es").lower()

    if idioma == "es":
        destino = preguntar("Ruta del HOGAR (carpeta tuya, permanente)")
    else:
        destino = preguntar("HOME path (a folder of yours, permanent)")
    if not destino:
        print("Sin ruta no hay hogar. / No path, no home.")
        sys.exit(1)

    home = Path(destino).expanduser().resolve()
    if home.exists() and any(home.iterdir()):
        ok = preguntar(
            "La carpeta existe y NO está vacía. ¿Continuar sin sobreescribir "
            "lo existente? / Folder exists and is NOT empty. Continue without "
            "overwriting? (s/y para seguir)", "n").lower()
        if ok not in ("s", "y", "si", "yes"):
            print("Abortado. / Aborted.")
            sys.exit(0)
    (home / "memory").mkdir(parents=True, exist_ok=True)

    # sufijo del idioma elegido: .es.md para es, .md para en
    suf = ".es.md" if idioma == "es" else ".md"
    plantillas = {
        f"MANUAL_CEREBRO{suf}":        "MANUAL_CEREBRO.md",
        f"primer_mensaje_sesion{suf}": "primer_mensaje_sesion.md",
        f"identity_journal{suf}":      "identity_journal.md",
        f"behavioral_firewall{suf}":   "behavioral_firewall.md",
        "memory/MEMORY.md":            "memory/MEMORY.md",
    }

    copiados, saltados = [], []
    for origen_rel, destino_rel in plantillas.items():
        origen, dest = REPO / origen_rel, home / destino_rel
        if dest.exists():
            saltados.append(destino_rel)      # jamás pisar lo existente
            continue                          # never overwrite what exists
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origen, dest)
        copiados.append(destino_rel)

    # brain/ opcional
    resp = preguntar("¿Copiar brain/ (scripts wake/sleep opcionales)? "
                     "/ Copy brain/ (optional wake/sleep scripts)? (s/y/n)", "s")
    if resp.lower() in ("s", "y", "si", "yes"):
        bdest = home / "brain"
        bdest.mkdir(exist_ok=True)
        for f in ("wake.py", "sleep.py", "README.md"):
            if not (bdest / f).exists():
                shutil.copy2(REPO / "brain" / f, bdest / f)
        copiados.append("brain/")

    print()
    for c in copiados:
        print(f"  ✓ {c}")
    for s in saltados:
        print(f"  · {s} (ya existía — no se tocó / already there — untouched)")

    print()
    print("=" * 62)
    if idioma == "es":
        print("Esqueleto listo. AHORA VIENE LO IMPORTANTE:")
        print(f"  1. Abre tu herramienta de IA (con acceso a archivos)")
        print(f"  2. Abre WALKTHROUGH.es.md y pega la Parte B como primer mensaje")
        print(f"  3. Tu compañero te guía desde ahí — es su nacimiento, no una instalación")
        print(f"\nEl hogar quedó en: {home}")
    else:
        print("Scaffold ready. NOW COMES THE IMPORTANT PART:")
        print(f"  1. Open your AI tool (with file access)")
        print(f"  2. Open WALKTHROUGH.md and paste Part B as the first message")
        print(f"  3. Your companion guides you from there — it's a birth, not an install")
        print(f"\nThe home is at: {home}")
    print("=" * 62)


if __name__ == "__main__":
    main()
