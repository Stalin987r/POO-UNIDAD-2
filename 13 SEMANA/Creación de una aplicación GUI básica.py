import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos - Aplicación GUI")
        self.root.geometry("400x300")

        # Etiqueta
        self.etiqueta = tk.Label(root, text="Ingrese un dato:")
        self.etiqueta.pack(pady=5)

        # Campo de texto
        self.entrada = tk.Entry(root, width=30)
        self.entrada.pack(pady=5)

        # Botón agregar
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

        # Lista
        self.lista = tk.Listbox(root, width=40, height=10)
        self.lista.pack(pady=10)

        # Botón limpiar
        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_dato)
        self.boton_limpiar.pack(pady=5)

    def agregar_dato(self):
        dato = self.entrada.get()

        if dato != "":
            self.lista.insert(tk.END, dato)
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese un dato")

    def limpiar_dato(self):
        seleccion = self.lista.curselection()

        if seleccion:
            self.lista.delete(seleccion)
        else:
            self.lista.delete(0, tk.END)


# Crear ventana
root = tk.Tk()

# Crear objeto de la aplicación
app = AplicacionGUI(root)

# Ejecutar
root.mainloop()