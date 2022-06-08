# Shallow copy y Deep copy, superficial y profunda
# Solo es importante para los objetos compuestos

# esto no es una copia solo se referencia a la misma instancia que a
a=5
b=a

nombres1=["Charo","Indira"]
nombres2=nombres1

# ambos a la misma instancia
print("misma instancia")
print("nombres1",nombres1)
print("nombres2",nombres2)
print()

# nombres2 ahora apunta a otra instancia
print("otra instancia")
nombres2=["Ana","Luis"]
print("nombres1",nombres1)
print("nombres2",nombres2)
print()
print("----"*10)

# HASTA ACÁ FUNCIONA PERO SI HAGO UNA MODIFICACION EN UN ÍNDICE ME CAMBIA
# TAMBIEN LA INSTANCIA REFERENCIADA

nombres1=["Charo","Indira"]
nombres2=nombres1

# ambos a la misma instancia
print("modificado")
print("misma instancia")
print("nombres1",nombres1)
print("nombres2",nombres2)
print()
nombres2[1]="Aldo"

# nombres2 ahora apunta a otra instancia
print("otra instancia")
nombres2=["Ana","Luis"]
print("nombres1",nombres1,"ha sido modificado el indice 1")
print("nombres2",nombres2)
print()
print("----"*10)


print("deepcopy")
# Necesitamos importar desde el modulo copy
from copy import deepcopy

fonemas1=["a","e","i",["ba","be","bi"]]
fonemas2= deepcopy(fonemas1)

# no se presentan problemas
fonemas2[1]="U"

print("fonemas1",fonemas1)
print("fonemas2",fonemas2)

# mas cambios
fonemas2[3][0]="DA"     #modificacion del array dentro del array
print("fonemas1",fonemas1)
print("fonemas2",fonemas2)



















