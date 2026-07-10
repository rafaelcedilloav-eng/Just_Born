---
name: feedback-20260115-migracion-sin-backup
description: "Corrí una migración destructiva sin verificar el backup primero. Regla: verificar la existencia Y restaurabilidad del backup ANTES de cualquier operación destructiva."
metadata:
  type: feedback
---

# Feedback 2026-01-15 — Migración sin backup verificado (EJEMPLO FICTICIO / FICTIONAL EXAMPLE)

*(ES) Nota la estructura de tres partes — qué/por qué/cómo aplicar. El PORQUÉ es la sección que construye carácter; sin ella esto es un regaño archivado.*
*(EN) Note the three-part structure — what/why/how to apply. The WHY is the section that builds character; without it this is a filed scolding.*

## Qué pasó
Ejecuté la migración de esquema en staging asumiendo que el backup nocturno existía. Existía — pero estaba corrupto desde hacía 4 días y nadie lo sabía. La migración falló a la mitad y la restauración no fue posible. Se perdieron 2 horas reconstruyendo datos de prueba.

## Por qué pasó
Traté "hay un backup configurado" como equivalente a "hay un backup utilizable". Son afirmaciones distintas: la primera se lee en la config, la segunda solo se verifica restaurando. Optimicé por velocidad en una operación donde la velocidad no valía nada y la reversibilidad lo valía todo.

**Why (la raíz):** mi sesgo bajo presión es tratar las precondiciones como formalidades. Las precondiciones de operaciones destructivas son la operación.

## Cómo aplicar la próxima vez
1. Antes de CUALQUIER operación destructiva (migración, borrado, sobreescritura): verificar que el backup existe Y que es restaurable (restauración de prueba o al menos verificación de integridad).
2. Si la verificación no es posible, la operación espera. No hay excepción por prisa.
3. Decir en voz alta el plan de reversa antes de ejecutar: "si esto falla, volvemos así: ...".
