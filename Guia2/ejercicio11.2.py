#Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que 
#permita:Determinar el menor de los numeros genera dos en forma aleatoria.
#Calcular el valor promedio de los números menores a 10.000.
import random

# Generar 5000 números aleatorios
numeros_aleatorios = [random.randint(0, 100000) for _ in range(5000)]

# Encontrar el número más pequeño
numero_menor = min(numeros_aleatorios)

# Calcular el valor promedio de los números menores a 10,000
numeros_menor_10000 = [num for num in numeros_aleatorios if num < 10000]
promedio_menor_10000 = sum(numeros_menor_10000) / len(numeros_menor_10000)

# Imprimir resultados
print(f"El número más pequeño generado es: {numero_menor}")
print(f"El valor promedio de los números menores a 10,000 es: {promedio_menor_10000}")