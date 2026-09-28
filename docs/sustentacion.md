# Sustentación: plan de cumplimiento (3 minutos)

Equipo: David y Samuel Ossa Escobar.
Repositorio: https://github.com/daviid0611/auditoria-calidad-agil

## 1. Guion

Ritmo de referencia: unas 75 palabras cada 30 segundos. Ensayen con cronómetro. Si se pasan, recorten los ejemplos entre paréntesis.

### 0:00 a 0:30. Diagnóstico (David)

> La startup entrega una app de citas médicas cada dos semanas, con defectos en producción, pruebas manuales y despliegues los viernes. Con ISO/IEC 25010, versión 2023, convertimos cada síntoma en un atributo medible. Los defectos afectan la fiabilidad, en ausencia de fallos. Las pruebas manuales, la mantenibilidad, en capacidad de ser probado. Los despliegues del viernes, la flexibilidad, en instalabilidad. Y agregamos uno del dominio médico, seguridad operacional: si la app no advierte un síntoma de alarma, puede retrasar una urgencia.

Pantalla: `docs/atributos_iso25010.md`.

### 0:30 a 2:30. Cadena problema, práctica, evidencia, métrica

**Cadena 1. XP (David, 0:30 a 1:00)**

> Problema: pruebas solo manuales. Práctica de XP: TDD. El historial lo demuestra: el commit "test: pruebas en rojo" está antes de "feat: implementación en verde". Usamos `pytest.raises(ValueError)` y no `Exception`, porque `NotImplementedError` también es una excepción y daría un verde falso. (Y probamos el contributivo con 1001 pesos: sin redondeo da 100,10000000000001.) Métrica: cobertura de sentencias. Hoy es 100 % y la meta mínima es 80 %.

Pantalla: `git log --oneline` y `tests/test_citas.py`.

**Cadena 2. DevOps (David, 1:00 a 1:30)**

> Problema: defectos que llegan a producción. Práctica de DevOps: un workflow de GitHub Actions como puerta de calidad. Ejecuta las pruebas y falla si la cobertura baja del 80 %. La evidencia son dos ejecuciones: la primera en rojo, porque la función aún no estaba implementada, y la de la implementación en verde. La puerta bloquea de verdad. Métrica: tasa de defectos escapados por sprint, con meta de 10 % o menos.

Pantalla: pestaña Actions con la [ejecución en rojo](https://github.com/daviid0611/auditoria-calidad-agil/actions/runs/36473636508) y la [ejecución en verde](https://github.com/daviid0611/auditoria-calidad-agil/actions/runs/36473951320).

**Cadena 3. Scrum (Samuel, 1:30 a 2:00)**

> Problema: se daba por terminado código que después fallaba en producción. Práctica de Scrum: una Definition of Done de seis criterios que se responden con sí o no, cada uno ligado a un atributo. Cuatro los verifica la máquina en cada push: pruebas por criterio de aceptación, casos inválidos con ValueError, cobertura y CI en verde. Los otros dos son la revisión del compañero y que no haya secretos ni datos reales de pacientes. Si uno dice "no", la tarjeta no pasa a Hecho.

Pantalla: `docs/DoD.md`.

**Cadena 4. Kanban (Samuel, 2:00 a 2:30)**

> Problema: despliegues los viernes. Práctica de Kanban: un tablero en GitHub Projects con límites WIP para dos personas, 2 en desarrollo y 1 en revisión, y políticas encadenadas: la salida de una columna es la entrada de la siguiente. La política clave es que de "Listo para desplegar" solo se sale de lunes a jueves, antes de la una de la tarde. Así, si algo falla, la recuperación promedio de 4,5 horas termina dentro de la jornada. Métrica: despliegues de viernes a domingo, con meta cero.

Pantalla: captura del tablero y `docs/politicas_kanban.md`.

### 2:30 a 3:00. Resultados DORA y metas (Samuel)

> Con los datos de 28 días: 5 despliegues por semana, lead time mediano de 20 horas, 20 % de fallos y 4,5 horas de recuperación. El hallazgo: los 4 fallos fueron en viernes o sábado; de lunes a jueves, cero de trece. Metas: fallos en 10 % o menos, cero despliegues de viernes a domingo y recuperación de 4 horas o menos. Aceptamos que el lead time suba, sin pasar de 48 horas. Todo se reproduce con el script y la hoja de cálculo del repositorio.

Pantalla: `datos/metricas_dora.xlsx`, hoja `por_dia`.

## 2. Por qué de cada decisión

### Bloque 1: diagnóstico

- **Nombres de ISO/IEC 25010:2023 y no de 2011.** La versión vigente cambió varios nombres: *madurez* pasó a ser **ausencia de fallos**, *usabilidad* pasó a ser **capacidad de interacción**, *portabilidad* pasó a ser **flexibilidad**, y se agregó **seguridad operacional (safety)**. Usar los nombres viejos muestra que no se consultó la versión que pide el taller.
- **Despliegues del viernes en flexibilidad / instalabilidad.** Desplegar es instalar el producto en el entorno de producción. La instalabilidad mide qué tan bien se instala en un entorno dado, y la tasa de fallo de despliegues lo mide directamente. No se eligió fiabilidad porque esa ya cubre los defectos del código (fila 1). Aquí el problema no es el código sino cuándo y cómo se instala.
- **Fila propia en seguridad operacional (safety) y no en seguridad.** Seguridad (security) protege la información. Seguridad operacional protege a las personas de daños. Una cita asignada a varios días para alguien con dolor en el pecho es un daño a una persona, no a un dato.
- **Cada métrica tiene meta y fuente.** Una métrica sin meta no se puede responder con sí o no, y una sin fuente no se puede auditar.

### Bloque 2: Scrum y Kanban

- **DoD de 6 criterios, 4 verificados por el CI.** Lo que verifica la máquina no depende de la memoria ni de la buena voluntad de nadie. El criterio 5 (revisión del compañero) no se puede automatizar del todo, pero deja registro en el PR.
- **El viernes no está en la DoD.** La DoD define cuándo un cambio está terminado. Cuándo se despliega es una política del flujo, así que va en la columna "Listo para desplegar" del Kanban.
- **Límites WIP para 2 personas: 4 / 2 / 1 / 2.**
  - 2 en desarrollo: una tarjeta por persona, nadie con dos trabajos a medias.
  - 1 en revisión: si hay algo esperando revisión, quien termine primero revisa antes de empezar otra cosa.
  - 2 en "Listo para desplegar": absorbe lo que se acumula entre el jueves a las 13:00 y el lunes.
  - 4 en "Por hacer": el doble del equipo.
- **Políticas encadenadas.** La salida de cada columna es la entrada de la siguiente. Así ninguna tarjeta queda "entre columnas" sin dueño ni condición.
- **Por qué antes de las 13:00.** La recuperación promedio fue de 4,5 h: 13:00 + 4,5 h = 17:30, dentro de la jornada.
- **Excepción urgente.** Una reversión o corrección de un fallo sí puede salir en viernes. Prohibirla aumentaría el tiempo de recuperación, que es lo que se quiere bajar.
- **GitHub Projects solo muestra el límite WIP, no lo impide.** Por eso el límite es una política del equipo y la captura sirve de evidencia: una columna resaltada indica que se incumplió.

### Bloque 4: CI (hecho antes que el bloque 3)

- **CI antes que la implementación.** Primero se demostró que la puerta bloquea: la ejecución quedó en rojo porque `calcular_copago` lanzaba `NotImplementedError`. Una puerta que nunca se vio en rojo no prueba nada.
- **`python-version: "3.12"` entre comillas.** YAML lee un número sin comillas como decimal: `3.10` se convertiría en `3.1`. Con comillas la versión es texto exacto.
- **`actions/setup-python@v5`.** Se fija la versión mayor de la acción para que el workflow no cambie solo si sale una versión incompatible.
- **`--cov-fail-under=80`.** Convierte la cobertura en condición: si baja del 80 %, pytest termina con error y el job queda en rojo. **`--cov-report=term-missing`** solo agrega al registro qué líneas no se cubrieron.
- **Dato clave del run rojo:** la cobertura era 100 % y aun así falló. La puerta tiene dos condiciones, que las pruebas pasen y que la cobertura sea ≥ 80 %, y ninguna reemplaza a la otra.

### Bloque 3: XP / TDD

- **Commit en rojo antes del verde.** Es la evidencia de que las pruebas se escribieron primero. `git log` muestra `test: pruebas en rojo (TDD)` antes de `feat: implementación en verde`. Con las pruebas nuevas la salida fue `6 failed`, y tras implementar, `6 passed`.
- **`pytest.raises(ValueError)` y no `Exception`.** `NotImplementedError` hereda de `Exception`. Con `Exception`, las pruebas de casos inválidos habrían pasado sin que la función existiera: un verde falso.
- **Contributivo con 1001 y 1234.56, comparando con `==`.**
  - `1001 * 0.10` da `100.10000000000001` en punto flotante. Si falta el `round`, la prueba falla.
  - Pero `1001 * 10 / 100` da `100.1` exacto, así que con esa forma de calcular, 1001 no detectaría la falta de redondeo. Por eso se agregó `1234.56`, que da `123.456` o `123.45599999999999` según cómo se calcule y falla siempre sin redondeo.
  - `pytest.approx` no se usó porque aceptaría el valor sin redondear.
  - Se comprobó con una prueba de mutación: al quitar el `round` en una copia del código fallaron las 2 pruebas de contributivo.
- **Diccionario `PORCENTAJE_COPAGO`.** El mismo diccionario sirve para calcular y para validar (`tipo_afiliado not in PORCENTAJE_COPAGO`), así que no pueden desincronizarse. Agregar un tipo de afiliado es cambiar una línea. Con `if/elif` habría que tocar dos sitios.
- **Validar primero y calcular después.** Los dos `raise ValueError` van al inicio, antes de cualquier cálculo (regla 4). El `round(..., 2)` va en el `return` porque la especificación pide redondear el resultado, no los pasos intermedios.
- **`float` y no `Decimal`.** La firma de la plantilla usa `float` y la especificación pide redondear a 2 decimales. Para un sistema de cobro real, `Decimal` evitaría los errores de punto flotante. Se deja como mejora y no se cambia la firma dada.

### Bloque 5: métricas

- **Script fuera de `src/`.** El CI mide cobertura con `--cov=src`. Si el script estuviera en `src/` sin pruebas, bajaría la cobertura y rompería la puerta por algo que no es código del producto.
- **Solo biblioteca estándar para calcular.** `openpyxl` se importa únicamente con `--xlsx` y no está en `requirements.txt`, para no instalar en el CI algo que el CI no usa.
- **Frecuencia sobre 28 días.** Es el periodo del enunciado (`datos/LEEME.md`), aunque las fechas van del 01 al 30 de septiembre.
- **Mediana para el lead time.** Hay valores de 48 y 52 h que subirían el promedio. La mediana (20 h) representa el caso típico.
- **Recuperación solo de los fallidos.** Los despliegues exitosos tienen `horas_recuperacion = 0`. Si se incluyeran, el promedio daría 18 / 20 = 0,9 h, un valor falso porque esos despliegues no se recuperaron de nada. Lo correcto es 18 / 4 = 4,5 h.
- **Hoja de cálculo con fórmulas.** Si cambian los datos, los resultados se recalculan, y cualquiera puede auditar el cálculo celda por celda. El día de la semana se calcula con `WEEKDAY` (tipo 2, lunes = 1) + `CHOOSE`, que funciona igual con Google Sheets en español o en inglés (`TEXT` con formato "dddd" depende del idioma). Las fórmulas se verificaron recalculando en Excel: 0 errores y los mismos valores del script.
- **No se usó la velocidad del sprint.** Mide puntos terminados, no calidad. Además los puntos son una estimación del propio equipo y no se pueden comparar.

### Punto débil conocido (mejor decirlo antes de que lo pregunten)

- **Commits directos a `main`.** La DoD pide revisión del compañero en el PR, pero los commits del taller fueron directos a `main`, porque la guía pedía un commit por paso en un orden fijo para que el rojo y el verde del TDD se vieran en el historial. Para el trabajo del producto, el siguiente paso es activar la protección de la rama `main` con 1 aprobación obligatoria.

## 3. Preguntas probables del docente

**1. ¿Por qué clasificaron los despliegues del viernes como flexibilidad y no como fiabilidad?**
Porque desplegar es instalar el producto en producción. En ISO/IEC 25010:2023, la instalabilidad está dentro de flexibilidad (antes portabilidad) y mide qué tan bien se instala en un entorno dado. La fiabilidad ya la usamos para los defectos del código. El patrón que muestran los datos está en el día del despliegue: de lunes a jueves fallaron 0 de 13 despliegues y en viernes, 3 de 3.

**2. En la ejecución roja la cobertura era 100 %. ¿Para qué sirve entonces la cobertura?**
La cobertura dice qué líneas ejecutaron las pruebas, no si el resultado es correcto. Esa ejecución lo demuestra: 100 % de cobertura y aun así falló, porque la prueba esperaba 100000 y la función lanzaba `NotImplementedError`. Por eso la puerta tiene dos condiciones: que las pruebas pasen y que la cobertura sea ≥ 80 %. La cobertura sirve para detectar código que ninguna prueba ejecuta.

**3. ¿Cómo demuestran que hicieron TDD y que sus pruebas sirven?**
Con tres evidencias:
- El orden de los commits: `test: pruebas en rojo (TDD)` va antes de `feat: implementación en verde`, con `6 failed` y luego `6 passed`.
- Las pruebas de casos inválidos usan `ValueError` y no `Exception`, así que no pasaban con `NotImplementedError`.
- Una prueba de mutación: al quitar el `round`, las 2 pruebas de contributivo fallaron. Por eso usamos 1234.56 además de 1001: con `valor * 10 / 100`, 1001 da `100.1` exacto y no detectaría la falta de redondeo.

**4. ¿Por qué la mediana para el lead time y solo los fallidos para la recuperación?**
- El lead time tiene valores de 48 y 52 h que suben el promedio. La mediana, 20 h, describe el caso típico.
- El tiempo de recuperación mide cuánto se tarda en recuperarse de un fallo. Los exitosos tienen 0 h porque no hubo nada que recuperar, y si se incluyeran el promedio bajaría a 0,9 h, lo cual es falso. Con solo los 4 fallidos da 18 / 4 = 4,5 h. Las dos cifras coinciden con los valores de control.

**5. Prohibir desplegar los viernes, ¿no esconde el problema en vez de resolverlo? ¿Y no empeora el lead time?**
Sí empeora el lead time: un commit del viernes espera al lunes. Por eso la meta es no pasar de 48 h, no mantener 20 h. La política no reemplaza la solución, reduce el riesgo mientras la solución madura. La causa de fondo la atacan el CI y el TDD, que detectan el defecto antes de desplegar. Además la política tiene excepción para reversiones y correcciones urgentes, para no empeorar la recuperación. Y la vamos a medir: si en el próximo periodo la tasa de fallo baja a 10 % o menos, se puede revisar la ventana. También reconocemos que con 20 despliegues y 4 fallos hay una asociación, no una prueba de la causa.
