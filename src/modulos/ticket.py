from datetime import datetime # importamos el modula para trabajar con el tiempo
from src.modulos.ofertas import menu_ofertas
IVA = 0.21
def print_ticket(lista_productos):

    tipo_iva = 0
    importe_total = 0
    oferta_promocional = menu_ofertas(lista_productos)

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

    for dato in lista_productos:

        importe_total +=dato[1] 

        ticket_str += f"{dato[0]:<29}{dato[1]:8.2f}€\n"

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