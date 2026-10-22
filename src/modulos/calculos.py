
from src.datos.ingredientes import ingrediente_precio, ingredientes_gramos
from src.datos.temporada import temporada

from src.modulos.seleccionar_pizza import escoger_pizza_usuario

def calculo_precio_pizzas():

    lista = escoger_pizza_usuario() # devuelve una lista que escoge una pizza 
    # y devuelve la pizza y sus ingredientes

    pizza_escogida_nombre = lista[0]
    ingredientes = lista[1]

    if (ingredientes != None): # si ingredientes no es none

        # calculamos el precio de la pizza


        precio_total_ingredientes = 0 # esto suma cuanto cuesta el total

        for i in range(0, len(ingredientes)): # vamos ingrediente a ingrediente
           
           ingrediente_actual = ingredientes[i] # por cada ingrediente sacamos su precio en gramos 

           precio_normal = ingrediente_precio[ingrediente_actual]*ingredientes_gramos[ingrediente_actual]

           print("precio ingrediente: ", ingrediente_actual, " es ", precio_normal)

           precio_total_ingredientes = precio_total_ingredientes + precio_normal

        print("la pizza cuesta sin IVA ni gastos ni temporada", precio_total_ingredientes)

        # aqui sumamos gastos que cuentan trabajadores luz alquiler...

        gastos_suministros = 5500

        beneficios = precio_total_ingredientes/2 # nos sumamos unos beneficios que son la mitad de los precios total que cuesta hacer la pizza

        precio_total_ingredientes = precio_total_ingredientes + gastos_suministros/200 + beneficios

        print("la pizza cuesta sin IVA ni temporada  pero con gastos: ", precio_total_ingredientes)

        # ahora añadimos el IVA, en este caso es *1,21

        precio_total_ingredientes = precio_total_ingredientes*1.21

        print("la pizza cuesta sin temporada: ", precio_total_ingredientes)

        precio_final = precio_total_ingredientes*temporada[0]
        print("la pizza final cuesta", precio_final)

        lista_resultado =[pizza_escogida_nombre, precio_final]
       

        return lista_resultado

