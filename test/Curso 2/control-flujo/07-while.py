numero = 1
while numero <= 100:
    print(numero)
    numero *= 2

# ejemplo para usar instrucciones en la linea de comando o terminal
comando = ""

while comando != "salir":
    comando = input("$ ").lower()  # interprete de linea de comando
    print(comando)

while True:  # loops infinitos necesitan siempre un break
    comando = input("$ ")  # interprete de linea de comando
    print(comando)
    if comando.lower() == "salir":
        break
