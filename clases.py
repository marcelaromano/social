import unittest


def suma(a, b):
    return a + b


class Vehiculo:

    def acelerar(self):
        print('Acelerando')

    def frenar(self):
        print('Frenando')


class Auto:

    # constructor
    def __init__(self, un_color, una_patente):
        self.color = un_color
        self.patente = una_patente

    def acelerar(self):
        print('Acelerando auto {}'.format(self.color))


# se costruye un objeto
auto_rojo = Auto('rojo', 'abc123')
print(auto_rojo.color)
print(auto_rojo.patente)
auto_rojo.acelerar()

auto_blanco = Auto('blanco', 'abc124')
auto_blanco.acelerar()



#class PruebasSuma(unittest.TestCase):




#print(suma(132321, 232321321))