# Creacion de un decorador
# definimos la funcion decoradora

def miDecorador(func):
    # definimos la funcion que envuelve
    def decorador(a, b):
        print("Antes de llamar al decorado")
        print("He recibido a: ", a, "y ", b)
        # Llamamos al decorado
        func(a, b)
        # Regresamos de la ejecucion del decorado
        print("Ya regrese de la ejecucion del decorador")
        print(a, b)

    return decorador


print("*****" * 9)


# Decoramos la funcion

@miDecorador
def miFuncion(a, b):
    x = a + b
    print("estoy en mi funcion con x:", x)


# invocamos la funcion
miFuncion(2, 3)

print("*****" * 9)


@miDecorador
def otraFunc(a, b):
    x = a * b
    print("multi :", x)


otraFunc(2, 2)

