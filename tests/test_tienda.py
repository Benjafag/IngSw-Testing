from clases.tienda import Tienda
from clases.producto import Producto

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
    
    resultado = tienda.buscar_producto("Laptop")
    
    assert resultado is None

def test_eliminar_producto():
    tienda = Tienda()
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda.agregar_producto(prod)
    tienda.eliminar_producto("Laptop")
    resultado = tienda.buscar_producto("Laptop")
    
    assert resultado is None

# PRUEBA UNITARIA
def test_tienda_inicia_inventario_vacio():
    tienda = Tienda()
    assert len(tienda.inventario) == 0