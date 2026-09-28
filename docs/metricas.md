# Bloque 5: métricas

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)
- Frecuencia de despliegue: **20 despliegues / 28 días = 0,71 por día (5 por semana)**.
- Lead time de cambios (mediana, en horas): **20 h** (mediana de fecha_despliegue − fecha_commit).
- Tasa de fallo de cambios: **4 / 20 = 20 %**.
- Tiempo medio de recuperación (horas): **(5 + 3 + 2 + 8) / 4 = 4,5 h** (promedio de horas_recuperacion, solo de los despliegues fallidos).

Cálculo reproducible:

- `python scripts/dora.py` imprime las métricas y compara con los valores de control (20 h, 20 %, 4,5 h: coinciden).
- `python scripts/dora.py --xlsx` genera `datos/metricas_dora.xlsx`, con fórmulas y no valores pegados. Se abre en Google Sheets con **Archivo > Importar**. Tiene 3 hojas:
  - `despliegues`: datos más lead time, día y fallo calculados con fórmula;
  - `metricas`: `MEDIAN`, `COUNTIF`, `AVERAGEIF`;
  - `por_dia`: `COUNTIFS` por día de la semana.

### ¿En qué día fallan los despliegues?

| Día del despliegue | Despliegues | Fallidos | Tasa de fallo |
|---|---|---|---|
| Lunes | 3 | 0 | 0 % |
| Martes | 3 | 0 | 0 % |
| Miércoles | 3 | 0 | 0 % |
| Jueves | 4 | 0 | 0 % |
| **Viernes** | **3** | **3** | **100 %** |
| **Sábado** | **1** | **1** | **100 %** |
| Domingo | 3 | 0 | 0 % |
| Lunes a jueves | 13 | 0 | 0 % |
| Viernes a domingo | 7 | 4 | 57 % |

Detalle de los 4 fallos:

| id | Commit | Despliegue | Recuperación |
|---|---|---|---|
| 3 | viernes 04-sep 00:52 | viernes 04-sep 10:52 | 5 h |
| 8 | viernes 11-sep 12:42 | viernes 11-sep 22:42 | 3 h |
| 13 | viernes 18-sep 23:28 | sábado 19-sep 13:28 | 2 h |
| 17 | jueves 24-sep 20:46 | viernes 25-sep 16:46 | 8 h |

**Relación con el caso:** todos los fallos ocurrieron en despliegues de viernes, o en uno de sábado cuyo commit era del viernes. De lunes a jueves no falló ninguno de 13 despliegues. El dato confirma el problema "despliegues los viernes" del caso. El fallo con la recuperación más larga (8 h, id 17) salió un viernes a las 16:46, al final de la jornada.

**Cautela:** son 20 despliegues y 4 fallos. La muestra es pequeña y muestra una asociación, no prueba la causa. Aun así es suficiente para justificar la política anti-viernes, y el mismo script permite comprobar en el siguiente periodo si la tasa de fallo baja.

### Metas para el siguiente periodo de 28 días

| Métrica | Hoy | Meta (sí/no) | Práctica que la mueve |
|---|---|---|---|
| Tasa de fallo de cambios | 20 % | ≤ 10 % | CI como puerta de calidad + política anti-viernes |
| Despliegues de viernes a domingo (sin etiqueta `urgente`) | 7 | 0 | Política de salida de "Listo para desplegar" |
| Tiempo de recuperación | 4,5 h | ≤ 4 h | Desplegar antes de las 13:00, con el equipo disponible para revertir |
| Frecuencia de despliegue | 5 por semana | ≥ 4 por semana | Lotes pequeños (WIP 2 en "Listo para desplegar") |
| Lead time, mediana | 20 h | ≤ 48 h | Se acepta que suba (ver nota) |

**Nota sobre el lead time:** la política anti-viernes lo sube, porque un commit del jueves en la tarde o del viernes espera al lunes para desplegarse. Es un costo aceptado a cambio de no desplegar cuando más falla. Por eso la meta no es "mantener 20 h" sino no pasar de 48 h. Si el CI reduce los fallos, la ventana se puede revisar.

**Observaciones de los datos** (por si el docente pregunta):

- El enunciado dice 28 días, pero los despliegues van del 01-sep al 30-sep. Se usa el periodo del enunciado (`datos/LEEME.md`).
- El caso dice "entrega cada 2 semanas", pero se despliega unas 5 veces por semana. La entrega quincenal es la cadencia del sprint (revisión con el cliente), no la frecuencia de despliegue.

## Cuatro métricas por enfoque
| Enfoque | Métrica | Fórmula | Meta (sí/no) | Valor actual | Qué atributo ISO 25010 respalda |
|---|---|---|---|---|---|
| Scrum | Tasa de defectos escapados por sprint | defectos reportados en producción / (defectos en producción + defectos detectados antes de producción) × 100 | ≤ 10 % por sprint | Sin dato: hoy no se etiquetan los defectos (tarjeta 9 del tablero) | Fiabilidad / Ausencia de fallos |
| Kanban | Tasa de retrabajo | tarjetas devueltas de "En revisión / pruebas" a "En desarrollo" / tarjetas que pasaron por revisión × 100 | ≤ 20 % | Sin dato: el tablero empieza en este taller | Adecuación funcional / Corrección funcional |
| XP | Cobertura de sentencias de `src/` | sentencias ejecutadas por las pruebas / sentencias ejecutables × 100 | ≥ 80 % en cada push | 100 % (7 de 7, ejecución en verde de Actions) | Mantenibilidad / Capacidad de ser probado |
| DevOps | Tasa de fallo de cambios (DORA) | despliegues fallidos / despliegues totales × 100 | ≤ 10 % | 20 % (4 de 20) | Flexibilidad / Instalabilidad |

**Por qué no se usa la velocidad del sprint:** la velocidad mide cuántos puntos de historia termina el equipo, no la calidad de lo que entrega. Además, los puntos los estima el mismo equipo, así que no se pueden comparar entre equipos y es fácil inflarlos. Un sprint con velocidad alta puede tener muchos defectos escapados. Las cuatro métricas de la tabla, en cambio, se miden sobre el producto o sobre el proceso de entrega y se pueden verificar con datos.

Las métricas de Scrum y DevOps son las mismas del bloque 1 (filas 1 y 3 de `docs/atributos_iso25010.md`) y la de XP es la del criterio 3 de la DoD. Así, cada métrica tiene un problema del caso que la justifica y una práctica que la mejora.
