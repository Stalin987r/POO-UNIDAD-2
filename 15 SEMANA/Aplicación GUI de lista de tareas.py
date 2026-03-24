import tkinter as tk

# Clase principal de la aplicación (POO)
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista donde guardamos las tareas
        self.tareas = []

        # ====== Campo de entrada ======
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento: presionar Enter para añadir tarea
        self.entry.bind("<Return>", self.agregar_tarea)

        # ====== Lista de tareas ======
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Evento opcional: doble clic para marcar como completada
        self.listbox.bind("<Double-Button-1>", self.marcar_completada)

        # ====== Botones ======
        btn_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        btn_agregar.pack(pady=5)

        btn_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.pack(pady=5)

        btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.pack(pady=5)

    # ====== Función para añadir tarea ======
    def agregar_tarea(self, event=None):
        tarea = self.entry.get()

        # Validar que no esté vacía
        if tarea != "":
            self.tareas.append(tarea)
            self.listbox.insert(tk.END, tarea)
            self.entry.delete(0, tk.END)

    # ====== Función para marcar como completada ======
    def marcar_completada(self, event=None):
        try:
            indice = self.listbox.curselection()[0]
            tarea = self.listbox.get(indice)

            # Evitar marcar dos veces
            if not tarea.startswith("✔ "):
                tarea_completada = "✔ " + tarea
                self.listbox.delete(indice)
                self.listbox.insert(indice, tarea_completada)

        except IndexError:
            pass  # Si no selecciona nada, no hace nada

    # ====== Función para eliminar tarea ======
    def eliminar_tarea(self):
        try:
            indice = self.listbox.curselection()[0]
            self.listbox.delete(indice)
        except IndexError:
            pass


# ====== Ejecución de la aplicación ======
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()