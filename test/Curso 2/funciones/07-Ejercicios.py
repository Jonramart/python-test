def palindromo(texto):
    palabra = ""
    for char in texto:
        palabra += char
        # print(palabra)
    return palabra


print("Abba", palindromo("Abba"))
# print("Reconocer", palindromo("reconocer"))
# print("Amo la paloma", palindromo("Amo la paloma"))
# print("Hola Mundo", palindromo("hola mundo"))
