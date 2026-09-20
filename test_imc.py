"""Testes unitários para a calculadora de IMC."""

import pytest
from imc import calcular_imc, classificar_imc


def test_calcular_imc_valido():
    assert round(calcular_imc(70, 1.75), 2) == 22.86


def test_calcular_imc_altura_invalida():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)


def test_calcular_imc_peso_invalido():
    with pytest.raises(ValueError):
        calcular_imc(0, 1.75)


@pytest.mark.parametrize(
    "imc,esperado",
    [
        (17, "Abaixo do peso"),
        (22, "Peso normal"),
        (27, "Sobrepeso"),
        (32, "Obesidade grau I"),
        (37, "Obesidade grau II"),
        (42, "Obesidade grau III"),
    ],
)
def test_classificar_imc(imc, esperado):
    assert classificar_imc(imc) == esperado
