# Método estático
# Método de clase
# Funciones de interfaz
# Propiedades


class Persona:
    """esta es la clase para personas"""  # este es el doc string
    # Atributo público
    valor = 0
    # Atributo privado
    _dato = 20

    # No hay constructor explícito, pero usamos _init_
    def __init__(self, nombre, edad):  # self va siempre, hace referencia al obj.
        print("estamos en __init__")
        self.__Nombre = nombre  # Así se crean los atributos
        self.Edad = edad

    # Definimos un método
    def muestra(self):
        print('Mi nombre es ', self.__Nombre)  # las invoco con self porque son del obj. no globales
        print('Mi edad es ', self.Edad)
        print('El valor guardado es ', self.valor)
        print('El dato es ', self._dato)
        print('------------')

    # No hay destructor explícito, pero usamos __del__
    def __del__(self):
        print('Bye desde: ', self.__Nombre)

    # Creamos un metodo estático
    @staticmethod
    def mensaje(msg):
        print('tienes este mensaje estatico: ', msg)

    # Creamos un metodo de clase
    # se usan en el patron fabrica
    @classmethod
    def autor(cls):
        print('La clase ', cls.__name__)
        print('fue creada por Gustavo')

    # Creamos funciones de interfaz para __dato
    def get_dato(self):
        return self._dato

    def set_dato(self, pDato):
        print('En propiedad')
        self._dato = pDato

    # Creamos propiedades para Nombre

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self, pDato):
        self.__Nombre=pDato 

# Hacemos uso de funciones de interfaz
persona1 = Persona('Aye', 20)
persona1.muestra()
persona1.Nombre = 'Gustavo'
persona1.muestra()

persona1.set_dato(67)

persona1.muestra()
# Hacemos uso de propiedades
p= persona1
p.Nombre = 'Charo'
print(p.muestra())
# Uso de los métodos
Persona.mensaje('msg insertado')
Persona.autor()
