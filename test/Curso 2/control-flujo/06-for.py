# iterando valores con For
for numero in range(5):  # rangle es un iterable, como listas y duplas
    print(numero, numero * 'happy ')

buscar = 3
for numero2 in range(5):
    if numero2 == buscar:
        print("encontrado", buscar)
        break  # detiene la ejecucion en el 3

buscar3 = 10
for numero3 in range(5):
    print(numero3)
    if numero3 == buscar3:
        print("encontrado", buscar3)
        break
else:
    print("No encontre el numero buscado")

for char in "Ultimate python":
    print(char)
