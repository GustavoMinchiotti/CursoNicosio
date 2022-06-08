# Creacion de listas
frutas = ["pera","manzana","ciruela","naranja"]
calif = [8,7,10,9,8]
varios = ["internet",14.5,"estrella",5, True]
for elemento in frutas:
    print (elemento)

print("-"*30)    

for elemento in calif:
    print (elemento)

print("-"*30)

for elemento in varios:
    print (elemento)

print("-"*30)
# Acceder a la lista por indice
print (frutas[0])
print (frutas[2])
print (frutas[-1])
#print (frutas[7])
# si utlizamos un indice fuera de los límites nos dara un error
print("¬~"*30)
# Actualizar un valor de la lista

print ("original")
for elemento in frutas:
    print(elemento)
print("^*^*"*10)
frutas[2]= "mango"
for elemento in frutas:
    print(elemento)
print("^*^*"*10)

# Borrado de elementos

for elemento in frutas:
    print(elemento)
print("{¨}"*20)
print ("Antiguo elemento 2: ",frutas[2])
del frutas[2]
print ("Nuevo elemento 2: ",frutas[2])    

print("-"*30)







