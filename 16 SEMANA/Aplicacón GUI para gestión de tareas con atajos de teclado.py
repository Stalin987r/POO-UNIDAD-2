import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas (texto, estado)
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Botones
        self.btn_add = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.btn_add.pack(pady=5)

        self.btn_complete = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.btn_complete.pack(pady=5)

        self.btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.btn_delete.pack(pady=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        self.tasks.append((task_text, False))  # False = pendiente
        self.update_list()
        self.entry.delete(0, tk.END)

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task_text, status = self.tasks[index]
            self.tasks[index] = (task_text, True)  # True = completada
            self.update_list()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_list()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            if completed:
                self.listbox.insert(tk.END, "✔ " + task)
                self.listbox.itemconfig(tk.END, fg="green")
            else:
                self.listbox.insert(tk.END, "✗ " + task)
                self.listbox.itemconfig(tk.END, fg="red")


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()