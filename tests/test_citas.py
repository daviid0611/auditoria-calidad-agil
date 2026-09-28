import pytest

from src.citas import calcular_copago


# Ejemplo de prueba (ya escrita para que vea el formato).
def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


# TODO 1: prueba para "contributivo" (10 %).
# TODO 2: prueba para "subsidiado" (0).
# TODO 3: prueba de valores inválidos: pytest.raises(ValueError).
