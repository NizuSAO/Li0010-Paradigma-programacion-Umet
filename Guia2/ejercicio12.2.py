#Números pares e impares Se pide desarrollar un programa que permita leer una serie de números. 
#La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo. 
#Los requerimientos funcionales del programa son: 
#La sumatoria de solo los números que estén comprendidos entre 50 y 100. 
#Cantidad de valores pares ingresados. Cantidad de valores impares ingresados.
#Informar si en la carga de números se ingreso al menos un número 0. 
#Informar si la serie contiene solo números pares e impares alternados. 
#Inicializamos las variables
suma_entre_50_y_100 = 0
cantidad_pares = 0
cantidad_impares = 0
contiene_cero = False
alternados = True

# Pedir números al usuario hasta que ingrese un número negativo
while True:
    numero = int(input("Ingrese un número (negativo para terminar): "))
    
    if numero < 0:
        break  # Salir del bucle si se ingresa un número negativo
    
    if numero >= 50 and numero <= 100:
        suma_entre_50_y_100 += numero
    
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    
    if numero == 0:
        contiene_cero = True
    
    if alternados and ((numero % 2 == 0 and cantidad_impares > 0) or (numero % 2 != 0 and cantidad_pares > 0)):
        alternados = False

# Mostrar resultados
print(f"La sumatoria de números entre 50 y 100 es: {suma_entre_50_y_100}")
print(f"Cantidad de números pares ingresados: {cantidad_pares}")
print(f"Cantidad de números impares ingresados: {cantidad_impares}")

if contiene_cero:
    print("Se ingresó al menos un número 0.")
else:
    print("No se ingresó ningún número 0.")

if alternados:
    print("La serie contiene solo números pares e impares alternados.")
else:
    print("La serie no contiene solo números pares e impares alternados.")