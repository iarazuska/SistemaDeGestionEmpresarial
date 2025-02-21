# Función para agregar un empleado
def nuevoEmpleado(lista, empleado):
    lista.append(empleado)

# Función para eliminar un empleado
def borraEmpleado(lista, empleado):
    if empleado in lista:
        lista.remove(empleado)

# Función para mostrar empleados
def verEmpleado(lista):
    print(sorted(lista))

# Lista de empleados
empleados = ["Ana", "Carlos", "Elena", "Javier", "María"]

# Usar funciones
nuevoEmpleado(empleados, "Luis")
borraEmpleado(empleados, "Carlos")
verEmpleado(empleados)
