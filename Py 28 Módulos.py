# En este programa utilizamos el modulo

# importamos el modulo
# Directorio actual
# Variable PYTHONPATH
# Path de default

import programa023Mod

m=3
n=5

programa023Mod.suma(m,n)
programa023Mod.multi(m,n)

print("****"*15)

# Importamos solo una funcion del modulo

from programa023Mod import suma

m=3
n=5

suma(m,n)
#multi(m,n)

print("****"*15)

# Importamos todas las funciones del modulo

from programa023Mod import *

m=3
n=5
suma(m,n)
multi(m,n)
div(m,n)

print("****"*15)

# Imprimimos la variable del modulo

print(x)

# Variable local y luego la del modulo
x=50
print(x)
imprime()   #funcion del modulo

print("****"*15)

# Uso de dir

import programa023Mod

contenidosModulo = dir(programa023Mod)
print(contenidosModulo)

# Importamos un paquete

'''import mensajes

mensajes.hola()
mensajes.como()
mensajes.adios()''' # quedo demostrado que este metodo no funciono en Py 3.X



