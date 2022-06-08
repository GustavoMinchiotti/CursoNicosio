# Diccionarios III
# Operaciones y funciones con diccionarios

productos={"ft01":"Manzana","ft02":"Pera","ft03":"Platano","ft04":"Ciruela"}
productos2={"ft01":"Manzana","ft02":"Uva","ft03":"Platano","ft04":"Ciruela"}
productos3={"ft01":"Manzana","ft02":"Pera","ft03":"Platano","ft04":"Ciruela"}

# Comparacion
#print (cmp (productos, productos2)) esto es de python 2 no funciona

print("-*-+"*7)

# Ejemplo de otra pagina
''' https://j2logo.com/python/tutorial/tipo-dict-python/#dict-equal'''

d1 = {'uno': 1, 'dos': 2}
d2 = {'dos': 2, 'uno': 1}
d3 = {'uno': 1}
print(d1 == d2)# responde true si son iguales o false si no lo son

print(d1 == d3)

print("-*-+"*7)

# Longitud
print (len(productos))
print("-*-+"*7)

# Conversion a cadena / string
cadena= str(productos)
cadena2="->"+cadena+"<-"
print(cadena2)
print("-*-+"*7)

# metodo tambien de python 2
'''print(productos.has_key("ft02"))'''


# Imprimir las llaves del dir
print(productos.keys())

print("-*-+"*7)


# Imprimir los valores del dir
print(productos.values())

print("-*-+"*7)

# Imprimir los items del dir
print(productos.items())
print("-*-+"*7)


# Uso de Setdefault
#clave existente no cambia el valor
print('productos.setdefault("ft02", "No hay")')
print(productos.setdefault("ft02", "No hay"))

#clave NO existente si cambia el valor
print('productos.setdefault("noExiste", "No hay")')
print(productos.setdefault("noExiste", "No hay"))

print("-*-+"*7)
print(productos)

# Otra forma de adicionar una entrada con update
print("-*-+"*7)
productos.update({"ft07":"Sandia"})
print(productos)

