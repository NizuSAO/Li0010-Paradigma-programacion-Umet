# Ventas por sucursal. Ingresar una serie de números por teclado que representan la cantidad de ventas 
# realizadas en las diferentes sucursales de un país de una determinada empresa. 
# Los requerimientos del programa son: Informar la cantidad de ventas ingresadas. 
# Total de ventas. Cantidad de ventas cuyo valores estén comprendidos entre 100 y 300 unidades.
# Cantidad de ventas con 400,500 y 600 unidades. 
# Indicar si hubo una cantidad de ventas inferior a 50 unidades. 
# Usted deberá ingresar cantidad es de ventas hasta que se ingrese un valor negativo. 
# Inicializamos las variables
ventas_totales = 0
ventas_entre_100_y_300 = 0
ventas_400 = 0
ventas_500 = 0
ventas_600 = 0
ventas_inferiores_a_50 = False


# Comenzamos a ingresar las ventas
while True:
    try:
        venta = int(input("Ingrese la cantidad de ventas (ingrese un número negativo para salir): "))
        if venta < 0:
            break  # Salir del bucle si se ingresa un número negativo
        ventas_totales += venta
        if 100 <= venta <= 300:
            ventas_entre_100_y_300 += 1
        if venta == 400:
            ventas_400 += 1
        if venta == 500:
            ventas_500 += 1
        if venta == 600:
            ventas_600 += 1
        if venta < 50:
            ventas_inferiores_a_50 = True
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Mostramos los resultados
print("Cantidad de ventas ingresadas:", ventas_totales)
print("Total de ventas:", ventas_totales)
print("Cantidad de ventas entre 100 y 300 unidades:", ventas_entre_100_y_300)
print("Cantidad de ventas de 400 unidades:", ventas_400)
print("Cantidad de ventas de 500 unidades:", ventas_500)
print("Cantidad de ventas de 600 unidades:", ventas_600)
if ventas_inferiores_a_50:
    print("Hubo ventas inferiores a 50 unidades.")
else:
    print("No hubo ventas inferiores a 50 unidades.")