# Manejo avanzado de funciones y decoradores
# Es un objeto que puede ser invocado y que modifica una funcion o clase

# En Python los nombres de las funciones son referencias y una funcion puede
# tener mas de un nombre

def cuadrado(a):
    r=a*a
    return r

potencia2 = cuadrado

print(cuadrado(2))
print("------"*10)
print(potencia2(4))

print()
# Si tenemos dos o mas referencias, podemos eliminar una sin perder la otra

del cuadrado
print(potencia2(5))

print("------"*10)

# En python de puede definir una funcion adentro de otra

def cuadradoPar(a):

    def checarPar(x):
        return x%2==0

    if(checarPar(a)):
        print("se puede hacer el cuadrado")
        return a*a
    else:
        print("no de puede hacer el cuadrado")
        return 0
print(cuadradoPar(16))
print(cuadradoPar(15))

print("------"*10)

# En Python la funcion es un objeto y puede ser pado como parametro.

def parImpar(a):
    if(a%2==0):
        print("es par")
    else:
        print("es impar")

def ImprimeMucho(a):
    valor=str(a)
    print((valor+" - ")*a)

def potencia(func,x):
    r=x**x
    func(r)
    print("la potencia es",r)

potencia(parImpar,5)
print()
'''potencia(ImprimeMucho,4)'''

print("------"*10)

# Las funciones tambien pueden regresar funciones (complicado)

def f(x):
    def g(y):
        print("estoy en g, este es x:",x,"este es y:",y)
        return y+x
    print("estoy en f, este es x:",x)
    return g

nf1 = f(1)
nf2 = f(3)

print()

print(nf1(5))
print(nf2(7))

print("------"*10)

# Creacion de un decorador
# definimos la funcion decoradora

def miDecorador(func):
    #definimos la funcion que envuelve
    def decorador(a):
        print("Antes de llamar al decorado")
        print("He recibido a: ",a)
        # Llamamos al decorado
        func(a)
        # Regresamos de la ejecucion del decorado
        print("Ya regrese de la ejecucion del decorador")

    return decorador
# Decoramos la funcion
@miDecorador
def miFuncion(x):
    print("estoy en mi funcion con x:",x)

# invocamos la funcion
miFuncion(5)

