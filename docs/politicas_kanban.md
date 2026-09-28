# Tablero Kanban: políticas por columna

Enlace o captura del tablero: _______

Equipo: 2 personas (David y Samuel Ossa Escobar). Tablero en GitHub Projects (ver `docs/tablero.md`).

| Columna | Límite WIP | Política de entrada | Política de salida | Evidencia |
|---|---|---|---|---|
| Por hacer | 4 | La tarjeta tiene historia de usuario, criterios de aceptación verificables (Dado / Cuando / Entonces) y el campo "Atributo ISO 25010" diligenciado. | La tarjeta tiene responsable asignado y ese responsable no tiene otra tarjeta en "En desarrollo". | Campos de la tarjeta en GitHub Projects (Assignees, Atributo ISO 25010). |
| En desarrollo | 2 | = salida de "Por hacer": responsable asignado sin otra tarjeta en desarrollo. | Las pruebas se escribieron primero (commit `test:` anterior al commit `feat:`), `pytest --cov=src --cov-fail-under=80` pasa en local y hay un PR abierto enlazado a la tarjeta. | Historial de commits (`git log --oneline`) y PR enlazado. |
| En revisión / pruebas | 1 | = salida de "En desarrollo": PR abierto y enlazado, con el workflow ejecutándose. | Workflow en verde, PR aprobado por el otro integrante, los 6 criterios de la DoD marcados en el PR y PR fusionado en `main`. | Check verde en Actions, aprobación del PR y lista de chequeo de la DoD. |
| Listo para desplegar | 2 | = salida de "En revisión / pruebas": cambio fusionado en `main` con la DoD completa. | **Política anti-viernes:** se despliega solo de lunes a jueves y antes de las 13:00. El despliegue queda registrado (fecha de commit, fecha de despliegue, resultado) y se conoce la versión anterior para revertir. | Registro en `datos/despliegues.csv`. `scripts/dora.py` muestra los despliegues por día de la semana: debe haber 0 en viernes, sábado o domingo. |
| Hecho | Sin límite | = salida de "Listo para desplegar": desplegado dentro de la ventana y registrado. | Sin fallo reportado en las 24 h siguientes al despliegue. Si aparece un fallo, se crea una tarjeta urgente (ver excepción). | Registro de despliegues con `exitoso = si`. |

## Por qué estos límites (equipo de 2 personas)

- **En desarrollo = 2:** una tarjeta por persona. Nadie tiene dos trabajos a medias.
- **En revisión / pruebas = 1:** con 2 personas la revisión es el cuello de botella natural. Si ya hay una tarjeta esperando revisión, quien termine primero revisa antes de tomar otra tarjeta: primero se termina, después se empieza.
- **Listo para desplegar = 2:** recibe lo que se termina entre el jueves a las 13:00 y el lunes (por la política anti-viernes) sin bloquear la revisión.
- **Por hacer = 4:** el doble del equipo. Alcanza para no quedarse sin trabajo y evita un backlog largo sin refinar.

## Política anti-viernes: por qué lunes a jueves antes de las 13:00

- En `datos/despliegues.csv` fallaron los 3 despliegues hechos en viernes y el único hecho en sábado, cuyo commit fue del viernes a las 23:28. De lunes a jueves no falló ninguno de 13 despliegues.
- La recuperación promedio de los fallos fue de 4,5 h. Si un despliegue sale a las 13:00 y falla, la recuperación promedio termina hacia las 17:30, dentro de la jornada y con el equipo disponible. Un fallo el viernes en la tarde se recupera con el equipo ya fuera.

## Excepción: clase de servicio urgente

Revertir a la versión anterior, o corregir un fallo en producción con la etiqueta `urgente`, puede hacerse cualquier día. Aun así cumple la DoD (CI en verde) y queda registrado. Prohibir también la corrección el viernes empeoraría el tiempo de recuperación, que es justamente lo que se quiere bajar.
