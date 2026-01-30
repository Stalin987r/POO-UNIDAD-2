# ===============================
# Clase base
# ===============================
class Empleado:
    """
    Clase base que representa a un empleado.
    Aplica encapsulación usando atributos privados.
    """

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # Atributo privado (encapsulación)

    # Método getter
    def get_salario(self):
        return self.__salario

    # Método setter
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser mayor a 0")

    # Método que será sobrescrito (polimorfismo)
    def calcular_bono(self):
        return self.__salario * 0.10


# ===============================
# Clase derivada (Herencia)
# ===============================
class Gerente(Empleado):
    """
    Clase derivada que hereda de Empleado.
    Demuestra herencia y polimorfismo.
    """

    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Sobrescritura del método (Polimorfismo)
    def calcular_bono(self):
        return self.get_salario() * 0.20


# ===============================
# Programa principal
# ===============================
if __name__ == "__main__":
    # Creación de objetos (instancias)
    empleado1 = Empleado("Carlos", 800)
    gerente1 = Gerente("Ana", 1500, "Sistemas")

    # Uso de métodos
    print("Empleado:", empleado1.nombre)
    print("Salario:", empleado1.get_salario())
    print("Bono:", empleado1.calcular_bono())

    print("\nGerente:", gerente1.nombre)
    print("Departamento:", gerente1.departamento)
    print("Salario:", gerente1.get_salario())
    print("Bono:", gerente1.calcular_bono())
