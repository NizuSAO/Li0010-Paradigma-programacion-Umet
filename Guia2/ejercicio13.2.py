#Desarrollar un programa que permita procesar los datos del último censo de un apequeña población.
#Por cada habitantes e ingresa:sexo(M/F)y edad. 
#La carga de datos analiza al ingresar cualquier otro valor para sexo.
#El programa debe informar:Aqué sexo corresponde la mayor cantidad de 
#habitantes(considerar que puede ser igual)Cantidad de mujeres en edad escolar(4 a 18 años inclusive)
#Si hay algún varón que supere los 80 años de edad. 
#Inicializamos las variables
cantidad_hombres = 0
cantidad_mujeres = 0
cantidad_mujeres_escolar = 0
hay_varon_mayor_80 = False
sexo_mayor_cantidad = None

# Pedir datos de habitantes hasta que se ingrese otro valor para el sexo
while True:
    sexo = input("Ingrese sexo (M/F) o cualquier otro valor para terminar: ").upper()
    
    if sexo != 'M' and sexo != 'F':
        break  # Salir del bucle si se ingresa un valor diferente de M o F
    
    edad = int(input("Ingrese la edad: "))
    
    if sexo == 'M':
        cantidad_hombres += 1
        if edad > 80:
            hay_varon_mayor_80 = True
    elif sexo == 'F':
        cantidad_mujeres += 1
        if 4 <= edad <= 18:
            cantidad_mujeres_escolar += 1

# Determinar qué sexo tiene la mayor cantidad de habitantes
if cantidad_hombres > cantidad_mujeres:
    sexo_mayor_cantidad = 'Masculino'
elif cantidad_mujeres > cantidad_hombres:
    sexo_mayor_cantidad = 'Femenino'
else:
    sexo_mayor_cantidad = 'Igual cantidad de hombres y mujeres'

# Mostrar resultados
print(f"Sexo con mayor cantidad de habitantes: {sexo_mayor_cantidad}")
print(f"Cantidad de mujeres en edad escolar (4 a 18 años inclusive): {cantidad_mujeres_escolar}")

if hay_varon_mayor_80:
    print("Hay al menos un varón que supera los 80 años de edad.")
else:
    print("No hay varones que superen los 80 años de edad.")