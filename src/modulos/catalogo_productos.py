from ..datos.pizzas import pizzerias_ingredientes as lista_pizzas

#recorrela lista de pizzas y mostarla en un formato editado 
#for para REcorrela y mostrarla 
def obtener_catalogo ():
    for i, (pizza,ingredientes) in enumerate(lista_pizzas.items(),start=1):

        print(f"pizza {i} : {pizza}:")

        for ingrediente in ingredientes:

            limpio = ingrediente.replace("_"," ").capitalize()
            print(f"    -{limpio}")
            
        print("\n")
    