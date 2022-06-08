# Range genera una lista de progresiones aritmeticas

# Uso de range n elementos, de 0 a n-1
print (*range (10))

# Uso de range en un rango (n,m) de n a m-1
print (*range (5,15))

# Uso de range con un incremento en particular
print (*range(5,50,5))

# ---------modificado para 3.X----------------

# Uso de for para iterar una lista
'''
nombres=["Charo","Indi","Aye","Gustavo"]

for nombre in nombres:
    print ("Hola ", nombre)
'''
'''
# Uso de for con un rango
sumatoria=0
for n in range(5):
    print(n)
    sumatoria = sumatoria + n
print("La sumatoria es ", sumatoria)

# Otro for con rango mas inicio -- 
# Uso de range en un rango (n,m) de n a m-1
for m in range (5, 15):
    print (m)
'''

'''
# Otro for con rango pero ahora regresivo
for g in range (15, 5, -1):
    print (g)
# Otro ejemplo con sumatoria e input del usuario
h= input("Ingrese un valor: ")
h= int (h)
sumador=0

for n in range(1,h+1):
    sumador = sumador + n
    
print(sumador)

'''
'''
# Ejemplo con continue
for n in range(10):
    print(n)
    if n%2==0:
        continue
    print("esto va luego de un impar")
'''
# Ejemplo con break
for n in range(10):
    print(n)
    if n==5:
        break
print("fuera del for")


# Ejemplo con else e input del usuario
r= input("Ingrese un valor: ")
r= int (r)

for n in range(10):
    print(n)
    if n==r:
        break
else:
    print("estoy dentro del else")
print("Fuera del for y del else")





















