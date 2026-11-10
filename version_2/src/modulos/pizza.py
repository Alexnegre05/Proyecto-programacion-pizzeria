from version_2.src.modulos.producto import Producto

class Pizza(Producto):

    def __init__(self, nombre, precio, ingredientes): # Le enviamos el nombre y precio a la clase madre (Producto)
        
        super().__init__(nombre, precio)
        
        self.ingredientes = ingredientes # Guardamos el parámetro específico de la subclase

    def mostrar_pizza_v2(lista_pizzas):

        listado_pizzas = "" # La variable str que nos devolvera la lista de las pizzas formateadas

        for i,pizza in enumerate(lista_pizzas): #

            listado_pizzas += f"{i+1}:{pizza.nombre}:\n"

            for ingrediente in pizza.ingredientes:

                listado_pizzas += f"    -{ingrediente}\n"

        return listado_pizzas # Retornamos la variable formateada

    def selecionar_pizzar_v2(lista_pizzas):

        seleccion = int (input('selecciona la pizza por su numero')) #Pedimos la pizza y casteamos a un entero

        while seleccion <= 0 or seleccion > len(lista_pizzas):

            seleccion = int (input('seleccion incorrecta intentalo de nuevo, la pizza por su numero')) 
        
        pizza_selecionada=lista_pizzas[seleccion-1] #Guardamos la pizza(Objeto) en una variable 

        return pizza_selecionada  #Retonamos la pizza(Objeto) al main

    def Calcular_precio_ingrediente_v2(self,lista_objetos_ingredientes):

        total_precio_por_ingrediente=0

        for ingrediente in self.ingredientes:

            for objeto_ingre in lista_objetos_ingredientes:

                if objeto_ingre.nombre == ingrediente: #Verificamos el ingrediente de la pizza selecionada con lo ingredientes de nuestra pizzas(Objeto) 

                    coste = objeto_ingre.coste_ingrediente_v2() #Traemos el precio por gramo de los ingredientes

                    total_precio_por_ingrediente += coste   #Acumulamos el coste de cada ingrediente en una unica variable 

        return total_precio_por_ingrediente
            
    def calcular_precio_pizzas(lista_pizzas_seleccionadas,lista_objetos_ingredientes):

        precio_x_pizza=[]

        gastos_suministros = 5500

        for pizza in lista_pizzas_seleccionadas:

            precio_total_ingredientes = pizza.Calcular_precio_ingrediente_v2(lista_objetos_ingredientes)

            beneficios = precio_total_ingredientes/2

            total = precio_total_ingredientes + beneficios + gastos_suministros/200 # Guardamos en una variable el coste dacada una de las pizzas selecionadas

            precio_x_pizza.append(total)

        return precio_x_pizza   #Retornamos en una lista cada uno de los costes de cada pizza seleccionada
        
        