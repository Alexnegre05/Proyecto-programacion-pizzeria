from src.datos.pizzas import pizzerias_ingredientes
from src.datos.ingredientes import ingrediente_precio, ingredientes_gramos
from src.datos.temporada import temporada
from src.modulos.catalogo_productos import obtener_catalogo


def seleccionar_pizzas():

    obtener_catalogo()

    # aqui ira la funcion de mostrar pizzas
    # 1 calcular precio pizza y desglose de precio
    # 2 calcular coste ingrediente de pizza

    print("\n")

    pizza_seleccionada = int(input("selecciona numero de que pizza quieres: ")) # pedimos un numero 
    # este numero es el indice de el diccionario
    
    # comprovamos que el nombre es correcto
    while(pizza_seleccionada < 1 or pizza_seleccionada > 20):
        
        pizza_seleccionada = int(input("selecciona numero correcto: "))



    num_pizzas = 1 # con esto sabemos si la pizza seleccionada en que posicion de el diccionario esta
    # como nosotros vamos de uno en uno la pizza 0 seria la 1...

    ingredientes = None # definimos ingredientes como None vacio

    for key,value in pizzerias_ingredientes.items():

        if (num_pizzas == pizza_seleccionada):# si la pizza seleccionada es la que estamos viendo

            ingredientes = value # los ingredientes son el value
            break # salimos de el bucle

        num_pizzas = num_pizzas + 1

    if (ingredientes != None): # si ingredientes no es none

        # calculamos el precio de la pizza


        precio_total_ingredientes = 0 # esto suma cuanto cuesta el total

        for i in range(0, len(ingredientes)): # vamos ingrediente a ingrediente
           
           ingrediente_actual = ingredientes[i] # por cada ingrediente sacamos su precio en gramos 

           precio_normal = ingrediente_precio[ingrediente_actual]*ingredientes_gramos[ingrediente_actual]

           print("precio ingrediente: ", ingrediente_actual, " es ", precio_normal)

           precio_total_ingredientes = precio_total_ingredientes + precio_normal

        print("la pizza cuesta sin IVA ni gastos ni temporada", precio_total_ingredientes)

        # aqui sumamos gastos, de momento son 0

        gastos_suministros = 0

        precio_total_ingredientes = precio_total_ingredientes + gastos_suministros

        print("la pizza cuesta sin IVA ni temporada  pero con gastos: ", precio_total_ingredientes)

        # ahora añadimos el IVA, en este caso es *1,21

        precio_total_ingredientes = precio_total_ingredientes*1.21

        print("la pizza cuesta sin temporada: ", precio_total_ingredientes)

        precio_final = precio_total_ingredientes*temporada[0]
        print("la pizza final cuesta")

