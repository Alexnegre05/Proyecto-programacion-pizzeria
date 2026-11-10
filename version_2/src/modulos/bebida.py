from version_2.src.modelos.producto import Producto

class Bebida(Producto):

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def mostrar(self):
        return "la bebida: ", self.nombre, "tiene: ", self.precio





    