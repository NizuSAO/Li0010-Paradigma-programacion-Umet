#Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000 
#números aleatorios generados en el rango de[0,100.000].
import random

# Genera 10,000 números aleatorios en el rango [0, 100,000]
numeros_aleatorios = [random.randint(0, 100000) for _ in range(10000)]

# Inicializa una variable para almacenar el número mayor
numero_mayor = 0

# Recorre la lista de números aleatorios para encontrar el número mayor
for numero in numeros_aleatorios:
    if numero > numero_mayor:
        numero_mayor = numero

# Imprime el número mayor encontrado
print(f"El número mayor de los 10,000 números aleatorios es: {numero_mayor}")