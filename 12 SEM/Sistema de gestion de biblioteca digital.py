# ============================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ============================================

# -------------------------------
# Clase Libro
# -------------------------------
class Libro:
    """
    Representa un libro dentro de la biblioteca.
    - titulo y autor se almacenan en una TUPLA porque son inmutables.
    - categoria puede variar.
    - isbn identifica de forma única al libro.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # Estado del libro

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Disponible: {self.disponible}"


# -------------------------------
# Clase Usuario
# -------------------------------
class Usuario:
    """
    Representa un usuario de la biblioteca.
    - nombre
    - id_usuario (único)
    - libros_prestados (lista)
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de ISBNs

    def prestar_libro(self, isbn):
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn):
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {self.libros_prestados}"


# -------------------------------
# Clase Biblioteca
# -------------------------------
class Biblioteca:
    """
    Gestiona:
    - Libros (diccionario: ISBN -> Libro)
    - Usuarios (diccionario: ID -> Usuario)
    - Conjunto de IDs para garantizar unicidad
    """

    def __init__(self):
        self.libros = {}  # Diccionario ISBN -> Libro
        self.usuarios = {}  # Diccionario ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # ---------------------------
    # Gestión de libros
    # ---------------------------
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ---------------------------
    # Gestión de usuarios
    # ---------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("ID de usuario ya existe.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ---------------------------
    # Préstamos
    # ---------------------------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro.disponible:
                libro.disponible = False
                usuario.prestar_libro(isbn)
                print("Préstamo realizado con éxito.")
            else:
                print("El libro no está disponible.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if isbn in usuario.libros_prestados:
                libro.disponible = True
                usuario.devolver_libro(isbn)
                print("Libro devuelto correctamente.")
            else:
                print("El usuario no tiene este libro.")
        else:
            print("Usuario o libro no encontrado.")

    # ---------------------------
    # Búsquedas
    # ---------------------------
    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        return resultados

    # ---------------------------
    # Listar libros prestados
    # ---------------------------
    def listar_libros_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            return "Usuario no encontrado."


# ============================================
# PRUEBA DEL SISTEMA
# ============================================

if __name__ == "__main__":

    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Python Básico", "Juan Pérez", "Programación", "111")
    libro2 = Libro("Estructuras de Datos", "Ana López", "Programación", "222")
    libro3 = Libro("Historia Universal", "Carlos Ruiz", "Historia", "333")

    # Agregar libros
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("María", "U001")
    usuario2 = Usuario("Pedro", "U002")

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Realizar préstamo
    biblioteca.prestar_libro("U001", "111")

    # Listar libros prestados
    print("Libros prestados a María:", biblioteca.listar_libros_usuario("U001"))

    # Devolver libro
    biblioteca.devolver_libro("U001", "111")

    # Buscar libro
    resultados = biblioteca.buscar_por_categoria("Programación")
    print("Libros encontrados en categoría Programación:")
    for libro in resultados:
        print(libro)