# Excepciones
# El codigo que tiene riesgo se coloca en un bloque try
# en lugar de try usamos except

# assert evalua una expresion, si la evaluacion es falsa se levanta una excepcion de
# tipo AssertionError

def pares(n):
    assert (n%2==0)
    print('es par')

pares(4)
pares(16)
#pares(5)

print('/*-/*-/*-/*-/*-'*4)

try:
    print('intento con un impar (5)')
    pares(5)
except AssertionError:
    print('fue impar')
else:
    print('era par')

print('/*-/*-/*-/*-/*-'*4)

# cuando deseamos capturar todas las excepciones

try:
    print('intento con un impar (5)')
    pares(5)
except:
    print('fue impar')
else:
    print('era par')

print('/*-/*-/*-/*-/*-'*4)

# finally se usa para poner codigo que se ejecuta independientemente de si la
# excepcion ocurre o no

try:
    print('vamos a intentar con un impar')
    pares(6)
except:
    print('fue impar')
else:
    print('era par')
finally:
    print('gracias por usar el programa')

print('/*-/*-/*-/*-/*-'*4)

# argument da informacion sobre la exepcion en Py 2.x pero no funciona en Py 3.x
# en este caso utilicé repr (https://www.delftstack.com/es/howto/python/python-exception-message/)

a='hola'

try:
    x=int(a)
    print(x)
except ValueError as e:
    print('El argumento dice', repr(e))

# https://controlautomaticoeducacion.com/python-desde-cero/manejo-de-errores-en-python/
print('/*-/*-/*-/*-/*-'*4)
print('/*-/*-/*-/*-/*-'*4)
# Se pueden tener multiples excepciones y levantar una excepcion usando rise

class Fue1(RuntimeError):
    def __init__(self):
        print('desde la clase') #no explico las clases

class Fue2(RuntimeError):
    def __init__(self, arg):
        self.args = arg         # esta tiene param y argumento creados

def checar(n):
    if n==1:
        raise Fue1              # la func. a traves de rise levanta las clases Fue1 y 2
    if n==2:
        raise Fue2('Error')
    print('todo bien')          # si entra otro valor ue 1 o 2 imprime todo bien

try:
    checar(3)
except Fue1:
    print('Excepcion para el 1')
except Fue2:
    print('Excepcion para el 2')

