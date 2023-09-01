# Función para generar los primeros n números de la sucesión de Fibonacci
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Solicitar al usuario la cantidad de números a mostrar
n = int(input("Ingrese la cantidad de números de la sucesión de Fibonacci a mostrar: "))

# Llamar a la función e imprimir la secuencia
result = fibonacci(n)
print(result)