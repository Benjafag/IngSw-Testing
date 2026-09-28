from clases.producto import Producto
import pytest

#PRUEBA UNITARIA
def test_producto_creacion():
    prod = Producto("Laptop",1200,"Tecnologia")
    assert prod.nombre == "Laptop"
    assert prod.precio == 1200
    assert prod.categoria == "Tecnologia"
    
def test_actualizar_precio_negativo():
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    with pytest.raises(Exception):
        prod.actualizar_precio(-1)