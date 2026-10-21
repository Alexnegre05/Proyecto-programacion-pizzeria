def mostrar_carrito(lista_producto):
    fotmat_carrito ="\n CARRITO:\n "

    for producto in lista_producto:
        fotmat_carrito += f"Producto:{producto[0]}, Precio: {producto[1]}\n"
    return fotmat_carrito