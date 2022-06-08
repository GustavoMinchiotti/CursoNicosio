# Listas III
# Obtención del máximo
lista2= [2,77]
lista3= [50,70,23,57,90,10,45,23,11,23,65]
lista4= [4,98,56,50,100]
print("Máximo",max(lista3))

# Obtención del mínimo
print("Mínimo",min(lista3))

# Adicion de elementos
print(lista3)
lista3.append(14) #.append + (valor a agregar) es un método de la clase list
print(lista3)

# Conteo de un elemento (cuantas veces aparece)
print(lista3.count(23))

# Obtener el indice mas bajo del elemento repetido
print(lista3.index(23)) 

# Otra forma de unir listas
lista3.extend(lista2)
print(lista3)
print("*****"*5)

# Insertar en un indice en particular
print(lista4)
lista4.insert(2,44) #inserto en el indice 2 al nº 44
print(lista4)
print("*****"*5)

# Hace pop del ùltimo objeto la lista
print(lista4)
print(lista4.pop())
print(lista4)
print("*****"*5)

# Hace pop de un objeto en un índice en particular
print(lista4)
print(lista4.pop(2))
print(lista4)
print("*****"*5)

# Hacer reversa de una lista
lista4.reverse()
print(lista4)
print("*****"*5)

# Ordenar una lista
lista4.sort()
print(lista4)









