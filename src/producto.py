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
        print(f"Precio: ${self.precio }")
        print(f"Inventario: {self.existencia} unidades\n")

# NUEVA FUNCIÓN PARA EL RETO
def buscar_producto(lista_productos, codigo_buscado):
    for producto in lista_productos:
        if producto.codigo == codigo_buscado:
            print("Producto disponible en inventario")
            return producto
    print("Producto no encontrado")
    return None

if __name__ == "__main__":
    p1 = Producto("PROD-001", "Monitor Gamer", 3500.00, 10)
    p2 = Producto("PROD-002", "Teclado Mecánico", 850.00, 25)
    inventario = [p1, p2]
    
    # Probar búsqueda
    buscar_producto(inventario, "PROD-001")
