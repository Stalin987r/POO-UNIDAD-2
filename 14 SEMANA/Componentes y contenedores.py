import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar  # Instalación de tkcalendar: pip install tkcalendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de eventos
        self.eventos = []

        # Crear la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        # Frame para la lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10)

        # Treeview para mostrar los eventos
        self.columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=self.columns, show="headings")
        self.tree.pack()

        # Configurar columnas
        for col in self.columns:
            self.tree.heading(col, text=col)

        # Frame para los campos de entrada
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10)

        # Etiquetas y entradas para fecha, hora y descripción
        label_fecha = tk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):")
        label_fecha.grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = tk.Entry(frame_entrada)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        label_hora = tk.Label(frame_entrada, text="Hora (hh:mm):")
        label_hora.grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        label_desc = tk.Label(frame_entrada, text="Descripción:")
        label_desc.grid(row=2, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(frame_entrada)
        self.entry_desc.grid(row=2, column=1, padx=5, pady=5)

        # Botones para agregar, eliminar y salir
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

        btn_salir = tk.Button(frame_botones, text="Salir", command=self.salir)
        btn_salir.grid(row=0, column=2, padx=5, pady=5)

        # Frame para el calendario (DatePicker)
        frame_calendario = tk.Frame(self.root)
        frame_calendario.pack(pady=10)

        # Calendar widget para seleccionar la fecha
        self.cal = Calendar(frame_calendario, selectmode='day', date_pattern='dd/mm/yyyy')
        self.cal.pack()

    def agregar_evento(self):
        """Agrega un nuevo evento a la lista de eventos."""
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        # Insertar el evento en el Treeview
        self.tree.insert('', 'end', values=(fecha, hora, descripcion))
        self.eventos.append((fecha, hora, descripcion))  # Guardar el evento en la lista

        # Limpiar los campos de entrada
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado después de confirmar."""
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este evento?")
        if confirmacion:
            item = self.tree.item(seleccionado)
            evento = item['values']
            self.eventos.remove(tuple(evento))  # Eliminar de la lista de eventos
            self.tree.delete(seleccionado)

    def salir(self):
        """Cierra la aplicación."""
        self.root.quit()


# Crear la ventana principal
root = tk.Tk()

# Crear una instancia de la aplicación
app = AgendaApp(root)

# Iniciar la aplicación
root.mainloop()