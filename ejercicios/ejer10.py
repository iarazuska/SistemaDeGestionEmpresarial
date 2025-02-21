class Empleado:
    def __init__(self, nombre, dni, fecha_alta):
        self.nombre = nombre
        self.dni = dni
        self.fecha_alta = fecha_alta

    def mostrar_info(self):
        print(f"empleado {self.nombre}, dni {self.dni}, fecha {self.fecha_alta}")

    def cambiar_fecha_alta(self, nueva_fecha):
        self.fecha_alta = nueva_fecha

# Crear empleados
empleado1 = Empleado("juan", "12345678A", "01/02/2020")
empleado2 = Empleado("marta", "87654321B", "15/06/2019")

# Cambiar fecha de alta de un empleado
empleado1.cambiar_fecha_alta("01/01/2023")

# Mostrar información
empleado1.mostrar_info()
empleado2.mostrar_info()
