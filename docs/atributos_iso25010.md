# Bloque 1: problemas del caso y atributos ISO/IEC 25010:2023

Atributos: adecuación funcional, eficiencia de desempeño, compatibilidad, capacidad de interacción, fiabilidad, seguridad, mantenibilidad, flexibilidad, seguridad operacional (safety).

| Problema del caso | Atributo afectado | Subcaracterística | Métrica propuesta (fórmula) | Meta verificable (sí/no) | Evidencia / fuente del dato |
|---|---|---|---|---|---|
| Defectos que llegan a producción | Fiabilidad | Ausencia de fallos | Tasa de defectos escapados = defectos reportados en producción / (defectos reportados en producción + defectos detectados antes de producción) × 100 | ¿Es ≤ 10 % en el sprint? | Tarjetas del tablero con etiqueta `defecto-produccion` o `defecto-pre`, contadas al cierre de cada sprint |
| Pruebas solo manuales | Mantenibilidad | Capacidad de ser probado | Cobertura de sentencias = sentencias de `src/` ejecutadas por pruebas automatizadas / sentencias ejecutables de `src/` × 100 | ¿Es ≥ 80 % en cada ejecución del CI? | Reporte de `pytest --cov=src` en la pestaña Actions (el workflow falla si es menor) |
| Despliegues los viernes sin control | Flexibilidad | Instalabilidad | Tasa de fallo de despliegues = despliegues fallidos / despliegues totales × 100, calculada en total y por día de la semana | ¿Es ≤ 10 % en total y hay 0 despliegues en viernes, sábado o domingo? | `datos/despliegues.csv` procesado con `scripts/dora.py` y `datos/metricas_dora.xlsx` |
| Propio de una app médica: un paciente escribe como motivo de consulta un síntoma de alarma (dolor en el pecho, dificultad para respirar) y la app le asigna la primera cita libre a varios días sin indicarle que acuda a urgencias | Seguridad operacional (safety) | Advertencia de peligro | Cobertura de advertencias de alarma = síntomas de la lista de alarma que muestran la advertencia de urgencias / síntomas de la lista de alarma × 100 | ¿Es 100 %? | Prueba automatizada parametrizada con la lista de síntomas de alarma (lista validada por personal médico), ejecutada en el CI |

## Notas para la sustentación

- Se usan los nombres de la versión 2023. Cambios frente a ISO/IEC 25010:2011 que aparecen en esta tabla:
  - *Madurez* pasó a llamarse **ausencia de fallos** (dentro de fiabilidad).
  - *Portabilidad* pasó a llamarse **flexibilidad**; instalabilidad quedó dentro de ella.
  - **Seguridad operacional (safety)** es una característica nueva: protege a las personas de daños. Es distinta de **seguridad (security)**, que protege la información.
  - *Usabilidad* pasó a llamarse **capacidad de interacción** (se usa en la DoD).
- Desplegar es instalar el producto en el entorno de producción. Por eso el problema de los viernes se asocia a instalabilidad y se mide con la tasa de fallo de despliegues. Con los datos del taller: los 3 despliegues hechos en viernes fallaron (ver `docs/metricas.md`).
- La cuarta fila es propia del dominio médico: un error de la app no solo produce una cita mal asignada, puede retrasar la atención de una urgencia. Por eso se clasifica como seguridad operacional y no como adecuación funcional.
