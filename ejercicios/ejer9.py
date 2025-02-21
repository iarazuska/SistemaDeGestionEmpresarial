try:
    # Pedimos los números al usuario
    num1 = float(input("primer numero"))
    num2 = float(input("segundo numero"))

    # Intentamos dividir
    resultado = num1 / num2
    print(resultado)

# Si el usuario ingresa texto en vez de números
except ValueError:
    print("no vale ese numero")

# Si el usuario intenta dividir entre cero
except ZeroDivisionError:
    print("no se puede dividir entre 0")

