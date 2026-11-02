from comun.try_except import comprovar_try_except


def modificar_gramos(ingredientes_gramos):

    contador = 0

    for clave, valor in ingredientes_gramos.items():

        contador = contador + 1

        print(contador, " producto: ", clave, " gramos: ", valor)

    opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")

    while(opcion < 1 or opcion > len(ingredientes_gramos)): # comprovamos que la opcion sea correcta

        contador = 0
        
        for clave, valor in ingredientes_gramos.items():
        
            contador = contador + 1
        
            print(contador, " producto: ", clave, " gramos: ", valor)

        
        opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")


    
    
    opcion_try_except = 0

    gramos = -1 
    while(opcion_try_except == 0):

        while(gramos < 0): # con este while nos aseguramos de que gramos sea > 0

            try:
                gramos = float(input("introduce cuantos gramos tiene ahora el producto"))

                opcion_try_except = 1 # la opcion vale 1 si el try except no ha salido
            
            except:
                print("introduce un valor correcto")

    # con gramso ahora correcto cambiamos los gramos

    contador = 0
    for clave, valor in ingredientes_gramos.items():

        contador = contador + 1

        if (contador == opcion): # si estamos en la opcion correcta cambiamos el valor

            ingredientes_gramos[clave] = gramos







def modificar_precio(ingredientes_precio):
    contador = 0
    
    for clave, valor in ingredientes_precio.items():
    
            contador = contador + 1
    
            print(contador, " producto: ", clave, " precio: ", valor)
    
    opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")
    
    while(opcion < 1 or opcion > len(ingredientes_precio)): # comprovamos que la opcion sea correcta
    
            contador = 0
            
            for clave, valor in ingredientes_precio.items():
            
                contador = contador + 1
            
                print(contador, " producto: ", clave, " precio: ", valor)
    
            
            opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")
    
    
        
        
    opcion_try_except = 0
    
    precio = -1 
    while(opcion_try_except == 0):
    
            while(precio < 0): # con este while nos aseguramos de que gramos sea > 0
    
                try:
                    precio = float(input("introduce cuantos precio tiene ahora el producto"))
    
                    opcion_try_except = 1 # la opcion vale 1 si el try except no ha salido
                
                except:
                    print("introduce un valor correcto")
    
    # con gramso ahora correcto cambiamos los gramos
    
    contador = 0
    for clave, valor in ingredientes_precio.items():
    
            contador = contador + 1
    
            if (contador == opcion): # si estamos en la opcion correcta cambiamos el valor
    
                ingredientes_precio[clave] = precio