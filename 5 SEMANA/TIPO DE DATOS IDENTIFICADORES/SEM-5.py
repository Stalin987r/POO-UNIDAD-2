"""
Programa: Conversor de Temperatura usando POO
Funcionalidad:
Este programa convierte una temperatura de grados Celsius a Fahrenheit
y determina si la temperatura es considerada alta.
"""

class ConversorTemperatura:
    """
    Clase que representa un conversor de temperatura.
    """

    def __init__(self, temperatura_celsius):
        # Atributo de tipo float
        self.temperatura_celsius = temperatura_celsius

        # Atributo de tipo integer
        self.limite_temperatura = 30

    def convertir_a_fahrenheit(self):
        """
        Convierte la temperatura de Celsius a Fahrenheit.
        """
        return (self.temperatura_celsius * 9 / 5) + 32

    def es_temperatura_alta(self):
        """
        Determina si la temperatura es mayor al límite establecido.
        Retorna un valor boolean.
        """
        return self.temperatura_celsius > self.limite_temperatura


# Entrada de datos (float)
temperatura_ingresada = float(input("Ingrese la temperatura en grados Celsius: "))

# Creación del objeto (instancia de la clase)
conversor = ConversorTemperatura(temperatura_ingresada)

# Uso de métodos POO
temperatura_fahrenheit = conversor.convertir_a_fahrenheit()
temperatura_alta = conversor.es_temperatura_alta()

# Mensajes (string)
mensaje = "La temperatura es alta." if temperatura_alta else "La temperatura es normal o baja."

# Salida de resultados
print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit} °F")
print(mensaje)
