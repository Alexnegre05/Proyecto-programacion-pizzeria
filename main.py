
from comun.menus import menu_principal,menu_pizzas,menu_bebidas,menu_otros, menu_carrito, menu_ingredientes,seleccionar_opcion_programa # carpeta.carpeta., etc para importar
from version_1.src.modulos.catalogo_productos import obtener_catalogo
from version_1.src.modulos.calculos import calculo_precio_pizzas
from comun.cambiar_temporada import cambiar_temporada
from version_1.src.modulos.pedidos import mostrar_carrito, quitar_producto_carrito
from version_1.src.modulos.ofertas import  menu_ofertas, mostrar_ofertas
from version_1.src.modulos.ticket import print_ticket
from version_1.src.datos.ingredientes import ingredientes_gramos, ingrediente_precio
from version_1.src.modulos.modificar_ingredientes import modificar_gramos, modificar_precio
from version_1.src.modulos.seleccionar_bebidas import seleccionar_bebida, mostrar_bebidas
from version_1.src.modulos.mostrar_ingredientes import mostrar_ingredientes
from comun.try_except import comprovar_try_except

from version_2.src.datos.bebidas import mostrar_bebida_v2, seleccionar_bebida_v2
from version_2.src.datos.bebidas import lista_bebidas

from version_2.src.datos.ingredientes import lista_ingredientes
from version_2.src.modulos.ingrediente import modificar_gramos_v2, modificar_precio_v2,mostrar_ingredientes_v2

from version_2.src.modulos.carrito import Carrito, print_ticket_v2, mostrar_carrito_v2, quitar_producto_carrito_v2

from version_2.src.datos.pizzas import pizzerias_ingredientes
from version_2.src.modulos.pizza import Pizza
from version_2.src.datos.ingredientes import lista_ingredientes


if "__main__" == __name__:

    opcion_programa = seleccionar_opcion_programa() # se puede seleccionar que opcion de el programa ejecutar

    if (opcion_programa == 1):

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
                            opcion_ingredientes = menu_ingredientes() # menu para indicar que quiere hacer el usuario

                            if (opcion_ingredientes == 1):

                                mostrar_ingredientes()

                            elif (opcion_ingredientes == 2):

                                ingredientes_gramos = modificar_gramos(ingredientes_gramos)

                            elif (opcion_ingredientes == 3):

                                ingrediente_precio = modificar_precio(ingrediente_precio)
                                
                
                        
            

                            
            
                        
                case 2:  # bebidas
                    opcion_bebidas = menu_bebidas()

                    if (opcion_bebidas == 1):

                        mostrar_bebidas()

                    if (opcion_bebidas == 2):
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

                        opcion_carrito = menu_carrito()

                        if (opcion_carrito == 1):

                            carrito = mostrar_carrito(lista_productos)
                            print(carrito)

                        elif (opcion_carrito == 2):

                            lista_productos =  quitar_producto_carrito(lista_productos) # que se pueda quitar un producto

                    
                    elif (opcion_otros == 4): # opcion 4
                        print(print_ticket(lista_productos))

                        
            

        
                        
            opcion_general = menu_principal()

    else:

        lista_productos_carrito = Carrito() # creamos un carrito que este vacio
        

        opcion_general = menu_principal()
        lista_pizzas =[]

        while opcion_general > 0 and opcion_general < 4:
            

            match opcion_general:
                
                case 1: # opcion seleccionada pizza
                    o_pizas = menu_pizzas()

                    resultado = Pizza.mostrar_pizza_v2(pizzerias_ingredientes)

                    match o_pizas: # Selecciona la funcion que se encarga de esta parte
                        case 1: # Muestra el catalo de pizzas
                             print(resultado)
                                
                        case 2: # Selecciona la pizza y nos muestra el carrito

                            resultado_seleccion=Pizza.selecionar_pizzar_v2(pizzerias_ingredientes)
                            resultado_seleccion.calcular_precio_pizzas(lista_ingredientes)

                            lista_productos_carrito.producto.append(resultado_seleccion)
                            print(mostrar_carrito_v2(lista_productos_carrito.producto))

                                
                        case 3:
                            opcion_ingredientes = menu_ingredientes() # menu para indicar que quiere hacer el usuario

                            if (opcion_ingredientes == 1):

                                 mostrar_ingredientes_v2(lista_ingredientes)

                            elif (opcion_ingredientes == 2):

                                lista_ingredientes = ingredientes_gramos = modificar_gramos_v2(lista_ingredientes)

                            elif (opcion_ingredientes == 3):

                                lista_ingredientes = modificar_precio_v2(lista_ingredientes)
                                
                
                        
            

                            
            
                        
                case 2:  # bebidas
                    opcion_bebidas = menu_bebidas()

                    if (opcion_bebidas == 1):

                        mostrar_bebida_v2(lista_bebidas)

                    if (opcion_bebidas == 2):
                        
                        bebida = seleccionar_bebida_v2(lista_bebidas)

                        lista_productos_carrito.producto.append(bebida) # añadimos en la lista las bebidas
                        

        #               

                        

                case 3: # otros
                    opcion_otros = menu_otros()

                    if (opcion_otros == 1): # ofertas solo sirve para saber en este momento si se le aplica o no una oferta
                         mostrar_ofertas() # al no cambiar las ofertas se llama a la misa funcion

                    elif (opcion_otros == 2): # cambiar temporada

                         cambiar_temporada()

                    elif (opcion_otros == 3): # carrito

                        opcion_carrito = menu_carrito()

                        if (opcion_carrito == 1):

                            carrito = mostrar_carrito_v2(lista_productos_carrito.producto)
                            print(carrito)

                        elif (opcion_carrito == 2):

                            lista_productos =  quitar_producto_carrito_v2(lista_productos_carrito.producto) # que se pueda quitar un producto

                    
                    elif (opcion_otros == 4): # opcion 4
                        print(print_ticket_v2(lista_productos_carrito.producto))

                        
            

        
                        
            opcion_general = menu_principal()

                    
                        





