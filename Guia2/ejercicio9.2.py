import random
#Promedio de números aleatorios: Realice un programa que permita calcular
# el promedio de 1000 números aleatorios generados en el rango de[0,100000].
# Generar una lista de 1000 números aleatorios en el rango [0, 100000]
numeros_aleatorios = [random.randint(0, 100000) for _ in range(1000)]

# Calcular el promedio
promedio = sum(numeros_aleatorios) / len(numeros_aleatorios)

# Imprimir el promedio
print(f"El promedio de los 1000 números aleatorios es: {promedio}")