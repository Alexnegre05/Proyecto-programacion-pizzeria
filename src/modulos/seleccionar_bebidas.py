from src.datos.temporada import temporada
from src.datos.bebidas import bebidas_precio



def mostrar_bebidas():

    for clave, valor in bebidas_precio.items(): # con items mostramos la clave y el valor

        print("bebida: ", clave, " precio: ", valor)



def seleccionar_bebida():

    mostrar_bebidas()



