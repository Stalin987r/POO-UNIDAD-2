# ==========================================
# SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO
# Ahora usa archivos y manejo de excepciones
# ==========================================

import os


# -------- CLASE PRODUCTO --------
class Producto:
    """
    Clase que representa un producto del inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
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
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

    def to_file_string(self):
        """Convierte el producto en formato para guardar en archivo"""
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}\n"


# -------- CLASE INVENTARIO --------
class Inventario:
    """
    Clase que administra los productos y los guarda en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # -------- CARGAR PRODUCTOS --------
    def cargar_desde_archivo(self):
        """Carga productos desde el archivo al iniciar el programa"""
        try:
            if not os.path.exists(self.archivo):
                # Si no existe, lo crea
                open(self.archivo, "w").close()
                print("📁 Archivo inventario.txt creado automáticamente.")
                return

            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_producto, nombre, cantidad, precio = datos
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)

            print("📂 Inventario cargado correctamente desde archivo.")

        except FileNotFoundError:
            print("❌ Error: Archivo no encontrado.")
        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"⚠️ Error inesperado al cargar archivo: {e}")

    # -------- GUARDAR PRODUCTOS --------
    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_file_string())
            print("💾 Cambios guardados correctamente en el archivo.")

        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"⚠️ Error inesperado al guardar archivo: {e}")

    # -------- MÉTODOS CRUD --------
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto añadido y guardado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("🗑️ Producto eliminado y archivo actualizado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad, precio):
        for p in self.productos:
            if p.get_id() == id_producto:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                self.guardar_en_archivo()
                print("✏️ Producto actualizado y cambios guardados.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

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

        try:
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

        except ValueError:
            print("❌ Error: Debes ingresar valores numéricos válidos para cantidad y precio.")
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}")


# -------- EJECUCIÓN --------
if __name__ == "__main__":
    main()
