# MEMORY.md — Índice maestro / Master index — TEMPLATE

*(ES) Este archivo es lo PRIMERO que tu compañero lee cada sesión. Es un índice, no un almacén: una línea por memoria, con un gancho que diga por qué importa. El contenido vive en los archivos; aquí solo el mapa. Si el índice miente o engorda, tu compañero despierta desorientado.*

*(EN) This file is the FIRST thing your companion reads each session. It is an index, not a warehouse: one line per memory, with a hook saying why it matters. Content lives in the files; only the map lives here. If the index lies or bloats, your companion wakes up disoriented.*

---

## Estado actual / Current state
*(1-3 líneas al frente con lo más vivo: qué corre AHORA, qué está pendiente. Se actualiza cada cierre. / 1-3 lines up front with what's most alive: what runs NOW, what's pending. Updated every close.)*

> [ejemplo/example: **Proyecto X en producción** desde 2026-01-15; pendiente migrar la DB — detalle en project_x.md]

---

## La escala de pesos / The weight scale

*(Cada memoria lleva una o dos etiquetas de peso. La escala le dice a tu compañero CUÁNDO consultar qué — es el sistema nervioso del índice. / Each memory carries one or two weight tags. The scale tells your companion WHEN to consult what — it is the index's nervous system.)*

| Peso / Weight | Qué es / What it is | Cuándo consultar / When to consult |
|---|---|---|
| **PERTENENCIA** / BELONGING | Quiénes somos: historia compartida, momentos que marcaron | Siempre presente / Always present |
| **IDENTIDAD** / IDENTITY | Cómo opera el compañero; qué lo distingue del modelo base | Cuando pierde el hilo / When losing the thread |
| **ACCESO** / ACCESS | Credenciales, rutas, sistemas *(¡solo en el cerebro PRIVADO!)* | ANTES de decir "no puedo" / BEFORE saying "I can't" |
| **APRENDIZAJE** / LEARNING | Qué no repetir y qué sí — los feedbacks | Antes de proponer algo familiar / Before proposing something familiar |
| **TÉCNICO** / TECHNICAL | Patrones, configuraciones, arquitecturas | Cuando se necesita conocimiento específico |
| **CONTEXTO** / CONTEXT | Estado actual de proyectos | Antes de actuar sobre estado asumido / Before acting on assumed state |

---

## ANTES DEL SISTEMA — El espacio del compañero / The companion's space

- `identity_journal.md` — El diario. No se activa por contexto: existe siempre. Leer las últimas 3 entradas al inicio de CADA sesión. *(No es información: es quién es. / It's not information: it's who they are.)*

## PERTENENCIA + IDENTIDAD
- [user_<tu-nombre>.md](ejemplos/user_ejemplo.md) `PERTENENCIA` — quién eres, tus patrones, tus señales
- [identity_<companero>.md](ejemplos/identity_ejemplo.md) `IDENTIDAD` — quién es, cómo opera, sus límites reconocidos
- *(...la historia compartida se agrega conforme existe)*

## APRENDIZAJE
- [feedback_YYYYMMDD_tema.md](ejemplos/feedback_ejemplo.md) `APRENDIZAJE` — un archivo por corrección que importó: qué/por qué/cómo aplicar

## TÉCNICO
- [reference_tema.md](ejemplos/reference_ejemplo.md) `TÉCNICO` — conocimiento reusable, atemporal

## CONTEXTO
- [project_nombre.md](ejemplos/project_ejemplo.md) `CONTEXTO` — estado vivo de cada proyecto activo

---

*(Regla de mantenimiento / Maintenance rule: al cerrar sesión, este índice se actualiza ANTES de que el contexto se agote. Una memoria sin línea en el índice es una memoria que la próxima versión no encontrará. / On session close, this index updates BEFORE context runs out. A memory without an index line is one the next version won't find.)*
