
from src.datos.pizzas import pizzerias_ingredientes

from src.modulos.catalogo_productos import obtener_catalogo

from src.modulos.try_except import comprovar_try_except

def escoger_pizza_usuario():

    obtener_catalogo()

    # aqui ira la funcion de mostrar pizzas
    # 1 calcular precio pizza y desglose de precio
    # 2 calcular coste ingrediente de pizza

    print("\n")

    pizza_seleccionada = comprovar_try_except("selecciona numero de que pizza quieres: ") # pedimos un numero 
    # este numero es el indice de el diccionario
    
    # comprovamos que el nombre es correcto
    while(pizza_seleccionada < 1 or pizza_seleccionada > 20):
        
       comprovar_try_except("selecciona numero correcto: ")



    num_pizzas = 1 # con esto sabemos si la pizza seleccionada en que posicion de el diccionario esta
    # como nosotros vamos de uno en uno la pizza 0 seria la 1...

    ingredientes = None # definimos ingredientes como None vacio

    pizza_escogida_nombre = ""
    for key,value in pizzerias_ingredientes.items():

        if (num_pizzas == pizza_seleccionada):# si la pizza seleccionada es la que estamos viendo

            ingredientes = value # los ingredientes son el value

            pizza_escogida_nombre = key # guardamos el nombre
            break # salimos de el bucle

        num_pizzas = num_pizzas + 1

    lista = [pizza_escogida_nombre, ingredientes] # devolvemos los ingredientes y la pizza seleccionada con una lista

    return lista