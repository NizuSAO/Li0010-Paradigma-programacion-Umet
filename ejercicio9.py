# Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.
# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número: "))

# Calcular y mostrar la tabla de multiplicar del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")




