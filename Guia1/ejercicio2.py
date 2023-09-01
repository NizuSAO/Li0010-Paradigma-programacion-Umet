nombre_de_usuario= str(input("ingrese el nombre de usuario: "))

cantidad_de_letras = len(nombre_de_usuario)

if cantidad_de_letras % 2 == 0:
    print(f"El nombre del usuario '{nombre_de_usuario}' es par")
else:
    print(f"El nombre del usuario '{nombre_de_usuario}' es impar")
    