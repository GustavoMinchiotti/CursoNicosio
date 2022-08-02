# Definimos la clase

class Persona:
    """esta es la clase para personas"""  # este es el doc string

    # Atributo público
    valor = 0

    # Atributo privado
    _dato = 20

    # No hay constructor explícito, pero usamos _init_
    def __init__(self, nombre, edad):  # self va siempre, hace referencia al obj.
        print("estamos en __init__")
        self.Nombre = nombre  # Así se crean los atributos
        self.Edad = edad

    # Definimos un método
    def muestra(self):
        print('Mi nombre es ', self.Nombre)  # las invoco con self porque son del obj. no globales
        print('Mi edad es ', self.Edad)
        print('El valor guardado es ', self.valor)
        print('El dato es ', self._dato)
        print('------------')

    # No hay destructor explícito, pero usamos __del__
    def __del__(self):
        print('Bye desde: ', self.Nombre)


# Imprimimos el doc string
print(Persona.__doc__)

# Creamos la instancia
persona1 = Persona('Aldo', 18)
print('imprimo un solo atributo', persona1.Nombre)

# Accedemos a atributo
persona1.valor = 5
print('------------' * 5)
# Invocamos método
persona1.muestra()

# Creamos otra instancia
person2 = Persona('Ana', 20)
# Eliminamos la otra instancia
del persona1
print('------------' * 5)
person2.muestra()
