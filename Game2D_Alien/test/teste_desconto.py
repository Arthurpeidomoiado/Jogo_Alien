import pytest
from desconto import DescontoNormal, DescontoVIP

def test_calcular_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100, 2)
    assert resultado == 28.0, f"Esperado: 28.0, Obtido: {resultado}"

@pytest.fixture
def desconto_vip():
    return DescontoVIP()
def test_desconto_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20.0, "Desconto VIP para 100 deve ser 20.0"
def test_desconto_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40.0, "Desconto VIP para 200 deve ser 40.0"
@pytest.mark.parametrize("valor, esperado", [
    (100, 20.0),
    (200, 40.0),
    (300, 60.0)
])
def test_desconto_vip_parametrizado( valor, esperado):
    desconto = DescontoVIP()
    resultado = desconto.calcular(valor)
    assert resultado == esperado