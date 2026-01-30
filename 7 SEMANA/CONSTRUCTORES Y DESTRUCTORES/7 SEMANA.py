class ArchivoRegistro:
    """
    Clase que representa un archivo de registro.
    Demuestra el uso de constructores y destructores en Python.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea un objeto.
        Inicializa los atributos y abre el archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "a", encoding="utf-8")
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir_mensaje(self, mensaje):
        """
        Método que escribe un mensaje en el archivo.
        """
        self.archivo.write(mensaje + "\n")
        print("Mensaje escrito en el archivo.")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto es eliminado
        o cuando finaliza el programa.
        Se utiliza para liberar recursos.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    # Creación del objeto (se ejecuta el constructor)
    registro = ArchivoRegistro("registro.txt")

    # Uso del objeto
    registro.escribir_mensaje("Inicio del programa")
    registro.escribir_mensaje("Registrando actividades del sistema")

    # Eliminación explícita del objeto (opcional)
    del registro

    print("Fin del programa.")
