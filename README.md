# Taller: Auditoría de calidad de un equipo ágil

Curso: Estándares y Métricas de Calidad de Software · Tema: cumplimiento de estándares en Scrum, Kanban, XP y DevOps.

## Caso
Una startup desarrolla una app de citas médicas. Entrega cada 2 semanas, tiene defectos que llegan a producción, pruebas manuales y despliega los viernes. Su equipo debe demostrar calidad con evidencia verificable.

## Requisitos (todo en línea, sin instalar nada)
- Cuenta gratuita de GitHub (y Trello o GitHub Projects para el tablero).
- Este repositorio: use **Use this template** o **Fork** y abra **Codespaces** (o edite en el navegador con la tecla `.`).

## Bloques
| Bloque | Min | Qué hacer | Archivo / entregable |
|---|---|---|---|
| 1. Diagnóstico | 15 | Asociar problemas del caso con atributos de ISO/IEC 25010:2023 | `docs/atributos_iso25010.md` |
| 2. Scrum y Kanban | 15 | Redactar la Definition of Done (6 criterios) y montar un tablero con límites WIP y políticas por columna | `docs/DoD.md`, `docs/politicas_kanban.md`, captura del tablero |
| 3. XP | 15 | Escribir 3 pruebas unitarias antes de implementar (TDD) y proponer 5 reglas de codificación | `tests/test_citas.py`, `src/citas.py`, `docs/reglas_codificacion.md` |
| 4. DevOps | 20 | Completar el workflow para que ejecute pruebas y falle si la cobertura es menor al 80 % | `.github/workflows/ci.yml` |
| 5. Métricas | 10 | Calcular las 4 métricas DORA con los datos simulados y elegir 4 métricas por enfoque | `docs/metricas.md` |
| 6. Socialización | 15 | Sustentación de 3 minutos del plan de cumplimiento | Exposición |

## Entrega
Un enlace al repositorio con el último commit y la ejecución del workflow en verde (pestaña **Actions**).

## Pistas para el bloque 3 (TDD)
1. Lea la especificación en `src/citas.py`.
2. Escriba primero las pruebas (deben fallar).
3. Implemente hasta que pasen.
4. Ejecute en la terminal de Codespaces: `pip install -r requirements.txt && pytest --cov=src`.
