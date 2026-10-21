from src.datos.temporada import temporada




def menu_actual_normal(): # si la temporada es la normal tenemos este menu

    print("opciones cambiar temporada")
    print("\n")

    print("0 mantener temporada actual")
    print("1 cambiar a temporada baja")
    print("2 cambiar a temporada alta")

    print("\n")
    opcion = int(input("escoge una opcion"))

    return opcion
    




def cambiar_si_actual_normal(): # si la actual es la normal mostramos esto

    opcion = menu_actual_normal()


    while(opcion < 0 or opcion > 2): # while para que el usuario escriba correctamente una opcion

            
        print("escoge una opcion correcta")
        opcion = menu_actual_normal()

    # dependiendo de la opcion se selecciona un valor u otro
    if (opcion == 1):
        temporada[0] = 0.5
        
    else:
        if (opcion == 2):
            temporada[0] = 1.5




def menu_actual_baja(): # si la temporada es la normal tenemos este menu

    print("opciones cambiar temporada")
    print("\n")

    print("0 mantener temporada actual")
    print("1 cambiar a temporada normal")
    print("2 cambiar a temporada alta")

    print("\n")
    opcion = int(input("escoge una opcion"))

    return opcion
    




def cambiar_si_actual_baja(): # si la actual es la normal mostramos esto

    opcion = menu_actual_baja()


    while(opcion < 0 or opcion > 2): # while para que el usuario escriba correctamente una opcion

            
        print("escoge una opcion correcta")
        opcion = menu_actual_baja()

    # dependiendo de la opcion se selecciona un valor u otro
    if (opcion == 1):
        temporada[0] = 1
        
    else:
        if (opcion == 2):
            temporada[0] = 1.5




def menu_actual_alta(): # si la temporada es la normal tenemos este menu

    print("opciones cambiar temporada")
    print("\n")

    print("0 mantener temporada actual")
    print("1 cambiar a temporada normal")
    print("2 cambiar a temporada baja")

    print("\n")
    opcion = int(input("escoge una opcion"))

    return opcion
    




def cambiar_si_actual_alta(): # si la actual es la normal mostramos esto

    opcion = menu_actual_alta()


    while(opcion < 0 or opcion > 2): # while para que el usuario escriba correctamente una opcion

            
        print("escoge una opcion correcta")
        opcion = menu_actual_alta()

    # dependiendo de la opcion se selecciona un valor u otro
    if (opcion == 1):
        temporada[0] = 1
        
    else:
        if (opcion == 2):
            temporada[0] = 0.5







# funcion que muestra la temporada actual
def mostrar_temporada_actual():

    temporada_actual = temporada[0] # temporada es un multiplicador que varia entre 1 , 0,5 y 1,5 dependiendo de la opcion la temporada es una u otra

    if (temporada_actual == 1):
        print("la temporada actual es la normal")

    else:
        if (temporada_actual == 0.5):
            print("la temporada actual es la baja")

        else:
            if (temporada_actual == 1.5): # si la temporada es alta cobramos mas
                print("la temporada actual es la alta")

    return temporada_actual







def cambiar_temporada():

   
    temporada_actual = mostrar_temporada_actual() # funcion que muestra la temporada actual en la que estamos

    # hacemos varios menus cada uno sera para escoger entre las dos opciones que no son la actual
    print("selecciona a que temporada quieres cambiar")

    if (temporada_actual == 1): # si la temporada es la normal

        cambiar_si_actual_normal()

    elif (temporada_actual == 0.5): # si la temporada es la baja

        cambiar_si_actual_baja()
    
    else: # temporada alta
        cambiar_si_actual_alta()
        

