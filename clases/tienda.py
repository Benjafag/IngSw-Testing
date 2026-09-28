from clases.producto import Producto

class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.inventario.remove(producto)
            return True # Producto eliminado con exito
        return False # Producto no encontrado