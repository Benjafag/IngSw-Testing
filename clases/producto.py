class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.categoria})"

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
        else:
            raise Exception("No se puede modificar el precio con un valor negativo")