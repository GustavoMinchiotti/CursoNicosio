# Conjuntos - Sets
# Es una coleccion no ordenada de objetos unicos e inmutables
# Trata de ser similar a los conjuntos en el sentido matematico

# Creacion de sets usando set, tambien se puede usar {} en algunas versiones de Py

letras=set("Hola a todos") # toma cada letra como elemento

print (letras)

meses=set(["enero","febrero","marzo","abril"])
# en la lista toma cada palabra como elemento, porque las estoy separando 

print (meses)

numeros=set((1,3,5,7,9,3,10))

print(numeros)

# Inmutables... si intento lo siguente terminaria en error porque una
# lista es mutable y el conjunto/set no lo es.

'''inmutable=set(([1,2,3],[4,5,6]))'''
# No puede contener objetos mutables pero si es mutable
'''una forma sencilla de comprobar que es mutable es
adicionando algo al conjunto'''
# Adicion al set
meses.add("mayo")

# Los Frozensets son similares pero inmutables
dias=frozenset(["lunes","martes","miercoles"])
'''dias.add("jueves")'''
print(dias)
