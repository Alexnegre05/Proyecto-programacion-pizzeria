# ofertas:
# 
# 1. 2 pizzas y solo 2 pizzas incluimos 1 bebida gratuita

# 2. 4 pizzas y solo 4 pizzas descuento 5%

# 3. n pizzas y m bebidas si y solo si n+m >=5 ^ n+m <=20 entonces n+m% de descuento total

from version_1.src.modulos.seleccionar_bebidas import seleccionar_bebida

def mostrar_ofertas():
    print("\n")
    print("1 2 pizzas-> 1 bebida gratis")
    print("2 4 pizzas -> 5 % en descuento")
    print("3 si tus productos en total estan entre 5 y 20 se te aplicara un descuento en porcentaje de la suma de tus productos")

def ofertas(lista_productos): # funcion que mira que oferta hay que aplicar

    print("\n")

    if (len(lista_productos) < 2): # si la longitud es menor a 2 no hay ninguna oferta a ofrecer

        print("no hay ninguna oferta")

        return 0 # 0 indica que no hay ofertas

    else:
        
        # contadores que nos indican el numero de pizzas o bebidas que hay
        count_pizzas = 0
        count_bebidas = 0

        for i in range(0, len(lista_productos)): # recorremos toda la lista


            if (lista_productos[i][2] == 0): # esto es una pizza, el segundo valor recibe un 0 si es pizza o un 1 el formato es (nombre,precio,numero)
                
                count_pizzas = count_pizzas + 1

            else: # esto es una bebida
                count_bebidas = count_bebidas + 1


        # dependiendo de el caso te returna un valor u otro eso indica que oferta se te ha aplicado
        if (count_pizzas == 2):

            print("oferta 1")

            return 1

        else:

            if (count_pizzas == 4):

                print("oferta 2")

                return 2

            elif ((count_pizzas + count_bebidas) >= 5 and (count_pizzas + count_bebidas) <= 20):
                    
                    print("oferta 3")
                    return 3
            
        # si llega a el final y no ha devuelto ningun valor entonces no hay ninguna oferta a aplicar, devolvemos 0

        print("oferta no")
        return 0



def oferta_1(lista_productos):
    
    print("se te aplica oferta 1")

    bebida_seleccionada = seleccionar_bebida() # llamamos a la funcion que selecciona una bebida

    bebida_seleccionada[1] = 0 # ponemos el precio de esta bebida en exclusiva a 0, recibimos una lista con (nombre bebida, precio)

    bebida_seleccionada.append(1) # añadir que es categoria bebida con un 1
    
    lista_productos.append(bebida_seleccionada)

    return 0  # devolvemos la bebida seleccionada

    

def oferta_2(precio_final):
    
    print("se te aplica oferta 2")
    
    precio_final= precio_final*(1/20) # aplicamos un 5%

    return precio_final

def oferta_3(lista_productos,precio_final):
    
    print("se te aplica oferta 3")
    
    precio_final = precio_final*(len(lista_productos)/100) # n+m en cuanto a bebidas y pizzas es lo mismo que len lista de productos

    return precio_final




# funcion que calcula las ofertas
def menu_ofertas(lista_productos):

    precio_final = 0 

    for i in range(0, len(lista_productos)):

        precio_final = precio_final + lista_productos[i][1] # el 1 es el precio 

        oferta_seleccionada = ofertas(lista_productos) # funcion que mira todas las ofertas

        if (oferta_seleccionada != 0): # si hay una oferta_seleccionada
                    
            if (oferta_seleccionada == 1):
                       
                lista_productos = oferta_1(lista_productos) # llamamos a oferta 1
                print(lista_productos)

                return lista_productos

            elif (oferta_seleccionada == 2):

                 print("se te aplica la segunda oferta")
                 precio_oferta = oferta_2(precio_final) # llamamos a oferta 2 devuelve el precio

                 return precio_oferta


            else:

                print("se te aplica la tercera oferta")
                precio_oferta = oferta_3(lista_productos, precio_final)

                return precio_oferta

                # llamamos a oferta 3

    return 0