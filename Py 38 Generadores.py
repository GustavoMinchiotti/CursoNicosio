# Un generador es una funcion que regresa un objeto generador
# Un generador se puede ver como una funcion que produce una secuencia de resultados en lugar de un
# solo objeto. Estos son producidos al iterar yield es lo que convierte a una funcion en un iterador.
# Se termina la ejecucion cuando se ha llegado a yield y el valor es regresado cuando se usa next, se
# avanza al siguiente yield.
# Cualquier estado intermedio de las variables se guarda entre invocaciones cosa que no sucede en las
# funciones.

def dias_generador():
    yield("lunes")
    yield("martes")
    yield("miercoles")
    yield("jueves")
    yield("viernes")

dias = dias_generador()

print(next(dias))
print(next(dias))
print(next(dias))
print(next(dias))
print(next(dias))
#print(next(dias))

print("-/-/-/-"*10)

# Creamos un generador para potencias de dos
def potencias2():
    b=1
    while b>0:
        yield b
        b=b+b

binarios=potencias2()
for x in binarios:
    print(x)
    if x>100:
        break

print("-/-/-/-"*10)

# Creamos un generador para potencias de 2 hasta un numero determinado

'''def potencias2b():
    b=1
    while b>0:
        yield b
        b=b+b
        if b>300:
            raise StopIteration

binarios2=potencias2b()
for x in binarios:
    print(x)'''  no funciona en P x.3


