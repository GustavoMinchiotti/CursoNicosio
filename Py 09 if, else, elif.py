# Uso normal de if, elif y else
# Bloque de codigo
"""
# Uso normal de if
a = input("ingresa un número ")
a = int(a) #En Python 2.X no hace falta convertir a int

if  a >0:
    print("El número es positivo")

if  a<0:
    print("el número es negativo")
    print("Esto tambien esparte del bloque de codigo")
print("Fin del elemplo")

# Uso de if con else
b = input("ingresa un número ")
b = int(b)
if b>0:
    print("El número es positivo")
else:
    print("el número es negativo")
    print("-"*50)
"""
# Uso de if con elseif
c = input("ingresa un número ")
c = int(c)
if c >0:
    print("El número es positivo")
elif c==0:    
    print("El número es cero")
else:    
    print("el número es negativo")
print("-"*50)

if c==1:
    print("Es 1")
elif c==2:
    print("Es 2")
elif c==3:
    print("Es 3")
elif c==4:
    print("Es 4")
else:
    print("Ni 1 ni 2 ni 3 ni 4, es cualquier otro NÚMERO")

    
    
