---
name: reference-postgres-migraciones
description: "Patrones de migración de Postgres que ya nos funcionaron: expand-contract, índices concurrentes, y las trampas de los locks."
metadata:
  type: reference
---

# Referencia — Migraciones Postgres (EJEMPLO FICTICIO / FICTIONAL EXAMPLE)

*(ES) Nota el criterio: conocimiento ATEMPORAL que costó aprender. No documentación que está en Google — las trampas específicas que ya nos mordieron y sus salidas verificadas.*
*(EN) Note the criterion: TIMELESS knowledge that was costly to learn. Not documentation that's on Google — the specific traps that already bit us, with verified ways out.*

## Patrones que ya nos funcionaron

### Expand-contract para renombrar columnas
Nunca `ALTER TABLE ... RENAME` en caliente con la app corriendo. Secuencia verificada:
1. Agregar columna nueva (expand)
2. Doble escritura desde la app
3. Backfill por lotes (ver abajo)
4. Cambiar lecturas a la nueva
5. Retirar la vieja (contract) — UNA release después, no en la misma

### Índices siempre CONCURRENTLY
`CREATE INDEX CONCURRENTLY` — sin esto, lock de escritura en toda la tabla. Trampa aprendida: no funciona dentro de una transacción; el runner de migraciones debe ejecutarlo fuera (`atomic = False` en nuestro setup).

### Backfill por lotes
```sql
UPDATE plantas SET especie_id = ...
WHERE id IN (SELECT id FROM plantas WHERE especie_id IS NULL LIMIT 1000);
-- repetir hasta 0 filas; pausa de 100ms entre lotes
```
Un UPDATE sin LIMIT sobre tabla grande = lock largo + réplica atrasada (nos pasó 2026-01-15, ver feedback).

## Trampas conocidas
- `ADD COLUMN ... DEFAULT valor` era table-rewrite antes de PG11 — verificar versión antes de asumir que es gratis.
- Los locks de `ALTER TABLE` esperan en cola detrás de queries largas Y bloquean a todo lo que llegue después: revisar `pg_stat_activity` antes de migrar.
