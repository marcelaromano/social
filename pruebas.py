import unittest

def suma(a, b):
    return a + b


class PruebasSuma(unittest.TestCase):

    def test_suma_2_2_da_4(self):
        resultado_obtenido = suma(2, 2)
        resultado_esperado = 4

        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_suma_numeros_grandes(self):
        resultado_obtenido = suma(123, 456)
        resultado_esperado = 579

        self.assertEqual(resultado_obtenido, resultado_esperado)
