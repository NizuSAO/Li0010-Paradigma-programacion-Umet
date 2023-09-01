#Escriba un programa que transforme todas las letras de una palabra en mayúsculas, minúsculas y la primera con minúsculas(capitalización).

def transformar_palabra(palabra):
    # Transformar a mayúsculas
    mayusculas = palabra.upper()
    
    # Transformar a minúsculas
    minusculas = palabra.lower()
    
    # Capitalizar la primera letra
    capitalizada = palabra.capitalize()
    
    return mayusculas, minusculas, capitalizada

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Llamar a la función y mostrar los resultados
mayusculas, minusculas, capitalizada = transformar_palabra(palabra)

print("En mayúsculas:", mayusculas)
print("En minúsculas:", minusculas)
print("Capitalizada:", capitalizada)
