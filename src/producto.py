# Archivo: src/producto.py

class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print("--- Detalles del Producto ---")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Inventario: {self.existencia} unidades\n")

# Bloque de prueba para verificar que funciona
if __name__ == "__main__":
    producto1 = Producto("PROD-001", "Monitor Gamer 24 pulg", 3500.00, 10)
    producto1.mostrar_informacion()