from clases.tienda import Tienda
from clases.producto import Producto
import pytest
import types

# FIXTURE
@pytest.fixture
def tienda_fixture():
    tienda = Tienda()
    tienda.agregar_producto(Producto("Laptop", 1200, "Tecnologia"))
    tienda.agregar_producto(Producto("Mouse", 25, "Accesorios"))
    tienda.agregar_producto(Producto("Impresora", 2000, "Tecnologia"))
    return tienda 

# PRUEBA DE INTEGRACION, ocupan las 2 clases reales interactuando entre si
def test_agregar_y_buscar_producto(tienda_fixture):
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda_fixture.agregar_producto(prod)
    
    resultado = tienda_fixture.buscar_producto("Laptop")
    assert resultado is not None
    assert resultado.precio == 1200

def test_buscar_producto_existente(tienda_fixture):
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda_fixture.agregar_producto(prod)
    
    resultado = tienda_fixture.buscar_producto("Laptop")
    assert resultado is not None
    assert resultado.nombre == "Laptop"

def test_buscar_producto_no_existente():
    tienda = Tienda()
    with pytest.raises(Exception): # pytest.raises funciona como un assert, si algo en el cuerpo lanza una excepcion se pasa el test y si no se lanza da como fallo
        tienda_fixture.buscar_producto("Laptop")

def test_eliminar_producto_existente(tienda_fixture):
    prod = Producto("Laptop", 1200, "Tecnologia")
    
    tienda_fixture.agregar_producto(prod)
    resultado = tienda_fixture.eliminar_producto("Laptop")
    assert resultado

def test_eliminar_producto_no_existente():
    tienda = Tienda()
    with pytest.raises(Exception):
        tienda.eliminar_producto("Laptop")

# PRUEBA UNITARIA
def test_tienda_inicia_inventario_vacio():
    tienda = Tienda()
    assert len(tienda.inventario) == 0
  

from unittest.mock import MagicMock
def test_actualizar_precio_doble_valido():
    tienda = Tienda()
    prod = MagicMock(nombre = "Laptop", precio = 1200)
    def actualizar_prec(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
        else:
            raise Exception("No se puede modificar el precio con un valor negativo")
    prod.actualizar_precio = types.MethodType(actualizar_prec, prod)

    tienda.agregar_producto(prod)
    tienda.aplicar_descuento("Laptop", .5)
    
    res = tienda.buscar_producto("Laptop")
    assert res.precio == 600
    

def test_actualizar_precio_doble_invalido():
    tienda = Tienda()
    prod = MagicMock(nombre = "Laptop", precio = 1200)
    def actualizar_prec(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.precio = nuevo_precio
        else:
            raise Exception("No se puede modificar el precio con un valor negativo")
    prod.actualizar_precio = types.MethodType(actualizar_prec, prod)

    tienda.agregar_producto(prod)
    with pytest.raises(Exception):
        tienda.aplicar_descuento("Laptop", -0.5)
         
def test_precio_carrito(tienda_fixture):
    carrito = ["Laptop", "Impresora", "Laptop"]
    res = tienda_fixture.calcular_total_carrito(carrito)
    assert res == 4400
    
def test_precio_carrito_con_descuento(tienda_fixture):
    tienda_fixture.aplicar_descuento("Impresora", .5)
    carrito = ["Impresora", "Mouse"]
    precio = tienda_fixture.calcular_total_carrito(carrito)
    assert precio == 1025
    
