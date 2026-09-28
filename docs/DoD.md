# Definition of Done (6 criterios)

Cada criterio debe ser verificable (sí/no) y estar ligado a un atributo de calidad.

| # | Criterio | Atributo ISO 25010 | Evidencia |
|---|---|---|---|
| 1 | Cada criterio de aceptación de la historia tiene al menos una prueba automatizada en `tests/` y todas pasan. | Adecuación funcional / Corrección funcional | **Automática:** `pytest -v` en el workflow lista cada prueba en verde. La tarjeta del tablero indica qué prueba cubre cada criterio. |
| 2 | Cada entrada inválida descrita en la especificación (valor negativo, tipo de afiliado desconocido) lanza `ValueError` y tiene su prueba con `pytest.raises(ValueError)`. | Capacidad de interacción / Protección contra errores del usuario | **Automática:** pruebas de casos inválidos en `tests/test_citas.py`, ejecutadas en cada push. |
| 3 | La cobertura de sentencias de `src/` es ≥ 80 %. | Mantenibilidad / Capacidad de ser probado | **Automática:** step `pytest --cov=src --cov-fail-under=80` del workflow. Si la cobertura es menor, el CI queda en rojo. |
| 4 | El workflow "CI de calidad" está en verde en el último commit de `main`. | Fiabilidad / Ausencia de fallos | **Automática:** check verde en la pestaña Actions (`gh run list --limit 1` muestra `success`). |
| 5 | El cambio fue revisado y aprobado por el otro integrante (no por su autor) y cumple las 5 reglas de `docs/reglas_codificacion.md`. | Mantenibilidad / Analizabilidad | **Semiautomática:** aprobación registrada en el pull request. GitHub puede exigirla con una regla de protección de la rama `main` (1 aprobación obligatoria). Las 5 reglas se marcan como lista de chequeo en la descripción del PR. |
| 6 | No hay secretos (tokens, contraseñas) ni datos reales de pacientes en el código, las pruebas ni los datos de ejemplo. Las pruebas usan solo datos ficticios. | Seguridad / Confidencialidad | **Automática:** secret scanning con push protection de GitHub activado en la configuración de seguridad del repositorio; un push con un secreto queda bloqueado. Los datos ficticios se revisan en el PR (criterio 5). |

## Cómo se usa

- Una tarjeta pasa a **Hecho** solo si los 6 criterios responden "sí". Si uno responde "no", la tarjeta no está terminada, aunque el código funcione.
- Los criterios 1 a 4 los verifica la máquina en cada push: el workflow `.github/workflows/ci.yml` es la puerta de calidad. El 6 lo verifica GitHub al recibir el push. El 5 necesita una persona, pero deja registro en el PR.
- El problema de los viernes no está en la DoD porque la DoD dice cuándo un cambio está terminado, no cuándo se despliega. Ese control está en la política de salida de "Listo para desplegar" (`docs/politicas_kanban.md`).
