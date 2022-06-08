# Comprension de listas
# implementa en las listas la notacion de los conjuntos que usan los matematicos

valores=[1,2,3,4,5]

cuadrados=[(x*x)for x in valores]
print("cuadrados")
print(cuadrados)
print()

# trinomio cuadrado perfecto

trinomios=[ (x*x + 2*x*y + y*y) for x in range (1,3) for y in range(1,3) ]
print("trinomios")
print(trinomios)
print()

# Convertir pulgadas a contimetros, solo para valores positivos

pulgadas=[1, 3.5, -6, -2, 5.1, -3.2]

cm=[ (x*2.54) for x in pulgadas if x>0]
print("conversion")
print(cm)
print()

# Comprension de Generador, crea un generador en lugar de una lista
# funcion que trabaja como un iterador

valores=[1,2,3,4,5,4,5]
gen1= (x*x for x in valores)

print("Generadores")
print(gen1)
# Lo convertimos en una lista

gen2 = list(gen1)
print(gen2)
print()

# Comprension de sets {conjuntos}

valores=[1,2,3,4,5,4,5] # intencionalmente hay valores repetidos

cuadrados= {x*x for x in valores}
print(cuadrados)





