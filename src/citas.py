"""Módulo de citas médicas (código base del taller)."""


def calcular_copago(valor_consulta: float, tipo_afiliado: str) -> float:
    """Calcula el copago que paga el paciente.

    Especificación:
    - "contributivo": paga el 10 % del valor de la consulta.
    - "subsidiado": paga 0.
    - "particular": paga el 100 %.
    - Si valor_consulta es negativo, lanza ValueError.
    - Si tipo_afiliado no es uno de los tres anteriores, lanza ValueError.
    - El resultado se redondea a 2 decimales.
    """
    # TODO (XP/TDD): escriba primero las pruebas en tests/test_citas.py y luego implemente.
    raise NotImplementedError
