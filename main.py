
from src.menus import menu, menu_principal,menu_pizzas,menu_bebidas,menu_otros # carpeta.carpeta., etc para importar
from src.modulos.catalogo_productos import obtener_catalogo
from src.modulos.calculos import calculo_precio_pizzas
from src.modulos.cambiar_temporada import cambiar_temporada
from src.modulos.pedidos import mostrar_carrito
from src.modulos.ofertas import ofertas,oferta_1, oferta_2, oferta_3

from src.modulos.seleccionar_bebidas import seleccionar_bebida, mostrar_bebidas

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
                    print("en desarrollo")
                        
           
                    
        case 2:  # bebidas
            opcion_bebidas = menu_bebidas()

            if (opcion_bebidas == 1):
                mostrar_bebidas()

            else:
                bebidas = seleccionar_bebida()

                pizzas.append(1) # añadimos que es una bebida popniendo un 1, para saber en ofertas que es exactamente este producto
                lista_productos.append(bebidas)

                

        case 3: # otros
             opcion_otros = menu_otros()

             if (opcion_otros == 1):
                
                oferta_seleccionada = ofertas(lista_productos) # funcion que mira todas las ofertas

                if (oferta_seleccionada != 0): # si hay una oferta_seleccionada
                    
                    if (oferta_seleccionada == 1):
                       lista_productos = oferta_1(lista_productos)
                       print(lista_productos)
                    
                    elif (oferta_seleccionada == 2):
                        oferta_2()

                    else:
                        oferta_3()



             elif (opcion_otros == 2): # cambiar temporada

                cambiar_temporada()

             elif (opcion_otros == 3): # carrito

                carrito = mostrar_carrito(lista_productos)
                print(carrito)

   
                
    opcion_general = menu_principal()
                
                    





