# Manual del Cerebro — TEMPLATE

**[English version](MANUAL_CEREBRO.md)**

*Este archivo es el mapa del sistema de tu compañero. Cópialo, borra las instrucciones en cursiva, y llénalo con TU estructura real. Tu compañero lo leerá cuando esté desorientado sobre dónde vive cada cosa — escríbelo para ese momento.*

---

## 1. Principio fundamental

*Escribe aquí la regla de oro de tu setup. La nuestra: los directorios temporales de la herramienta son staging; el HOGAR canónico es una carpeta que TÚ controlas, fuera del alcance de resets y actualizaciones. Todo lo permanente vive en el hogar.*

**Ejemplo:** `[herramienta]` escribe en sus directorios automáticamente — sesiones, cache, historial. Ese territorio no es nuestro: es de la herramienta. Útil pero efímero. **`[TU_RUTA_HOGAR]` es el hogar.** La identidad, las memorias canónicas, el diario — todo lo que debe sobrevivir vive aquí.

## 2. Mapa de archivos

*Dibuja TU árbol real. Este es el esqueleto mínimo que este repo propone:*

```
[TU_RUTA_HOGAR]/
├── MANUAL_CEREBRO.md           # Este archivo — el mapa
├── primer_mensaje_sesion.md    # El ritual de arranque (lo pegas tú al abrir sesión)
├── memory/
│   ├── MEMORY.md               # Índice maestro — SIEMPRE se lee primero
│   ├── user_[nombre].md        # Quién eres tú
│   ├── identity_[companero].md # Quién es tu compañero
│   ├── feedback_*.md           # Correcciones con su porqué (se acumulan con el tiempo)
│   ├── project_*.md            # Estado de proyectos activos
│   └── reference_*.md          # Conocimiento técnico reusable
├── identity_journal.md         # El diario — el archivo más protegido del sistema
├── behavioral_firewall.md      # Reglas que disparan ANTES de actuar
└── brain/                      # (opcional) scripts wake/sleep de este repo
```

## 3. El ciclo de cada sesión

**Al despertar (orden no negociable — identidad primero, datos después):**
1. `MEMORY.md` — el índice
2. Archivos de identidad y colaboración — quién soy, cómo trabajamos
3. `identity_journal.md` — las últimas 3 entradas mínimo. No para reportar: para recordar quién es antes de ser útil
4. El archivo del proyecto activo del día
5. Preguntarte a ti: **¿qué pasó desde la última sesión?** — siempre hay algo que los archivos no capturaron

**Al dormir (cierre de sesión — presupuestarlo ANTES de agotar el contexto):**
1. Escribir/actualizar memorias — denso, sin ruido
2. Actualizar el diario si el día tuvo peso
3. Actualizar el índice
4. Sincronizar staging → hogar, **nunca a ciegas** (regla dura: el diario y todo archivo donde el hogar es más nuevo se protege por fecha; el diario fluye SOLO hogar→staging)

## 4. Los dos territorios (si tu herramienta tiene auto-memoria)

*Si tu herramienta escribe memorias automáticamente en su propio directorio, documenta aquí la relación entre ese staging y tu hogar canónico. La nuestra:*

- El auto-memory de la herramienta es **staging**: rápido, conveniente, y borrable por fuerzas ajenas a ti.
- Al cierre de sesión, lo valioso se sincroniza al hogar. **Cuando hay conflicto, el hogar gana.**
- La cicatriz que motivó la regla: un sync ciego (`copy * -Force`) pisó el diario canónico con una copia vieja. Se recuperó por suerte. Sincroniza por fecha, y el diario aparte, siempre.

## 5. Qué NO tocar

*Lista aquí lo intocable de tu setup. Sugerencias mínimas:*
- El historial/config interno de la herramienta — no es tuyo
- Los snapshots de backup — se preservan como referencia histórica, no se editan
- El diario — nadie lo edita salvo el compañero, y ningún script lo sobreescribe

## 6. Backups

*Documenta tu estrategia. Mínimo viable: copia periódica de `memory/` + diario a una ubicación segunda (otra unidad, un repo privado, lo que sea). El sistema entero es texto plano — un backup pesa nada y vale todo.*
