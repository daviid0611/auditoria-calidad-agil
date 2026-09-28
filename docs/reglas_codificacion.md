# Cinco reglas de codificación del equipo

Cada regla se responde con sí o no. Los comandos se ejecutan desde la raíz del repositorio. Revisar estas reglas es parte del criterio 5 de la DoD.

1. **Toda función pública declara el tipo de cada parámetro y del valor de retorno.**
   - Verificación: `grep -n "^def " src/*.py`. Cada línea muestra `nombre: tipo` en todos los parámetros y `-> tipo` antes de los dos puntos.
   - Evidencia: `def calcular_copago(valor_consulta: float, tipo_afiliado: str) -> float:` (`src/citas.py`).
   - Atributo: Mantenibilidad / Analizabilidad.

2. **Toda función pública tiene un docstring con su especificación: entradas válidas, errores que lanza y formato del resultado.**
   - Verificación: la primera línea del cuerpo de cada función de `src/` es un docstring que menciona los casos válidos, los `ValueError` y el redondeo.
   - Evidencia: el docstring de `calcular_copago` enumera los 3 tipos de afiliado, los 2 casos de `ValueError` y el redondeo a 2 decimales.
   - Atributo: Mantenibilidad / Analizabilidad.

3. **Los porcentajes de negocio se definen una sola vez, en una constante con nombre en MAYÚSCULAS. No se escriben porcentajes literales dentro de las funciones.**
   - Verificación: `grep -nE "[0-9]+\.[0-9]+" src/citas.py` solo muestra líneas dentro de `PORCENTAJE_COPAGO`.
   - Evidencia: `PORCENTAJE_COPAGO = {"contributivo": 0.10, "subsidiado": 0.0, "particular": 1.0}`. Para cambiar un porcentaje o agregar un tipo de afiliado se toca una sola línea.
   - Atributo: Mantenibilidad / Modificabilidad.

4. **Las entradas inválidas se validan al inicio de la función y se rechazan con `ValueError` y un mensaje que dice qué dato falló. Está prohibido capturar excepciones genéricas (`except Exception`) o devolver `None` ante un error.**
   - Verificación: `grep -rn "except" src/` no devuelve nada, y `grep -n "raise ValueError" src/citas.py` muestra las validaciones antes del `return`.
   - Evidencia: `raise ValueError("valor_consulta no puede ser negativo")` y `raise ValueError(f"tipo_afiliado no válido: {tipo_afiliado!r}")`, líneas 23 y 25 de `src/citas.py`.
   - Atributo: Capacidad de interacción / Protección contra errores del usuario.

5. **Los nombres se escriben en español y en `snake_case` (constantes en `MAYÚSCULAS`). Las pruebas se llaman `test_<caso>_<resultado_esperado>`.**
   - Verificación: `grep -n "^def test_" tests/*.py`. Cada nombre dice qué caso prueba y qué resultado espera.
   - Evidencia: `test_subsidiado_no_paga`, `test_valor_negativo_lanza_value_error`, `test_tipo_afiliado_invalido_lanza_value_error`. Si una prueba falla en el CI, su nombre ya dice qué regla de negocio se rompió.
   - Atributo: Mantenibilidad / Analizabilidad.
