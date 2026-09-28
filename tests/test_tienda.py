from clases.tienda import Tienda
from clases.producto import Producto
import pytest

# PRUEBA DE INTEGRACION, ocupan las 2 clases reales interactuando entre si
def test_agregar_y_buscar_producto():
    tienda = Tienda()
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda.agregar_producto(prod)
    
    resultado = tienda.buscar_producto("Laptop")
    assert resultado is not None
    assert resultado.precio == 1200

def test_buscar_producto_existente():
    tienda = Tienda()
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda.agregar_producto(prod)
    
    resultado = tienda.buscar_producto("Laptop")
    assert resultado is not None
    assert resultado.nombre == "Laptop"

def test_buscar_producto_no_existente():
    tienda = Tienda()
    
    with pytest.raises(Exception): # pytest.raises funciona como un assert, si algo en el cuerpo lanza una excepcion se pasa el test y si no se lanza da como fallo
        tienda.buscar_producto("Laptop")

def test_eliminar_producto_existente():
    tienda = Tienda()
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda.agregar_producto(prod)
    resultado = tienda.eliminar_producto("Laptop")
    assert resultado

def test_eliminar_producto_no_existente():
    tienda = Tienda()
    
    with pytest.raises(Exception):
        tienda.eliminar_producto("Laptop")

# PRUEBA UNITARIA
def test_tienda_inicia_inventario_vacio():
    tienda = Tienda()
    assert len(tienda.inventario) == 0