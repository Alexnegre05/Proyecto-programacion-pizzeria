from comun.try_except import comprovar_try_except 



        
def mostrar_carrito(lista_producto):

        
        if (len(lista_producto) != 0): # si hay elementos en el carrito

            fotmat_carrito ="\n CARRITO:\n "

            for producto in lista_producto:
                fotmat_carrito += f"Producto:{producto[0]}, Precio: {producto[1]}\n"
            return fotmat_carrito

        else:
            return "\n no hay elementos en el carrito \n"



def quitar_producto_carrito(lista_producto):


        for i in range(0, len(lista_producto)):

            print(i + 1, "-Producto: ", lista_producto[i][0], "Precio: ", lista_producto[i][1])

            # mostramos el carrito pero con un numero indexado, es i + 1 para que empieze desde 1

        opcion = comprovar_try_except("\n selecciona el numero de el producto que quieres quitar, 0 para salir: ")

        # con esto el usuario escribe una opcion

        while(opcion < 0 or opcion > len(lista_producto)): # en caso de que el numero no exista
            
            for i in range(0, len(lista_producto)):
            
                    print(i + 1, "-Producto: ", lista_producto[i][0], "Precio: ", lista_producto[i][1])
            
            opcion = comprovar_try_except("\n selecciona el numero correcto de el producto que quieres quitar, 0 para salir: ")


        # si la opcion es 0 como hay que salir devolvemos directamente la lista sin modificar nada
        if (opcion == 0):
            return lista_producto

        else:

            lista_producto.pop(opcion - 1) # esto elimina por indice, como el usuario no empieza desde 1 sino desde 0 hacemos opcion - 1

            return lista_producto # devolvemos la lista