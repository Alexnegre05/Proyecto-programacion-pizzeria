from datetime import datetime # importamos el modula para trabajar con el tiempo


def print_ticket(lista_productos):

    time = datetime.now() #guardamos en una variable

    #guardamos la variable de tiempo
    date = time.strftime("%d/%m/%y")
    hora = time.strftime("%H:%M")

    #generamos la variable que contendra el formato para el tiket
    ticket_str = f"""=====================================\n
          PIZZERIA PLANETAFP\n
=====================================\n
fecha: {date}            hora: {hora}\n
-------------------------------------\n
DESCRIPCION                   IMPORTE\n
"""

    for dato in lista_productos:

        ticket_str += f"{dato[0]:<25} {dato[1]:8.2f}€\n"

    
    ticket_str +=f"""  """

    ticket_str +=f"""==================================================
        ¡Muchas gracias por su visita!            
             www.pizzeriaplanetafp.cat            
================================================== """

    return ticket_str