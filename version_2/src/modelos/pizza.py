from version_2.src.modelos.producto import Producto

class Pizza(Producto):

    def __init__(self, nombre, precio, ingredientes): # Le enviamos el nombre y precio a la clase madre (Producto)
        
        super().__init__(nombre, precio)
        
        self.ingredientes = ingredientes # Guardamos el parámetro específico de la subclase

    def mostrar_pizza_v2(lista_pizzas):
        listado_pizzas = ""

        for i,pizza in enumerate(lista_pizzas):

            listado_pizzas += f"{i+1}:{pizza.nombre}:\n"

            for ingrediente in pizza.ingredientes:

                listado_pizzas += f"    -{ingrediente}\n"

        return listado_pizzas

    def selecionar_pizzar_v2(lista_pizzas):
        pizza_selecionada = []

        seleccion = int (input('selecciona la pizza por su numero'))

        while seleccion <= 0 or seleccion > len(lista_pizzas):
            seleccion = int (input('seleccion incorrecta intentalo de nuevo, la pizza por su numero')) 
        
        pizza_selecionada.append(lista_pizzas[seleccion-1])

        return pizza_selecionada    
