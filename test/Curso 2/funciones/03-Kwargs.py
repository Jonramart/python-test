def get_product(**datos):  # key words arguments
    print(datos)
    print(datos["id"])
    print(datos["id"], datos["name"])


# se necesita agregar el nombre del parametro y el valor
get_product(id="id",
            name="Iphone",
            desc="Esto es un Iphone")
