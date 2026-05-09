print("Bienvenidos a la calculadora")
print("Para salir escriba Salir")
print("Las operaciones son suma, resta, multi y div")
valor = input("ingresa un numero: ")

while True:
    operacion = input("ingrese la operacion: ").lower()
    if operacion.lower() == "salir":
        break
    elif operacion == "suma":
        num_sig = int(input(("ingresa el siguiente numero: ")))
        valor = int(valor)
        valor += num_sig
    elif operacion == "resta":
        num_sig = int(input(("ingresa el siguiente numero: ")))
        valor -= num_sig
    elif operacion == "multi":
        num_sig = int(input(("ingresa el siguiente numero: ")))
        valor *= num_sig
    elif operacion == "div":
        num_sig = int(input("ingresa el siguiente numero: "))
        valor /= num_sig
    else:
        print("Operacion no valida")
        break
    print(f"El resultado es {valor}")
