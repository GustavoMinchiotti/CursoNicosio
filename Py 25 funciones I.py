# Definicion de funciones

'''def mostrar(numero):
    "esta funcion imprime el numero" #esto es el Docstring es documentacion 
    print(numero)

# Aqui el codigo principal
mostrar(1)
mostrar(3)
mostrar(5)

print("/*-/*-"*10)

# Aqui vemos el uso de Docstring
def mostrar(numero):
    "esta funcion imprime el numero"
    print(numero)
    
print(mostrar.__doc__)

print("/*-/*-"*10)   '''

# Pasar parametros
def adicionar (nombre):
    nombre="Hola "+nombre
    print(nombre)

def mostrarSuma(a,b):
    r=a+b
    print(r)

adicionar("Charo") # Adicione directamente una string

print("/*-/*-"*10)

nombre="Gustavo"
adicionar(nombre) # A la variable ya declarada le asigno otra string
mostrarSuma(5,4)

print("/*-/*-"*10)
    
# Parametros opcionales
def multi(a, b=5):
    r=a*b
    print(r)

# invocamos normal
multi(4,8)
    
# Invocamos opc. con un solo parametro
multi(7)

print("/*-/*-"*10)

# Parametros con Keyword
def muestraValores(a=1, b=2, c=3):
    print("A es ",a)
    print("B es ",b)
    print("C es ",c)

# Invocamos normal
muestraValores(5,10,15)
print("/*-/*-"*10)

# Invocamos con keyword
muestraValores(b=6, c=8, a=16)
print("/*-/*-"*10)

# Invocamos con keyword y parametro opcional
muestraValores(b=20)


    






