# Uso de slots y atributos dinámicos
# Nuestra clase debe descender de object

class Persona(object): 
    """esta es la clase para personas"""  
    # Usar __slots__ para evitar los atributos dinámicos
    __slots__=('Nombre','Edad')

    # No hay constructor explícito, pero usamos _init_
    def __init__(self, nombre, edad):
        print("estamos en __init__")
        self.Nombre = nombre  
        self.Edad = edad

    # Definimos un método
    def muestra(self):
        print('Mi nombre es ', self.Nombre) 
        print('Mi edad es ', self.Edad)
        print('------------')

    # No hay destructor explícito, pero usamos __del__
    def __del__(self):
        print('Bye desde: ', self.Nombre)

     
persona1 = Persona('Aye', 20)
persona1.muestra()

# Creamos un atributo dinámico

persona1.peso=60
print(persona1.peso)
