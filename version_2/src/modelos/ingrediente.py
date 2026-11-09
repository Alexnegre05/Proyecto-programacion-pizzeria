from version_2.src.datos.ingredientes import lista_ingredientes

class Ingrediente:
    def __init__(self,nombre, precio, gramos):
        self.nombre = nombre
        self.precio = precio
        self.gramos = gramos
        
    def coste_ingrediente_v2(self):

        return self.precio * self.gramos
    
            