print("Bienvenidos a la calculadora")
print("Para salir escriba Salir")
print("Las operaciones son suma, resta, multi y div")
valor = input("ingresa un numero: ")

while True:
    operacion = input("ingrese la operacion: ").lower()
    if operacion.lower() == "salir":
        break
    elif operacion == "suma":
        valor = int(valor)
        num_sig = int(input(("ingresa el siguiente numero: ")))
        # suma = num_ini + num_sig
        valor += num_sig
        # valor = suma
        print("El resultado es ", valor)
    elif operacion == "resta":
        num_sig = int(input(("ingresa el siguiente numero: ")))
        resta = valor - num_sig
        valor = resta
        print("El resultado es ", resta)
    elif operacion == "multi":
        num_sig = int(input(("ingresa el siguiente numero: ")))
        prod = valor * num_sig
        valor = prod
        print("El resultado es ", prod)
    elif operacion == "div":
        num_sig = int(input("ingresa el siguiente numero: "))
        div = float(valor / num_sig)
        valor = div
        print("El resultado es ", div)
    # print("loop infinito")
    # break
