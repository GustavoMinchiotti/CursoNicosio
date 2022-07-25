class Persona:
    """Esta es la clase para personas"""

    # Variable de clase
    cantidad = 0;

    # Atributo publico
    valor = 0

    # Atributo privado
    __dato = 20

    # Usamos __init__ para  inicializar
    def __init__(self, nombre, edad):
        # print ('estamos en __init__')
        self.Nombre = nombre
        self.Edad = edad

    # Definimos un metodo
    def muestra(self):
        print('Mi nombre es ', self.Nombre)
        print('Mi edad es ', self.Edad)
        print('el valor guardado es ', self.valor)
        print('el dato es ', self.__dato)
        print('La cantidad es ', Persona.cantidad)  # Uso la variable de clase
        print('-------------' * 4)

    # Otro método
    def muestraSaludo(self):
        print('hola, soy ', self.Nombre)

    # Método para la variable de clase (modifica la variable)
    def ponCantidad(self, cant):
        Persona.cantidad = cant

    # No hay destructor explícito, pero usamos __del__
    def __del__(self):
        print('bye desde: ', self.Nombre)  # la instancia a destruir


# Hacemos una herencia
class Empleado(Persona):
    # Atributo de empleado
    sueldo = 0

    # Inicialización
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        self.sueldo = salario

    # Método que aprovecha el método de la clase padre
    def muestraEmpleado(self):
        Persona.muestra(self)
        print('El sueldo es ', self.sueldo)

    # Override a un método
    def muestraSaludo(self):
        print('Hola, tengo trabajo y soy ', self.Nombre)


# Probamos la variable de clase
per1 = Persona('Aldo', 18)
per2 = Persona('Ana', 20)

per1.valor = 50

per1.muestra()
per2.muestra()

print('Ponemos cantidad')
per1.ponCantidad(100)
print('-------------' * 4)

per1.muestra()
per2.muestra()

# Probamos la clase con herencia
empleado1 = Empleado('Juan', 25, 50000)

empleado1.muestraEmpleado()
empleado1.muestraSaludo()
