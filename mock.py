from unittest.mock import MagicMock

mo = MagicMock(atributo1="valor1", atributo2="valor2")
print(mo.atributo1, mo.atributo2)

mo.stock.return_value = 50
print(mo.stock())

mo.__len__.return_value = 5
print(len(mo))