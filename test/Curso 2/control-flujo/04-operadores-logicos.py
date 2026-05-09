# and , or , not

edad = 22

print(edad > 18 and edad < 30)
print(edad > 18 or edad < 30)
print(not (edad > 17))

gas = True
encendido = True
gas2 = False
encendido2 = True
gas3 = False
encendido3 = True
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar")

if gas2 and (encendido2 or edad > 17):
    print("Puedes avanzar2")

if not gas2 and (encendido2 or edad > 17):
    print("Puedes avanzar3")

# operacion de corto circuito And deben de ser True el primero de la izquierda pra ejecutar todo a la derecha
if not gas3 and encendido3 and edad > 17:
    print("Puedes avanzar3")
if not gas3 or encendido3 or edad > 17:  # operacion de corto circuito con OR la primera condicione debe ser false para ejecutar todo lo de la derecha
    print("Puedes avanzar4")
