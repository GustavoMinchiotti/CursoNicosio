# Operaciones con sets

# Creacion de set con {}
colores={"rojo","verde","azul"}
print(type(colores))
print(colores)

print("*-*-"*20)

# Copiar el set
masColores = colores.copy()
print(masColores,'".copy"')

print("*-*-"*20)

# Remover todos los elementos de la lista
masColores.clear()
print(masColores,'".clear"')

'''si quiero borrar el conjunto lo hago con del (del masColores)'''

print("*-*-"*20)

# Diferencia / muestra los elementos los elementos de (a)
# que no pertenecen a (b)
a= {1,2,3,4,5,6}
b= {1,3,5}
print(a.difference(b))
print (a-b)
print("*-*-"*20)

c = {1, 2, 3, 4}
d = {2, 4, 6, 8}
print (c - d)
print("*-*-"*20)

# Difference_update
print("difference_update")
x= a-b
print(a,x)
# Difference_update
c={1,2,3,4,5,6}

c.difference_update(b)
print("c", c)

print("*-+-"*20)

# Discard, no muestra error
print("discard sin error")
b.discard(3)    # saca al elemento 3 del conjunto no al indice 3º
print(b)

b.discard(9)#acá estoy eliminando un elemento que no existe

# Remove, muestra error
print("remuve con error")
d={1,2,3}

d.remove(2)
print(d)
d.remove(9)


print("*-+-"*20)
mi_conjunto = {1, 3, 2, 9, 3, 1}
for e in mi_conjunto:
    print(e)
    
