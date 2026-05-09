nombre_curso = "Ultimate Python"
descripcion_curso = """
Este curso contempla todos los detalles
que necesitas apreander para encontrar
un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)
print(len(nombre_curso))  # longitud
# indices
print(nombre_curso[2])
print(nombre_curso[0:8])
print(nombre_curso[9:])
print(nombre_curso[:8])
print(nombre_curso[:])


texto = "Hola Mundo"
# indice 0123456789
print(texto.upper())
print(texto.lower())
print(texto.find("M"))
print(texto.find("Mund"))
# print(texto.replace("Mun","Cerdito feliz"))
nuevoTexto = texto.replace("Mun", "Cerdito Cantan")
print(texto, nuevoTexto)
print("Mundo" in texto)
