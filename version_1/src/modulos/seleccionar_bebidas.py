
from version_1.src.datos.bebidas import bebidas_precio

from comun.try_except import comprovar_try_except

def mostrar_bebidas():

    contador = 1 # sirve como indice para las bebidas

    print("\n")

    for clave, valor in bebidas_precio.items(): # con items mostramos la clave y el valor

        print(contador, "-bebida: ", clave, " precio: ", valor)

        contador = contador + 1 # sumamos 1 a el contador




def seleccionar_bebida():

    mostrar_bebidas()

    opcion = comprovar_try_except("selecciona una opcion: ")

    while(opcion < 1 or opcion > 6):
        
        mostrar_bebidas()

        opcion = comprovar_try_except("selecciona uan opcion correcta: ")

     
    contador = 1 # sirve como indice para las bebidas ahora tambien se compara con al opcion seleccionada si son iguales devolvemos la bebida con el precio

    for clave, valor in bebidas_precio.items(): # con items mostramos la clave y el valor

        

        if (contador == opcion):

            print("\n bebida seleccionada: ", clave)

            lista_resultado = [clave, valor] # devolvemos el nombre de la bebida jubto a su precio
            
            return lista_resultado

        contador += 1


