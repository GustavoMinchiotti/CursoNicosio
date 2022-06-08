# Operadores booleanos
'''
a=input("Ingresa un Número: ")
a = int (a)
if a>=5 and a<=10:
    print (a," esta entre 5 y 10")

b=input("Ingresá un número que divida exactamente a 8: ")
b = int (b)
if b==1 or b==2 or b==4 or b==8:
    print("correcto")
else:
    print("incorrecto")
if not(b==1):
    print("El uno divide a todos exactamente")
'''
'''
# Segunda parte: in e is.
# Uso de in, verifica si un objeto existe dentro de un objeto iterable.
nombre = input ("Tu nombre?: ")
#nombre = str (nombre) ----EN ESTE CASO VO HACE FALTA CONVERTIRLO EN STRING----
# es case sensitive
if nombre in [ 'Charo', 'Mabel', 'Gustavo', 'Vlad']:
    print("Conozco ese nombre")
else:
    print("No lo conozco")
'''


# Uso de is, compara las instancias No los valores,
#(se refiere a los espacios de memoria que ocupan las variables)
a=[2,3,5]
b=[2,3,5]    
c=a
if a==b:
    print("a y b tienen el mismo valor")# acá se comparan valores

if a is b:
    print("a y b son la misma instancia")# acá se comparan espacios de memoria
else:
    print("a y b No son la misma instancia")

if c is a:
    print("a y c son la misma instancia")
else:
    print("a y c No son la misma instancia")
