---
name: project-huerto
description: "Huerto — app de gestión de huertos urbanos. Estado vivo: MVP en beta cerrada, 12 usuarios, pendiente sistema de riego v2."
metadata:
  type: project
---

# Proyecto Huerto (EJEMPLO FICTICIO / FICTIONAL EXAMPLE)

*(ES) Nota el formato: estado VIVO arriba (lo que cambia), fundamentos abajo (lo que no). Fechas absolutas siempre — "la semana pasada" no significa nada en tres meses.*
*(EN) Note the format: LIVE state on top (what changes), foundations below (what doesn't). Absolute dates always — "last week" means nothing three months from now.*

## Estado actual (actualizado 2026-01-20)
- **MVP en beta cerrada** desde 2026-01-10. 12 usuarios activos.
- Pendiente inmediato: sistema de riego v2 (el v1 notifica pero no calendariza).
- Bug abierto: las fotos de plantas rotan 90° en iOS — sospecha de EXIF, sin diagnosticar.
- Decisión pendiente de Alex: ¿cobrar en beta o esperar al launch?

## Qué es
App para gestionar huertos urbanos comunitarios: parcelas, calendarios de siembra, riego compartido. FastAPI + Postgres + PWA.

**Why:** los huertos comunitarios del barrio se coordinan por grupos de chat y se pierde todo. Alex tiene parcela en uno.

## Decisiones de arquitectura (con su porqué)
- **PWA, no app nativa** (2025-12-01): el público objetivo no instala apps; el costo de dos stores no se justifica en MVP.
- **Postgres sobre SQLite** (2025-12-15): multiusuario concurrente desde el día uno — los huertos editan en simultáneo los domingos.

## Historia comprimida
| Fecha | Hito |
|---|---|
| 2025-11-20 | Idea + primer esquema de datos |
| 2025-12-28 | Primer deploy a staging |
| 2026-01-10 | Beta cerrada con el huerto de Alex |
