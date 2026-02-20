import json


# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único para el producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en inventario
        self.precio = precio  # Precio del producto

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario que almacena productos

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if
                      nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_todos_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        # Guardar inventario en archivo (en formato JSON)
        with open(archivo, 'w') as f:
            inventario_data = {str(id_producto): vars(producto) for id_producto, producto in self.productos.items()}
            json.dump(inventario_data, f)

    def cargar_inventario(self, archivo):
        # Cargar inventario desde un archivo JSON
        try:
            with open(archivo, 'r') as f:
                inventario_data = json.load(f)
                for id_producto, data in inventario_data.items():
                    producto = Producto(data['id_producto'], data['nombre'], data['cantidad'], data['precio'])
                    self.productos[producto.get_id()] = producto
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")


# Funciones del menú
def mostrar_menu():
    print("=== Sistema de Gestión de Inventario ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")


def ejecutar_programa():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido con éxito.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado si existía.")

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco si no deseas cambiar): ")
            precio = input("Nuevo precio (deja en blanco si no deseas cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)
            print("Producto actualizado si existía.")

        elif opcion == '4':
            nombre = input("Introduce el nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_por_nombre(nombre)
            if productos_encontrados:
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            archivo = input("Introduce el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)
            print("Inventario guardado correctamente.")

        elif opcion == '7':
            archivo = input("Introduce el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(archivo)
            print("Inventario cargado correctamente.")

        elif opcion == '8':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el programa
if __name__ == '__main__':
    ejecutar_programa()
