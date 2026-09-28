from clases.producto import Producto

#PRUEBA UNITARIA
def test_producto_creacion():
    prod = Producto("Laptop",1200,"Tecnologia")
    assert prod.nombre == "Laptop"
    assert prod.precio == 1200
    assert prod.categoria == "Tecnologia"