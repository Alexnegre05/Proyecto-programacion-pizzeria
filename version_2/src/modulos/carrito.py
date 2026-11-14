
from datetime import datetime # importamos el modula para trabajar con el tiempo
from version_2.src.datos.bebidas import lista_bebidas,seleccionar_bebida_v2,mostrar_bebida_v2
from comun.try_except import comprovar_try_except
from version_2.src.modulos.pizza import Pizza
import copy


IVA = 0.21

class Carrito:
    def __init__(self):
        self.producto = []

    def ofertas(self): # funcion que mira que oferta hay que aplicar

        print("\n")

        if (len(self.producto) < 2): # si la longitud es menor a 2 no hay ninguna oferta a ofrecer

            print("no hay ninguna oferta")

            return 0 # 0 indica que no hay ofertas

        else:
            
            # contadores que nos indican el numero de pizzas o bebidas que hay
            count_pizzas = 0
            
            count_bebidas = 0

            for i in self.producto: # recorremos toda la lista


                if isinstance(i,Pizza): # esto es una pizza
                    
                    count_pizzas = count_pizzas + 1

                else: # esto es una bebida
                    count_bebidas = count_bebidas + 1


            # dependiendo de el caso te returna un valor u otro eso indica que oferta se te ha aplicado
            if (count_pizzas == 2):

                print("oferta 1")

                return 1

            else:

                if (count_pizzas == 4 and count_bebidas < 2):

                    print("oferta 2")

                    return 2

                elif ((count_pizzas + count_bebidas) >= 5 and (count_pizzas + count_bebidas) <= 20):
                        
                        print("oferta 3")
                        
                        return 3
                
            # si llega a el final y no ha devuelto ningun valor entonces no hay ninguna oferta a aplicar, devolvemos 0

            print("oferta no")
            
            return 0
        
    def print_ticket_v2(self):

        tipo_iva = 0
        importe_total = 0
        oferta_promocional = 0 # menu_ofertas(lista_productos)

        opcion_oferta = self.ofertas()

        if opcion_oferta == 3:
            oferta_promocional=oferta3_v2(self)
            
        elif opcion_oferta == 2:
            
            oferta_promocional=oferta2_v2(self)
        elif opcion_oferta == 1:

            bebida_seleccionada=seleccionar_bebida_v2(lista_bebidas)

            oferta1_v2(self,bebida_seleccionada)
                
            

        time = datetime.now() #guardamos en una variable

        #guardamos la variable de tiempo
        date = time.strftime("%d/%m/%y")
        hora = time.strftime("%H:%M")

        #generamos la variable que contendra el formato para el tiket
        ticket_str = f"""========================================\n
    {'PIZZERIA PLANETAFP':^40}\n
    ========================================\n
    fecha: {date:<9}            hora: {hora}\n
    ----------------------------------------\n
    DESCRIPCION                   IMPORTE\n
    """

        for dato in self.producto:

            importe_total +=dato.precio # esto es el precio 

            ticket_str += f"{dato.nombre:<29}{dato.precio:8.2f}€\n"

        tipo_iva = (importe_total-oferta_promocional)*IVA # el iva se cobra sobre el precio final a cobrar, por eso descontamos la oferta y asi tener el precio base final
        total_fina = importe_total -oferta_promocional+tipo_iva
        ticket_str +=f"""----------------------------------------\n 
    {'Subtotal':<29}{importe_total:8.2f}€\n 
    {'Ofertas':<29}{oferta_promocional:8.2f}€\n
    {'Iva':<29}{tipo_iva:8.2f}€\n
    ----------------------------------------\n
    {'Total':<29}{total_fina:8.2f}€\n
    """

        ticket_str +=f"""========================================
    {'¡Muchas gracias por su visita!':^40}            
    {'www.pizzeriaplanetafp.cat':^40}            
    ========================================"""

        return ticket_str    

def mostrar_carrito_v2(lista_producto):

        
        if (len(lista_producto) != 0): # si hay elementos en el carrito

            fotmat_carrito ="\n CARRITO:\n "

            for producto in lista_producto:

                fotmat_carrito =fotmat_carrito +  f"Producto:{producto.nombre}, Precio: {producto.precio}\n"

            return fotmat_carrito

        else:
            return "\n no hay elementos en el carrito \n"
        



def quitar_producto_carrito_v2(lista_producto):


        for i in range(0, len(lista_producto)):

            print(i + 1, "-Producto: ", lista_producto[i].nombre, "Precio: ", lista_producto[i].precio)

            # mostramos el carrito pero con un numero indexado, es i + 1 para que empieze desde 1

        opcion = comprovar_try_except("\n selecciona el numero de el producto que quieres quitar, 0 para salir: ")

        # con esto el usuario escribe una opcion

        while(opcion < 0 or opcion > len(lista_producto)): # en caso de que el numero no exista
            
            for i in range(0, len(lista_producto)):
            
                    print(i + 1, "-Producto: ", lista_producto[i].nombre, "Precio: ", lista_producto[i].precio)
            
            opcion = comprovar_try_except("\n selecciona el numero correcto de el producto que quieres quitar, 0 para salir: ")


        # si la opcion es 0 como hay que salir devolvemos directamente la lista sin modificar nada
        if (opcion == 0):

            return lista_producto

        else:

            lista_producto.pop(opcion - 1) # esto elimina por indice, como el usuario no empieza desde 1 sino desde 0 hacemos opcion - 1

            return lista_producto # devolvemos la lista
        







def oferta1_v2(self,bebida):

     bebida_gratis = copy.copy(bebida)

     bebida_gratis.precio = 0

     self.producto.append(bebida_gratis)
     
     pass


def oferta2_v2(self):
    total = 0

    for i in self.producto:

        if isinstance(i,Pizza):
             
            total += i.precio
          
        
    descuento_oferta2 = total * 0.05
    return descuento_oferta2


def oferta3_v2(self):
     total = 0
     contador = 0

     for i in self.producto:
        contador += 1

        total += i.precio 

     descuento_oferta3 = total * contador / 100
     return descuento_oferta3
     