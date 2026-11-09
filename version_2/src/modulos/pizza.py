from version_2.src.modulos.producto import Producto

class Pizza(Producto):
    def __init__(self, nombre, precio, ingredientes): # Le enviamos el nombre y precio a la clase madre (Producto)
        
        super().__init__(nombre, precio)
        
        self.ingredientes = ingredientes # Guardamos el parámetro específico de la subclase

        