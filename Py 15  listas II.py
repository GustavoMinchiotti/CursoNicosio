# Operraciones y funciones sobre listas
frutas = ["pera","manzana","ciruela","naranja"]
calif = [8,7,10,9,8]
varios = ["internet",14.5,"estrella",5, True]

# Longitud
print (len(frutas))

print("-*-"*10)

# Concatenacion
lista2 = calif+varios
for elemento in lista2:
    print(elemento)

print("-*-"*10)    


print(frutas)
print ("lista2",lista2)

# Membresia

print(7 in lista2)#me va a devolver true si 7 se encuentra la lista
print("manzana"in lista2)# me devuelve false si manzana no se encuentra

# Repeticion
lista3 = frutas*2
print(lista3)

# Slicing
listaN = [0,1,2,3,4,5,6,7,8,9]
print("ListaN: ",(listaN))

print("El indice 3 tiene valor=" , listaN[3])

listaH = listaN[3:]
print("ListaH es listaN [3:] ",(listaH))

listaJ = listaN[:7]
print("ListaJ es listaN [:7] ",(listaJ))

listaU = listaN[3:7]
print("ListaU es listaN [3:7]",(listaU))
