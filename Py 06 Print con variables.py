# definimos un entero. El operador = es de asignacion
valor=5
print (valor)
# Definimos un flotante
precio=18.5
print (precio)

# Lo definimos con constructor
saldo=float(14)
print(saldo)

# Podemos definir directamente al hacer la operacion
total=precio+saldo
print (total)

# Se pueden tener variables de tipo string
nombre = "Aldo"
print (nombre)

# Tambien de tipo Bool
acierto = True #importante la mayúscula.
print (acierto)

# Se pueden hacer asignaciones multiples
calif1, calif2 = 10, 8
print (calif1)
print (calif2)

""" Diferentes formas en las que podemos usar print utilizamos las variables
de la clase anterior obviamente en el mismo programa."""
print("-"*20)
print("El alumno uno tiene la calif de: ", calif1, "y el dos de: ", calif2)

# Otra forma es con el uso de formateadores
print("El primer alumno tiene un: %d y el segundo un: %d" %(calif1, calif2))
# %d indica que el formato es de tipo int
print("%s el precio es de %f por articulo"%(nombre, precio))
# %s es para string y %f para float vemos muchos decimales!!!
print("El precio es %.2f pesos" %precio)

