# saludo = "Hola Global"  # Es una mala practica usar variables de este modo


def saludar():
    # global saludo
    saludo = "Hola Mundo"
    print(saludo)


def saludaCerdito():
    saludo = "Hola Cerdito"
    print(saludo)


saludar()
saludaCerdito()

# print(saludo)
