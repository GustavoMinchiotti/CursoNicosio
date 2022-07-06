# Lectura de archivos

# r - solo lectura
# rb - solo lectura en formato binario
# r+ - lectura y escritura, apuntador al inicio del archivo
# rb+ - igual que el anterior pero binario
# w - solo escritura
# wb - solo escritura binario
# w+ - escritura y lectura, sobre escribe el archivo si existe
# wb+ - igual al anterior pero en binario
# a - abre para append (adicion), el apuntador al final del archivo
# ab - igual pero binario
# a+ - abre para append o lectura, el apuntador al final del archivo
# ab+ - igual pero en binario

# Abrimos el archivo para lectura

archivo=open('practicaArchivos.txt','r')

# Recorremos el archivo linea por linea
for linea in archivo:
    print(linea.rstrip())

print('Nombre: ', archivo.name)
print('Cerrado? : ',archivo.closed)
print('Modo de apertura: ', archivo.mode)

# Cerramos el archivo --IMPORTANTE-- siempre se deben cerrar los archivos luego de usarlos
archivo.close()

print('/*-/*-/-*/*-/*-/*-/*-')

# Abrimos el archivo para escritura  - uno nuevo...
'''archivo=open('practicaArchivos2.txt','w')
n=0

# Escribimos 5 letras
while n<5:
    texto=input('Dame un texto ')
    archivo.write(texto+'\n') #con esta funcion escribe una letra por linea.
    n=n+1

# cerramos el archivo
archivo.close()'''


####### archivos II #####
print('<<<<<<<<<<clase archivos II >>>>>>>>>>>')
# Abrir el archivo a una lista
lista = open('practicaArchivos.txt', 'r').readlines()
print(lista)
print('----------------------'*3)

# Ver la posicion
archivo=open('practicaArchivos.txt','r')
pos=archivo.tell()
print('posicion inicial sin modificar ',pos)

# Colocamos en una posc. determinada
# 0 - inicio
# 1 - posicion actual
# 2 - final del archivo

archivo.seek(5,0)
cadena=archivo.read(8)
print('cadena: ',cadena)
pos=archivo.tell()
print('posicion luego de utilizar .seek ',pos)

archivo.close()
print('----------------------'*3)

# Serializacion
# tres protocolos, 0-ascii, 1-compacto, 2-clases optimizadas (ver en py 3.X)

# importamos el modulo PICKLE

import pickle

# crear el objeto a serializar
lista1=[5,'hola']
lista2=[7.8,'Python',True]

# abro para escritura
archivo5=open('misdatos.dato','wb') # importante Wb para guardar como binario

# hago la serializacion
pickle.dump(lista1,archivo5)
pickle.dump(lista2,archivo5)
print(lista1, ' sin serializar')
print(archivo5, '  Archivo serializado OBJETO')
print('\n')
archivo5.close()

# Deserializamos

archivo5=open('misdatos.dato','rb') # leer binario
lst1=pickle.load(archivo5)
lst2=pickle.load(archivo5)

print(lst1)
print(lst2)
