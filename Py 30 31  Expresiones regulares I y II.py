# Expresiones regulares
# Se usan para filtrar textos y verificar si un texto concuerda con la expresion

# importamos el modulo re

import re

a= re.search("casa","La casa del Casamentero")
print(a)

if re.search("casa","El estudiante es un casanova en la escuela"):
    print("1 Está casa")
else:
    print("1 No está casa")

if re.search("casa","El estudiante es un genio en la escuela"):
    print("2 Está casa")
else:
    print("2 No está casa")

if re.search("casa ","El estudiante es un casanova en la escuela"):
    print("3 Está casa")
else:
    print("4 No está casa")# notar que hay un espacio.

print("*+*+*"*10)    

# Uso de . significa cualquier caracter
# cabal, academico

if re.search(" ca.","Saludos al mas cabal"):
    print("Hay palabra que inicia con ca")
else:
    print("No hay palabra que inicia con ca")

if re.search(" ca.","Saludos al mas academico"):
    print("Hay palabra que inicia con ca")
else:
    print("No hay palabra que inicia con ca")

print("*+*+*"*10)

# Uso de clases de caracteres, se usa [] para contener los caracteres
# Nico, Necio, Naco

if re.search("N[ie]c","Hola Nico"):
    print("Se encontro")
else:
    print("No se encontro")

print("*+*+*"*10)

# Un rango   (en este ejemplo rango alfabético desde a hasta u)
# Nico, Neco, Noco, Nzco
if re.search("N[a-u]c", "Hola Nico"):
    print("Se encontro")
else:
    print("No se encontro")

print("*+*+*"*10)

# uso del complemento ^  (va a encontrar todos los caracteres menos i e)

if re.search("N[^ie]c", "Hola Nico"):
    print("Se encontro")
else:
    print("No se encontro")

print("*+*+*"*12)

# Uso de match para saber si una cadena inicia con una expresion

if re.match("N[ie]c", "de youtube ...Nicosio mi canal favorito"):
    print("Si inicia")
else:
    print("No inicia")
    
print("*+*+*"*12)

# Para saber si una cadena finaliza con una expresion ($)

if re.search("N[ie]c$", "de youtube ...Nicosio mi canal favorito"):
    print("Si finaliza")
else:
    print("No finaliza")

print("*+*+*"*15)

# Uso de un elemento opcional
# Nico, Nilo, Nio

if re.search("N[ie]c?o","Hola Nio"):
    print("Se encontro")
else:
    print("No se encontro")

print("*+*+*"*10)

# Cuantificador
# Busca que existan dos digitos

if re.search("[0-9]{2}", "hola 45 nico"):
    print("Se encontro")
else:
    print("No se encontro")



    
