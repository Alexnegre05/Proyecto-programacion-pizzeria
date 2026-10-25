
from src.menus import menu_principal,menu_pizzas,menu_bebidas,menu_otros # carpeta.carpeta., etc para importar
from src.modulos.catalogo_productos import obtener_catalogo
from src.modulos.calculos import calculo_precio_pizzas
from src.modulos.cambiar_temporada import cambiar_temporada
from src.modulos.pedidos import mostrar_carrito
from src.modulos.ofertas import  menu_ofertas, mostrar_ofertas
from src.modulos.ticket import print_ticket

from src.modulos.seleccionar_bebidas import seleccionar_bebida, mostrar_bebidas
from src.modulos.mostrar_ingredientes import mostrar_ingredientes
lista_productos = []


opcion_general = menu_principal()

while opcion_general > 0 and opcion_general < 4:

    match opcion_general:
        case 1: # opcion seleccionada pizza
            o_pizas = menu_pizzas()

            match o_pizas: # selecciona la funcion que se encarga de esta parte
                case 1:
                    obtener_catalogo()
                        
                case 2:
                    pizzas = calculo_precio_pizzas()

                    pizzas.append(0) # añadimos que es una pizza popniendo un0, para saber en ofertas que es exactamente este producto
                    lista_productos.append(pizzas)
                        
                case 3:
                    mostrar_ingredientes()
                        
           
                    
        case 2:  # bebidas
            opcion_bebidas = menu_bebidas()

            if (opcion_bebidas == 1):
                mostrar_bebidas()

            elif (opcion_bebidas == 2):
                bebidas = seleccionar_bebida()

                bebidas.append(1) # añadimos que es una bebida popniendo un 1, para saber en ofertas que es exactamente este producto
                lista_productos.append(bebidas)

                

        case 3: # otros
             opcion_otros = menu_otros()

             if (opcion_otros == 1): # ofertas solo sirve para saber en este momento si se le aplica o no una oferta
                mostrar_ofertas()

             elif (opcion_otros == 2): # cambiar temporada

                cambiar_temporada()

             elif (opcion_otros == 3): # carrito

                carrito = mostrar_carrito(lista_productos)
                print(carrito)

            
             elif (opcion_otros == 4): # opcion 4
                print(print_ticket(lista_productos))

                
    

   
                
    opcion_general = menu_principal()
                
                    





