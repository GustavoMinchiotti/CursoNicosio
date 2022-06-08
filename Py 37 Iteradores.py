# Iterador - nos permite recorrer una estuctura de datos sin que nos interese conocer la forma
# como trabaja esa esturctura, usamos for

# Generador - es una funcion especial que nos permite implementar iteradores

# internamente el for trabaja con un iterador que va pidiendo el elemento siguiente hasta que
# recibe StopIteration.

'''dias = ["lunes","martes","miercoles","jueves", "viernes"]

for d in dias:
    print(d)

print("------"*10)


dias = ["lunes","martes","miercoles","jueves", "viernes"]

# Se invoca iter en la estructura y nos regresa un iterable
mi_iterador = iter(dias)

# Usamos el iterable con next para obtener el elemento siguiente
print (next(mi_iterador))
print (next(mi_iterador))
print (next(mi_iterador))
print (next(mi_iterador))

# Cuando recibimos StopIteration, sabemos que ya no hay mas elementos
print (next(mi_iterador))
print (next(mi_iterador))

print("------"*10)'''

    
dias = ["lunes","martes","miercoles","jueves", "viernes"]

# Aqui ya estamos mas cerca de construir un iterador para las listas
# Se invoca iter en la estructura y nos regresa un iterable
mi_iterador = iter(dias)

# Creamos un ciclo pero tenemos que tener una excepcion para cachar cuando ya
# no hay mas elementos
while mi_iterador:
    try:
        d=next(mi_iterador)
        print(d)
    except StopIteration:
        print ("no hay mas elementos, forzamos la salida")
        break

print("------"*10)    
