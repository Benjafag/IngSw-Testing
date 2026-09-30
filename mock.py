
from unittest.mock import MagicMock

# si no tengo la clase
mo = MagicMock(atributo1="valor1", atributo2="valor2")
print(mo.atributo1, mo.atributo2)

mo.stock.return_value = 50
print(mo.stock())

mo.__len__.return_value = 5
print(len(mo))


# ====================================================================================


# si ya tengo la clase y quiero modificar el comportamiento de metodos o atributos ya creados
# pip install pytest-mock

import requests

class ServicioClima:
    def obtener_temperatura_api(self, ciudad):
        respuesta = requests.get(f"https://api.clima.com/{ciudad}")
        return respuesta.json()["temp"]

    def obtener_clima_actual(self, ciudad):
        temp = self.obtener_temperatura_api(ciudad)
        if temp > 30:
            return "Caluroso"
        return "Agradable"

def test_obtener_clima_caluroso(mocker):
    # 1. Se crea una instancia del servicio
    servicio = ServicioClima()

    # 2. Usar mocker.patch para interceptar el método externo 'obtener_temperatura_api'
    # y forzarlo a que devuelva un valor controlado (por ejemplo, 35) en lugar de llamar a la API real.
    mocker.patch.object(servicio, 'obtener_temperatura_api', return_value=35)

    # 3. Ejecutar el metodo a probar
    resultado = servicio.obtener_clima_actual("Madrid")

    # 4. Validar el resultado
    assert resultado == "Caluroso"

    # Opcional: Asegurar que el método fue llamado exactamente una vez con el argumento "Madrid"
    servicio.obtener_temperatura_api.assert_called_once_with("Madrid")