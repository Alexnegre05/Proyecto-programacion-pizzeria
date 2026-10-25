from src.datos.ingredientes import ingrediente_precio
from src.datos.ingredientes import ingredientes_gramos

def mostrar_ingredientes():

    print("\n")
    for ingrediente, precio in ingrediente_precio.items():
        
        print(ingrediente, "precio: ", precio*ingredientes_gramos[ingrediente]) 
        
        # esta formula es precio por gramo*cantidad de gramos en ingrediente, como sabemos que las claves en ambos diccionarios son iguales
        # no hace falta hacer dos for, uno recorre uno de los diccionarios y el otro diccionario sacamos valor por valor
        # usamos el .items para ello