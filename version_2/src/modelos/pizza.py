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

    def Calcular_precio_ingrediente_v2(self,lista_objetos_ingredientes):
        total_precio_por_ingrediente=0

        for ingrediente in self.ingredientes:

            for objeto_ingre in lista_objetos_ingredientes:

                if objeto_ingre.nombre == ingrediente:

                    coste = objeto_ingre.coste_ingrediente_v2()

                    total_precio_por_ingrediente += coste

        return total_precio_por_ingrediente
            
    def calcular_precio_pizzas(lista_pizzas_seleccionadas,lista_objetos_ingredientes):

        total = 0

        gastos_suministros = 5500

        for pizza in lista_pizzas_seleccionadas:

            precio_total_ingredientes = pizza.Calcular_precio_ingrediente_v2(lista_objetos_ingredientes)

            beneficios = precio_total_ingredientes/2

            total += precio_total_ingredientes + beneficios + gastos_suministros/200

        return total
        
        