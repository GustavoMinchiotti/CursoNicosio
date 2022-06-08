# Numero arbitrario de parametros

def sumatoria(a,*mas):
    sum=a;
    if len(mas)>0:
        for n in mas:
            sum=sum+n
    print(sum)
sumatoria(5)
sumatoria(5,3,1)
sumatoria(1,2,3,4,5)

print("-----------------"*3)
# Uso de return
def suma(a,b):
    r=a+b
    return r

s=suma(5,4)
print(s)

s=suma("Hola"," atodos")
print(s)

print("-----------------"*3)

# Variables globales y locales

g=5

def funcion(mensaje):
    local=3
    print(mensaje*3)
    print(local)
    print("bye "*g)

funcion("hola ")
print(local)
print(g)
