# Uso de while de la forma general
'''
n=0 #inicializo la variante y en python es importante declararla antes
# el resultado es muy claro porque Py es secuencial
while n<10:
    print ("Hola")
    print (n)
    n=n+1

print ("\nAfuera del while")'''

# Uso del continue
print ("\n")
m=0
while m<10:
    print("Hola")
    print(m," Valor original")
    m=m+1
    print(m," aplico módulo")
    if m%2==0:   # cuando se cunpla esto pasa al continue
        continue # y el continue lleva la ejecucion de vuelta al while
    print("Solo se imprime si NO se cumple el continue, m%2 !=0 \n")

    
print("\nNuevamente fuera del while") 

'''
# Uso de break

g=0

while g<10:
    print("hola",g)
    g=g+1
    if g==5:
        break
    print("Esto solo se imprime dentro del ciclo")
    
print ("\nAfuera del while")
'''
# Uso de else
'''
a=0
b=input("ingrese un numero: ")
b= int(b)
while a<10:
    print("hola",a)
    if a==b:
        break

    a=a+1
    print("Sigo imprimiendo")

else:
    print("No encontre el numero")

print ("\nAfuera del while")    
    
'''
