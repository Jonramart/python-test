print("hola mundo " * 2)


def hola(nombre, apellido="Feliz"):  # funciones y parametros
    print("Hola Mundo")
    print("Ultimate Python")
    print(f"Bienvenido {nombre} {apellido}")  # parametro


hola("Nicolas", "schumann")  # argumentos son los valores pasados a la funcion
# No se agrego el segundo argumento y de todos modos se manda el segundo parametro
hola("Pipen")

# argumentos nombrados
hola(apellido="Ramos", nombre="Jon")
