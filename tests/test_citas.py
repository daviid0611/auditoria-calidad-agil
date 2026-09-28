import pytest

from src.citas import calcular_copago


# Ejemplo de prueba (ya escrita para que vea el formato).
def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


# TODO 1: "contributivo" paga el 10 %, redondeado a 2 decimales.
# Sin redondeo, 1001 * 0.10 da 100.10000000000001 y 1234.56 da 123.456 o
# 123.45599999999999 según cómo se calcule. Por eso se compara con == y no
# con pytest.approx: approx aceptaría el valor sin redondear.
@pytest.mark.parametrize(
    ("valor_consulta", "copago_esperado"),
    [(1001, 100.1), (1234.56, 123.46)],
)
def test_contributivo_paga_diez_por_ciento_redondeado(
    valor_consulta, copago_esperado
):
    assert calcular_copago(valor_consulta, "contributivo") == copago_esperado


# TODO 2: "subsidiado" paga 0.
def test_subsidiado_no_paga():
    assert calcular_copago(100000, "subsidiado") == 0


# TODO 3: valores inválidos lanzan ValueError.
# Se usa ValueError y no Exception: NotImplementedError también es una
# Exception y la prueba pasaría sin que la función estuviera implementada.
def test_valor_negativo_lanza_value_error():
    with pytest.raises(ValueError):
        calcular_copago(-1, "contributivo")


def test_tipo_afiliado_invalido_lanza_value_error():
    with pytest.raises(ValueError):
        calcular_copago(100000, "prepagada")
