# Diccionario con información del producto
producto = {
    "nombre": "portatil",
    "precio": 1200,
    "stock": 15,
    "fabricacion": "20/01/2003"
}

# Reducir el precio a la mitad
producto["precio"] /= 2

# Eliminar el stock
del producto["stock"]

# Mostrar la información
print("info")
for clave, valor in producto.items():
    print(clave , valor)
