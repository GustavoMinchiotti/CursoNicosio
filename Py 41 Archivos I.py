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
archivo=open('practicaArchivos2.txt','a')
n=0

# Escribimos 5 letras
while n<5:
    texto=input('Dame un texto ')
    archivo.write(texto+'\n') #con esta funcion escribe una letra por linea.
    n=n+1

# cerramos el archivo
archivo.close()
