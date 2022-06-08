# Operador lamba
# Crea funciones anonimas que se usan en el moemnto que hacen falta
# Generalmente se usan con filter(), map(), reduce()
# lambda arg1, ar2, ...: expresion

valor = lambda a, b: a*a+2*a*b+b*b

print(valor(2,3))

print()
print('****'*15)

# Uso de map
# Invoca una funcion haciendo uso de una secuencia
# ejemplos modificados para python 3.X

def cuadrados(valor):
    return valor * valor

valores=[2,5,10]

resultados = list(map(cuadrados,valores))

print(resultados)

print()
print('****'*15)

# Uso de map con lambda

valores = [2,5,10,3]

resultados= list (map(lambda x: x*x, valores))
print(resultados)

print()
print('****'*15)

# Uso de filter
# Filtra los elementos de una secuencia dependiendo del true o false
# regresando una funcion

def impares (val):
    return (val %2)!=0

valores = [1,4,5,7,8,9,10,12,15,17,18,28]

filtrados=list (filter(impares, valores))
print(filtrados)

print()
print('****'*15)

# Filter con lamba
filtrados= list (filter(lambda x: x%2!=0 , valores))
print (filtrados)

print()
print('****'*15)

# Uso de reduce
# Aplica una funcion de manera continua a una secuencia de valores y regresa
# un unico valor
# [a1,a2,a3,a4,a5]
# b1=fun(a1,a2)
# b2=fun(b1,a3)
# b3=fun(b2,a4)
# b4=fun(b3,a5) -> resultado final
from functools import reduce

valores=[1,2,3,4,5]
def suma (a,b):
    return a+b

r= reduce (suma,valores)
print(r)
print()

# Con lambda

r=reduce(lambda a,b: a+b,valores)
print(r)





