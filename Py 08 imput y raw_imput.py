# Pedir informacion al usuario
# usando input
# al escribir cadenas Hay que ponerlas con " "

nombre = input ("Decime tu nombre: ")
base = input ("Ingrese la base: ")
altura = input ("Ingrese la altura: ")

base = int (base)       # los tuve que parcear porque
altura = int (altura)   # no me los reconocia como int

area = base * altura
perimetro = 2 * (base + altura)

print ("Hola ",nombre,"el área es: ",area," y el perimetro es: ",perimetro)

print ("Usando la funcion type podemos ver que tipo de variable es:")
print ("variable base tiene asignado el valor: ", base ,"y su tipo es:", type (base))

# Usando raw_input
# en raw_input hay que forzar el tipo de la variable a la cual
# le asignamos lo ingresado pero no existe en Py 3.X asi que
# no voy a profundizar
"""nombre = str(raw_input("Decime tu nombre ")) """

