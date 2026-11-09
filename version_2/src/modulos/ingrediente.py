from comun.try_except import comprovar_try_except



class Ingrediente:
    def __init__(self,nombre, precio, gramos):

        self.precio = precio
        self.gramos = gramos
        self.nombre = nombre

    

def modificar_gramos_v2(lista_ingredientes):

        contador = 0

        for i in range(0, len(lista_ingredientes)):

            contador = contador + 1

            print(contador, " producto: ", lista_ingredientes[i].nombre, " gramos: ", lista_ingredientes[i].gramos)

        opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")

        while(opcion < 1 or opcion > len(lista_ingredientes)): # comprovamos que la opcion sea correcta

            contador = 0
            
            for i in range(0, len(lista_ingredientes)):

                contador = contador + 1

                print(contador, " producto: ", lista_ingredientes[i].nombre, " gramos: ", lista_ingredientes[i].gramos)

            
            opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")


        
        
        opcion_try_except = 0

        gramos_cambio = -1 
        while(opcion_try_except == 0):

            while(gramos_cambio < 0): # con este while nos aseguramos de que gramos sea > 0

                try:
                    gramos_cambio = float(input("introduce cuantos gramos tiene ahora el producto"))

                    opcion_try_except = 1 # la opcion vale 1 si el try except no ha salido
                
                except:
                    print("introduce un valor correcto")

        # con gramso ahora correcto cambiamos los gramos

        contador = 0
        
        for i in range(0, len(lista_ingredientes)):

            contador = contador + 1

            if (contador == opcion): # si estamos en la opcion correcta cambiamos el valor

                lista_ingredientes[i].gramos  =  gramos_cambio

        
        return lista_ingredientes # devolvemos la lista modificada







def modificar_precio_v2(lista_ingredientes):
        
        contador = 0
        
        for i in range(0, len(lista_ingredientes)):

                contador = contador + 1

                print(contador, " producto: ", lista_ingredientes[i].nombre, " precio: ", lista_ingredientes[i].precio)

            
        
        opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")
        
        while(opcion < 1 or opcion > len(lista_ingredientes)): # comprovamos que la opcion sea correcta

            contador = 0
            
            for i in range(0, len(lista_ingredientes)):

                contador = contador + 1

                print(contador, " producto: ", lista_ingredientes[i].nombre, " gramos: ", lista_ingredientes[i].precio)

            
            opcion = comprovar_try_except("introduce el numero de el producto que quieres cambiar")

        
        
            
            
        opcion_try_except = 0
        
        precio_cambio = -1 
        while(opcion_try_except == 0):
        
                while(precio_cambio < 0): # con este while nos aseguramos de que gramos sea > 0
        
                    try:
                        precio_cambio = float(input("introduce cuantos precio tiene ahora el producto"))
        
                        opcion_try_except = 1 # la opcion vale 1 si el try except no ha salido
                    
                    except:
                        print("introduce un valor correcto")
        
        # con gramso ahora correcto cambiamos los gramos
        
        contador = 0

        for i in range(0, len(lista_ingredientes)):

            contador = contador + 1

            if (contador == opcion): # si estamos en la opcion correcta cambiamos el valor

                lista_ingredientes[i].precio  =  precio_cambio

        return lista_ingredientes




def mostrar_ingredientes_v2(lista_ingredientes):
     

     contador = 0

     for i in range(0, len(lista_ingredientes)):

            contador = contador + 1

            print(contador, " producto: ", lista_ingredientes[i].nombre, " precio: ", (lista_ingredientes[i].gramos)*(lista_ingredientes[i].precio))