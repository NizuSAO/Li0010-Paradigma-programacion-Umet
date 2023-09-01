# Solicitar al usuario el valor de la base
base = float(input("Ingrese el valor de la base del triángulo: "))

# Calcular la altura (altura = base^2)
altura = base ** 2

# Calcular el área del triángulo
area = (base * altura) / 2

# Imprimir el resultado
print(f"El área del triángulo con base {base} y altura {altura} es: {area}")