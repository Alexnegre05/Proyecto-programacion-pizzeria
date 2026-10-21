# ofertas:
# 
# 1. 2 pizzas y solo 2 pizzas incluimos 1 bebida gratuita

# 2. 4 pizzas y solo 4 pizzas descuento 5%

# 3. n pizzas y m bebidas si y solo si n+m >=5 ^ n+m <=20 entonces n+m% de descuento total



def ofertas(lista_productos): # funcion que mira que oferta hay que aplicar

    print("\n")

    if (len(lista_productos) < 2): # si la longitud es menor a 2 no hay ninguna oferta a ofrecer
        print("no hay ninguna oferta")

    else:
        
        # contadores que nos indican el numero de pizzas o bebidas que hay
        count_pizzas = 0
        count_bebidas = 0

        for i in range(0, len(lista_productos)): # recorremos toda la lista


            if (lista_productos[i][2] == 0): # esto es una pizza, el segundo valor recibe un 0 si es pizza o un 1 el formato es (nombre,precio,numero)
                count_pizzas = count_pizzas + 1

            else: # esto es una bebida
                count_bebidas = count_bebidas


        # dependiendo de el caso te returna un valor u otro eso indica que oferta se te ha aplicado
        if (count_pizzas == 2):

            return 1

        else:

            if (count_pizzas == 4):

                return 2

            elif ((count_pizzas + count_bebidas) >= 5 and (count_pizzas + count_bebidas) <= 20):
                    return 3



def oferta_1(lista_productos):
    
    print("se te aplica oferta 1")
    pass

def oferta_2(lista_productos):
    
    print("se te aplica oferta 2")
    pass

def oferta_3(lista_productos):
    
    print("se te aplica oferta 3")
    pass