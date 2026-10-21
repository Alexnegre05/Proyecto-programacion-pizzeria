
from src.datos.bebidas import bebidas_precio



def mostrar_bebidas():

    contador = 1 # sirve como indice para las bebidas

    print("\n")
    for clave, valor in bebidas_precio.items(): # con items mostramos la clave y el valor

        print(contador, "-bebida: ", clave, " precio: ", valor)

        contador = contador + 1 # sumamos 1 a el contador




def seleccionar_bebida():

    mostrar_bebidas()

    opcion = int(input("selecciona una opcion"))

    while(opcion < 1 or opcion > 6):
        
        mostrar_bebidas()

        opcion = int(input("selecciona una opcion correcta"))

     
    contador = 1 # sirve como indice para las bebidas ahora tambien se compara con al opcion seleccionada si son iguales devolvemos la bebida con el precio

    for clave, valor in bebidas_precio.items(): # con items mostramos la clave y el valor

        

        if (contador == opcion):

            print("\n bebida seleccionada: ", clave)
            lista_resultado = [clave, valor] # devolvemos el nombre de la bebida jubto a su precio
            return lista_resultado

        contador += 1


