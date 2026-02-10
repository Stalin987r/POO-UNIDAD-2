# ==========================================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# ==========================================
# Programa que permite gestionar un inventario
# de productos usando Programación Orientada a Objetos
# ==========================================


# -------- CLASE PRODUCTO --------
class Producto:
    """
    Clase que representa un producto del inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados (encapsulamiento)
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        # Muestra la información del producto de forma legible
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# -------- CLASE INVENTARIO --------
class Inventario:
    """
    Clase que administra los productos del inventario.
    """

    def __init__(self):
        self.productos = []  # Lista que almacena objetos Producto

    def añadir_producto(self, producto):
        # Verifica que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑️ Producto eliminado correctamente.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        for p in self.productos:
            if p.get_id() == id_producto:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                print("✏️ Producto actualizado correctamente.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            print("\n📋 LISTA DE PRODUCTOS")
            for p in self.productos:
                print(p)


# -------- MENÚ DE USUARIO --------
def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIOS =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


# -------- PROGRAMA PRINCIPAL --------
def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\n🔍 Productos encontrados:")
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Gracias por usar el sistema de inventarios.")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")


# -------- EJECUCIÓN --------
if __name__ == "__main__":
    main()
