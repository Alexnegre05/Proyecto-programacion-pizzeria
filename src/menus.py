from src.modulos.try_except import comprovar_try_except



# menu principal devuelve opcion
def menu_principal():

    print("\n")

    print("menu")

    print("opcion 0 salir")

    print("opcion 1 pizzas")

    print("opcion 2 bebidas")

    print("opcion 3 otros")

    
    opcion = comprovar_try_except("selecciona una opcion de el menu: ")

    while (opcion < 0 or opcion > 3): # while que compreuba si el usuario ah introducido un numero correcto
    # si no lo hace vuelve a mostra el menu con las opciones

        print("\n")

        print("menu")

        print("opcion 0 salir")

        print("opcion 1 pizzas")

        print("opcion 2 bebidas")

        print("opcion 3 otros") # aqui añadimos todo lo referente a ofertas, temporadas...

        opcion = comprovar_try_except("selecciona una opcion correcta de el menu: ")
       

    return opcion # devolvemos la opcion







# menu de solo pizas
def menu_pizzas():

    print("\n")

    print("menu")

    print("opcion 0 salir")

    print("opcion 1 mirar pizzas")  # muestra todas las pizza

    print("opcion 2 seleccionar pizza") # aqui la podemos añadir a el carrito una pizza, la cantidad de gramos totales y el desglose de precios
    
    print("opcion 3 seleccionar ingredientes") # podemos ver los ingredienets y su coste


    opcion = comprovar_try_except("selecciona una opcion de el menu: ")

    

    while (opcion < 0 or opcion > 3): # comprovamos que la opcion sea correcta si no lo es volvemos a mostrar el menu

        print("\n")

        print("menu")

        print("opcion 0 salir")
        
        print("opcion 1 mirar pizzas")  
        
        print("opcion 2 seleccionar pizza")  
        
        print("opcion 3 seleccionar ingredientes") 

        opcion = comprovar_try_except("selecciona una opcion correcta de el menu: ")
    
    return opcion # devolvemos la opcion






def menu_bebidas():
    
    print("\n")

    print("menu")

    print("opcion 0 salir")
    
    print("opcion 1 mirar bebidas")
    
    print("opcion 2 seleccionar bebidas")

    opcion = comprovar_try_except("selecciona una opcion de el menu: ")

    while (opcion < 0 or opcion > 2): # comprovamos que la opcion sea correcta si no lo es volvemos a mostrar el menu

        print("\n")

        print("menu")

        print("opcion 0 salir")
        
        print("opcion 1 mirar bebidas")
        
        print("opcion 2 seleccionar bebidas")

        opcion = comprovar_try_except("selecciona una opcion correcta de el menu: ")

    return opcion # devolvemos la ocpion





# menu de otras opciones
def menu_otros():

    print("\n")

    print("opcion 0 salir")
    
    print("opcion 1 ofertas") # para poder seleccionar ofertas
    
    print("opcion 2 seleccionar temporada") # para poder seleccionar entre una de 3 temporadas
    
    print("opcion 3 carrito") # para quitar cosas de el carrito y ver lo que hay
    
    print("opcion 4 tiquet final") # para ver el tiquet final

    opcion = comprovar_try_except("selecciona una opcion de el menu: ")

    while (opcion < 0 or opcion > 4):  # comprovamos que la opcion sea correcta si no lo es volvemos a mostrar el menu
        
        print("\n")

        print("menu")

        print("opcion 0 salir")
        
        print("opcion 1 ofertas")
        
        print("opcion 2 seleccionar temporada")
        
        print("opcion 3 carrito") 
        
        print("opcion 4 tiquet final")

        opcion = comprovar_try_except("selecciona una opcion correcta de el menu: ")

    return opcion  # devolvemos la opcion


def menu():

   

    opcion = menu_principal()
    # seleccionamos con cada menu un submenu

    # si la opcion es 0 salimos de aqui(llegamos a el final)
    if (opcion != 0):

        if (opcion == 1):
           
           menu_pizzas()

        elif (opcion == 2):

            menu_bebidas()

        else: # opcion 3

            menu_otros()
