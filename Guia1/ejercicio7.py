#Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas pulgadas cenơmetros metros 
#Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro = 1000.

def convertir_medida_pies(medida_pies):
    # Convertir pies a yardas, pulgadas, centímetros y metros
    yardas = medida_pies / 3.0
    pulgadas = medida_pies * 12.0
    centimetros = pulgadas * 2.54
    metros = centimetros / 100.0
    
    return yardas, pulgadas, centimetros, metros

# Solicitar al usuario la medida en pies
medida_pies = float(input("Ingrese la medida en pies: "))

# Llamar a la función para realizar las conversiones
yardas, pulgadas, centimetros, metros = convertir_medida_pies(medida_pies)

# Mostrar los resultados
print(f"{medida_pies} pies equivalen a:")
print(f"{yardas} yardas")
print(f"{pulgadas} pulgadas")
print(f"{centimetros} centímetros")
print(f"{metros} metros")