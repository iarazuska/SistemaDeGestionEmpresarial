# Usamos un bucle para contar hacia abajo
for i in range(10, 0, -1):  # Comienza en 10, termina en 1, va restando 1
    for j in range(1, i + 1):  # Imprime desde 1 hasta i
        print(j, end=" ")
    print()  # Salto de línea
