print("menu")

print("opcion 0 salir")
print("opcion 1 pizzas")
print("opcion 2 bebidas")
print("opcion 3 otros")

opcion = int(input("selecciona una opcion de el menu: "))

while (opcion < 0 or opcion > 3): # while que compreuba si el usuario ah introducido un numero correcto
# si no lo hace vuelve a mostra el menu con las opciones

    print("menu")

    print("opcion 0 salir")
    print("opcion 1 pizzas")
    print("opcion 2 bebidas")
    print("opcion 3 otros")

    opcion = int(input("selecciona una opcion correcta de el menu: "))


# seleccioanmos con cada menu un submenu

# si la opcion es 0 salimos de aqui(llegamos a el final)
if (opcion != 0):

    if (opcion == 1):
        
        print("opcion 0 salir")
        print("opcion 1 mirar pizzas")  # muestra todas las pizzas
        print("opcion 2 seleccionar pizza") # aqui la podemos añadir a el carrito una pizza, la cantidad de gramos totales y el desglose de precios
        print("opcion 3 seleccionar ingredientes") # podemos ver los ingredienets y su coste


        opcion = int(input("selecciona una opcion de el menu: "))

        while (opcion < 0 or opcion > 3): 

            print("menu")

            print("opcion 0 salir")
            print("opcion 1 mirar pizzas")  
            print("opcion 2 seleccionar pizza")  
            print("opcion 3 seleccionar ingredientes") 

            opcion = int(input("selecciona una opcion correcta de el menu: "))

    elif (opcion == 2):

        print("menu")

        print("opcion 0 salir")
        print("opcion 1 mirar bebidas")
        print("opcion 2 seleccionar bebidas")

        opcion = int(input("selecciona una opcion de el menu: "))

        while (opcion < 0 or opcion > 2): 

            print("menu")

            print("opcion 0 salir")
            print("opcion 1 mirar bebidas")
            print("opcion 2 seleccionar bebidas")

            opcion = int(input("selecciona una opcion correcta de el menu: "))

    else: # opcion 3

        print("opcion 0 salir")
        print("opcion 1 ofertas") # para poder seleccionar ofertas
        print("opcion 2 seleccionar temporada") # para poder seleccionar entre una de 3 temporadas
        print("opcion 3 carrito") # para quitar cosas de el carrito y ver lo que hay
        print("opcion 4 tiquet final") # para ver el tiquet final

        opcion = int(input("selecciona una opcion de el menu: "))

        while (opcion < 0 or opcion > 4): 

            print("menu")

            print("opcion 0 salir")
            print("opcion 1 ofertas")
            print("opcion 2 seleccionar temporada")
            print("opcion 3 carrito") 
            print("opcion 4 tiquet final")

            opcion = int(input("selecciona una opcion correcta de el menu: "))

 
