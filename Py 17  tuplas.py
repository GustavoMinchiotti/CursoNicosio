# Tuplas
#creacion de una tupla
meses=("enero","febrero","marzo","abril")
unDato=(5,)

# Acceso al tuple
print(meses)
print(meses[1:3])   # imprime un rango
print('---'*10)

for m in meses:     # itera
    print(m)
print('---'*10)
print(meses[2])     # imprime un indice

# NO LO PUEDO MODIFICAR

# SE PUEDEN CONCATENAR  porque estamos creando una nueva tupla
nuevoTuple = meses + unDato
print(nuevoTuple)
print('---'*10)
# No se puede borrar un elemento en particular
# si se puede borrar completo
del nuevoTuple
# print(nuevoTuple)

# Convertir una lista en un tuple
miLista = [":)",":|",":/",":("]
miTuple = tuple(miLista)

print(miTuple, " TUPLE")
print('---'*10)

# Convertir una lista en un tuple
miLista2= list(miTuple)
print(miLista2, " LISTA")
print('---'*10)
# Operacines con Tuples
# Son similares a las de las listas
print('---'*10)
print(len(meses))
print('---'*10)
otro= (5,6,7,)*4
print (otro)

print (('¿se encuentra 5 en otro?'),5 in otro)
print (('¿se encuentra 9 en otro?'),9 in otro)
print('---'*10)

tuple1, tuple2 = (100, 'hola'),(300,'adios') # Asignacion multiple

tuple3 = tuple2 + (50, 'saludos') # estoy creando una nueva.

print (tuple1, tuple2)
print(tuple3)
print('---'*10)
print(max (otro))
print(min (otro))

















