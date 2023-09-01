#Desarrollar un programa que permita procesar funciones de un complejo de cines. 
#Por cada función se conoce:cantidad de espectadores y descuento(S/N).
#La carga termina cuando la cantidad de espectadores sea igual a 0(cero).
#El programa deberá:Calcular la recaudación total del complejo,
#considerando que el valor de la entrada e sde$50en los días con descuento y $75 en los días sin descuento.
#Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones
# Inicializamos las variables para contar funciones con y sin descuento
funciones_con_descuento = 0
funciones_sin_descuento = 0

# Inicializamos la variable para la recaudación total
recaudacion_total = 0

# Iteramos para procesar cada función
while True:
    # Pedimos la cantidad de espectadores
    cantidad_espectadores = int(input("Ingrese la cantidad de espectadores (0 para salir): "))
    
    # Verificamos si se debe salir del bucle
    if cantidad_espectadores == 0:
        break
    
    # Pedimos información sobre el descuento
    descuento = input("¿Hay descuento? (S/N): ").upper()
    
    # Calculamos el costo de la entrada y la recaudación para esta función
    if descuento == "S":
        costo_entrada = 50
        funciones_con_descuento += 1
    else:
        costo_entrada = 75
        funciones_sin_descuento += 1
    
    recaudacion_funcion = cantidad_espectadores * costo_entrada
    
    # Actualizamos la recaudación total
    recaudacion_total += recaudacion_funcion

# Calculamos el porcentaje de funciones con descuento
total_funciones = funciones_con_descuento + funciones_sin_descuento
porcentaje_descuento = (funciones_con_descuento / total_funciones) * 100 if total_funciones > 0 else 0

# Mostramos los resultados
print(f"Recaudación total del complejo: ${recaudacion_total}")
print(f"Funciones con descuento: {funciones_con_descuento}")
print(f"Porcentaje de funciones con descuento: {porcentaje_descuento:.2f}%")