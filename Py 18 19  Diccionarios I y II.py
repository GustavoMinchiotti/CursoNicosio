# diccionarios, estructura de datos asociativa no secuencial
# estructura de datos, tiene una llave y un valor asociado a esa llave/clave
# las llaves deben de ser inmutables y es posible tener llaves repetidas
# Los valores pueden ser cualquier objeto valido en python
# Solo un valor por llave

# Creacion de diccionario y acceso

productos={"ft01":"Manzana","ft02":"Pera","ft03":"Platano","ft04":"Ciruela"}

print(productos["ft02"])
print("-+-+"*5)

print(productos)
print("-+-+"*5)

for n in productos:
    print(n,(productos[n]))
    
# ejemplo de algo inexistente

# print(productos["NoExiste"]) # va a generar un error.

# Actualizando una entrada
print("-+-+"*7)

productos["ft03"]= "Mango"

print(productos["ft03"])
print("-+-+"*7)

# Adicionando una entrada
productos["ft05"]="Kiwi"
print(productos)
print("-+-+"*7)

# Copiar el diccionario en una nueva instancia
productos2=productos.copy()
print("COPIA")
print(productos2)
print("-+-+"*7)

# Borrar un elemento
del productos["ft02"]
print(productos)
print("-+-+"*7)

# Borrar todos los elementos de la lista //imprime un dir vacío
productos.clear()
print(productos)
print("-+-+"*7)

# Elimina el diccionario
'''del productos'''
