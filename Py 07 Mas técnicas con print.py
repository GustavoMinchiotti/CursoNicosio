# definimos un entero. El operador = es de asignacion
valor=5
print (valor)
# Definimos un flotante
precio=18.5
print (precio)

# Lo definimos con constructor
saldo=float(14)
print(saldo)

# Podemos definir directamente al hacer la 

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
print ("\n")# estoy usando el salto de linea para que la salida sea mas prolija

# The line `# Creación de una cadena con formato` is a comment in Spanish that translates to "Creating
# a formatted string". It is describing the purpose or functionality of the following code block,
# which involves using string formatting with the `%` operator to insert variables into a string
# template.
# Creación de una cadena con formato
formato = "Una variable %r, otra variable %r"
# var %r, r = raw mantiene el tipo de variable, es util para frases repetitivas!!
# pero se utiliza mas para debug, no es una buena practica.
print (formato %(precio, saldo))
print (formato %(nombre, acierto))
print (formato %(valor, calif1))
print ("\n")

# Imprimir lineas multiples...
print ("""esta es
una impresión
de varias lineas""")
print ("\n")
# Códigos de escape
print ("Voy a imprimir una \\ aqui")
print ("Si lo deseo pongo \' o \" en la impresión")
print ("una linea \notra linea abajo")
print ("\t con salto de tab")
