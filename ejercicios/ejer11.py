# Definir la clase Videojuego
class Videojuego:
    def __init__(self, nombre, genero, precio):
        self.nombre = nombre
        self.genero = genero
        self.precio = precio

    def mostrar_info(self):
        """Muestra la información del videojuego"""
        print(f"🎮 {self.nombre} - Género: {self.genero} - Precio: {self.precio:.2f}€")

    def aplicar_descuento(self, porcentaje):
        """Reduce el precio según el porcentaje de descuento"""
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"✅ Descuento aplicado. Nuevo precio de {self.nombre}: {self.precio:.2f}€")


# Crear catálogo de videojuegos
catalogo = [
    Videojuego("The Witcher 3", "RPG", 50),
    Videojuego("FIFA 23", "Deportes", 60),
    Videojuego("Cyberpunk 2077", "Acción", 55),
    Videojuego("Dark Souls III", "RPG", 40)
]

# Mostrar el catálogo inicial
print("\n📜 Catálogo de videojuegos:")
for juego in catalogo:
    juego.mostrar_info()

# Aplicar descuentos a los videojuegos
while True:
    nombre_juego = input("\n✏️ Escribe el nombre del videojuego para aplicar descuento (o 'salir' para terminar): ").strip()

    if nombre_juego.lower() == "salir":
        break  # Salimos del bucle si el usuario escribe "salir"

    encontrado = False  # Variable para saber si encontramos el juego

    for juego in catalogo:
        if juego.nombre.lower() == nombre_juego.lower():  # Comparamos sin importar mayúsculas
            try:
                descuento = float(input(f"🔻 Ingresa el porcentaje de descuento para {juego.nombre}: "))
                if descuento < 0 or descuento > 100:
                    print("⚠️ El descuento debe estar entre 0 y 100.")
                else:
                    juego.aplicar_descuento(descuento)
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")
            encontrado = True
            break

    if not encontrado:
        print("❌ Error: El videojuego no está en el catálogo.")

# Mostrar el catálogo actualizado
print("\n📢 Catálogo actualizado con descuentos:")
for juego in catalogo:
    juego.mostrar_info()
