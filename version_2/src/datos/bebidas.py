from version_2.src.modelos.bebida import Bebida

from comun.try_except import comprovar_try_except
# creamos las 6 bebidas

Agua = Bebida("Agua", 1.5)
Aquarius = Bebida("Aquarius", 2)
Nestea = Bebida("Nestea",2)
Vino_rojo = Bebida("Vino_rojo", 15)
Vino_blanco = Bebida("Vino_blanco", 18)
Vino_caro = Bebida("Vino_caro", 45)


lista_bebidas = [Agua, Aquarius, Nestea, Vino_rojo, Vino_blanco, Vino_caro]


def mostrar_bebida_v2(lista_bebidas):

    for i in range(0, len(lista_bebidas)):

        resultado = lista_bebidas[i].mostrar()

        print(i + 1, resultado) # mostramos el resultado con un indice 


def seleccionar_bebida_v2(lista_bebidas):

      mostrar_bebida_v2(lista_bebidas)

      opcion = comprovar_try_except("selecciona una opcion: ")

      while(opcion < 1 or opcion > 6):
            
         mostrar_bebida_v2

         opcion = comprovar_try_except("selecciona una opcion correcta: ")

       
      contador = 1 # sirve como indice para las bebidas ahora tambien se compara con al opcion seleccionada si son iguales devolvemos la bebida con el precio

      for i in range(0, len(lista_bebidas)): # con items mostramos la clave y el valor

            

        if (contador == opcion):

            print("\n bebida seleccionada: ", lista_bebidas[i].nombre) # mostramos el nombre

            return lista_bebidas[i]

                

        contador =contador +  1