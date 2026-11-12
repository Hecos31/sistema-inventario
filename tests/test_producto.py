
import io
import os
import sys
import unittest
from unittest.mock import patch

# Permite importar src/producto.py desde la carpeta tests/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.producto import Producto


class TestProducto(unittest.TestCase):

    def setUp(self):
        # Producto base para CP01 - CP06
        self.producto1 = Producto("P001", "Teclado", 350, 10)

    def test_cp01_crear_producto(self):
        """CP01: Crear un producto con los datos proporcionados"""
        self.assertIsInstance(self.producto1, Producto)
        self.assertEqual(self.producto1.codigo, "P001")
        self.assertEqual(self.producto1.nombre, "Teclado")
        self.assertEqual(self.producto1.precio, 350)
        self.assertEqual(self.producto1.existencia, 10)

    def test_cp02_mostrar_codigo(self):
        """CP02: Mostrar el código"""
        with patch('sys.stdout', new=io.StringIO()) as salida_capturada:
            self.producto1.mostrar_informacion()
            texto = salida_capturada.getvalue()
        self.assertIn("P001", texto)

    def test_cp03_mostrar_nombre(self):
        """CP03: Mostrar el nombre"""
        with patch('sys.stdout', new=io.StringIO()) as salida_capturada:
            self.producto1.mostrar_informacion()
            texto = salida_capturada.getvalue()
        self.assertIn("Teclado", texto)

    def test_cp04_mostrar_precio(self):
        """CP04: Mostrar el precio"""
        with patch('sys.stdout', new=io.StringIO()) as salida_capturada:
            self.producto1.mostrar_informacion()
            texto = salida_capturada.getvalue()
        self.assertIn("350", texto)

    def test_cp05_mostrar_existencia(self):
        """CP05: Mostrar la existencia"""
        with patch('sys.stdout', new=io.StringIO()) as salida_capturada:
            self.producto1.mostrar_informacion()
            texto = salida_capturada.getvalue()
        self.assertIn("10", texto)

    def test_cp06_mostrar_informacion_completa(self):
        """CP06: Mostrar información completa"""
        with patch('sys.stdout', new=io.StringIO()) as salida_capturada:
            self.producto1.mostrar_informacion()
            texto = salida_capturada.getvalue()
        for dato in ["P001", "Teclado", "350", "10"]:
            self.assertIn(dato, texto)

    def test_cp07_crear_otro_producto(self):
        """CP07: Crear otro producto sin confundir sus datos con el primero"""
        producto2 = Producto("P002", "Mouse", 180, 5)
        self.assertEqual(producto2.codigo, "P002")
        self.assertEqual(producto2.nombre, "Mouse")
        self.assertEqual(producto2.precio, 180)
        self.assertEqual(producto2.existencia, 5)
        # Verificar que el primero no fue alterado
        self.assertEqual(self.producto1.codigo, "P001")
        self.assertEqual(self.producto1.nombre, "Teclado")


if __name__ == "__main__":
    unittest.main(verbosity=2)
