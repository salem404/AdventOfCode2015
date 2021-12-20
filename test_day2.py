from day2 import calcular_papel, menor

datos = '''2x3x4
2x3x4'''

def test_calcular_papel():
    assert calcular_papel(datos) == 116

def test_menor():
    assert menor(1,2,3) == 1