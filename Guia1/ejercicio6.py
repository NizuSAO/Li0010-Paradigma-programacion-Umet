# Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado). 
# Solicita al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Obtiene el último dígito
ultimo_digito = numero % 10

# Obtiene los dos últimos dígitos
dos_ultimos_digitos = numero % 100

# Muestra el último dígito y los dos últimos dígitos
print(f"El último dígito es: {ultimo_digito}")
print(f"Los dos últimos dígitos son: {dos_ultimos_digitos}")