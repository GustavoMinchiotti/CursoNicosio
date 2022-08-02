# Sobrecarga de operadores
# + __add__
# - __sub__
# * __mul__
# ** __pow__
# / __truediv__
# // __floordiv__
# % __mod__
# << __lshift__
# >> __rshift__
# & __and__
# | __or__
# ^ __xor__
# ~ __invert__
# < __lt__
# <= __le__
# == __eq__
# != __ne__
# > __gt__
# >= __ge__

import math

class Vector:
    def __init__(self, px=0, py=0):
        self.x=px
        self.y=py

    def __str__(self):
        return '(%f,%f)'%(self.x, self.y) #método mágico, le digo en que 
                                          #formato quiero la salida de datos  
    # Sobrecarga del operador +
    def __add__(self, operando):
        mx=self.x + operando.x
        my=self.y + operando.y

        return Vector(mx,my)

    # Calculamos la magnitud
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Sobrcarga de ==
    def __eq__(self, operando):
        return self.magnitud()==operando.magnitud()# va a regresar true o false

    # Sobrecarga de >
    def __gt__(self, operando):
        return self.magnitud()>operando.magnitud()

a = Vector(5,3)
b= Vector(-1,2)
d = Vector(5,3)
print(a)
print(b)
print('******'*5)

c= a+b
print(c)
print(a.magnitud())

print('******'*5)

if(a==b):
    print('a y b son iguales')
else:
    print('a y b No son iguales')

if(a==d):
    print('a y d son iguales')
else:
    print('a y d No son iguales')

if(a>b):
    print('a es mayor')
else:
    print('b es mayor')    
    
