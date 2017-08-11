import unittest


def suma(a, b):
    return a + b

# xxla clase vehiculo  el self es ninguna parametro de entrada.. lo que sale de la funcion es acelerando?
class Vehiculo:

    def acelerar(self):
        print('Acelerando')

    def frenar(self):
        print('Frenando')


# la clase Auto hereda de Vehiculo (entre parentesis). Auto hereda atributos y operaciones de Vehiculo.
class Auto(Vehiculo):

   # constructor....... xx self.color es un arreglo self ?    xxx para que crea la variable un-_color

    def __init__(self, un_color, una_patente):
        self.color = un_color
        self.patente = una_patente

    def acelerar(self):
        print('Acelerando auto {}'.format(self.color))


class Camion(Vehiculo):

    def acelerar(self):
        print('Es un camion acelerando')


# se costruye un objeto
auto_rojo = Auto('rojo', 'abc123')
print(auto_rojo.color)
print(auto_rojo.patente)
auto_rojo.acelerar()
auto_rojo.frenar()

auto_blanco = Auto('blanco', 'abc124')
auto_blanco.acelerar()

camion_1 = Camion()
camion_1.acelerar()

print()

# ejemplo de polimorfismo
vehiculos = [camion_1, auto_rojo, auto_blanco]

for vehiculo in vehiculos:
    vehiculo.acelerar()

