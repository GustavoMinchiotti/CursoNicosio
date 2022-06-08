import re
# findall regresa una lista con todos los matches

encontrados=re.findall("c[ao]s","El casanova no se casa ni va al casamiento, porque la cosa es complicada")
print(encontrados)

print("++++++"*7)

# Alternaciones
b = "yo se programar en python"
mo = re.search("(c|java|python)",b)
if mo:
    print("Sabes programar")
else:
    print("aprende otro lenguaje")

print("++++++"*8)

# Split nos ayuda a dividir una cadena en sub cadenas

mensaje="Este es un test de separacion, division"

partes=re.split(" ",mensaje)
print(partes)

print("++++++"*9)

# Reemplazar

mens2="Yo hablo ingles y no soy ingles"

sustituido=re.sub("ingles","español",mens2)
print(sustituido)

print("++++++"*10)

# metodos utiles para cadenas
print()

mensajex = "hola A Todos"
print(mensajex.capitalize())

print()

palabra="Python"
print(palabra.center(15,"-"))

print()

cuenta= "Hola a todos los que ven la ola en Holanda"
print(cuenta.count("ola"))

print()

tex="345"
print(tex.isalnum()) # regresa true or false si son o no todos alfanuméricos
print(tex.isalpha()) # regresa true or false si son o no todos letras
print(tex.isdigit()) # regresa true or false si son o no todos numeros

