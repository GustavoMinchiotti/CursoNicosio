'''import mensajes

mensajes.hola()
mensajes.como()
mensajes.adios()'''

'''from mensajes import hola

hola()'''


'''from mensajes.hola import hola

mensajes.hola()'''

from mensajes.hola import *
from mensajes.como import *
from mensajes.adios import *
hola()
como()
adios()

# esto corresponde al video Nº 29 modulos y paquetes
