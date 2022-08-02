class Persona:
    
    # Atributo público
    valor = 0

    # Atributo privado
    _dato = 20
 
    def __init__(self, nombre, edad):  
        print("estamos en __init__")
        self.__Nombre = nombre  
        self.Edad = edad

    def get_dato(self):
        return self._dato

    def set_dato(self, pDato):
        print('En propiedad')
        self._dato = pDato

        
    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self, pDato):
        self.__Nombre = pDato 

# Hacemos uso de funciones de interfaz
persona1 = Persona('y', 20)
print(persona1.Nombre)


persona1.Nombre = 'susana'
print(persona1.Nombre)

persona1.set_dato(67)

print(persona1._dato)  
