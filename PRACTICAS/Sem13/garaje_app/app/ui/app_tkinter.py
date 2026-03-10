import tkinter as tk
from tkinter import ttk, messagebox
import sys
from pathlib import Path
import re


# Agregar el directorio raíz al path para importaciones
sys.path.insert(0, str(Path(__file__).parent))

from servicios.garaje_servicio import GarajeServicio
from modelos.vehiculo import Vehiculo


class AppGaraje:
    """
    Interfaz gráfica principal del sistema de gestión de garaje.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.servicio = GarajeServicio()

        # Configuración de la ventana principal
        self.root.title("Sistema de Gestión de Garaje")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        # Configurar estilo
        self.configurar_estilos()

        # Crear widgets
        self.crear_interfaz()

    def configurar_estilos(self):
        """Configura los estilos visuales de la aplicación."""
        style = ttk.Style()
        style.theme_use('clam')

        # Estilos personalizados
        style.configure('Title.TLabel',
                        font=('Arial', 18, 'bold'),
                        foreground='#2c3e50')
        style.configure('Subtitle.TLabel',
                        font=('Arial', 10, 'bold'),
                        foreground='#34495e')
        style.configure('Action.TButton',
                        font=('Arial', 10, 'bold'),
                        padding=10)

    def crear_interfaz(self):
        """Crea todos los componentes de la interfaz gráfica."""

        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Título
        titulo = ttk.Label(main_frame,
                           text="🚗 Sistema de Gestión de Garaje",
                           style='Title.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Frame de formulario
        self.crear_formulario(main_frame)

        # Frame de botones
        self.crear_botones(main_frame)

        # Frame de lista de vehículos
        self.crear_tabla_vehiculos(main_frame)

    def crear_formulario(self, parent):
        """Crea el formulario de entrada de datos."""
        form_frame = ttk.LabelFrame(parent,
                                    text="Información del Vehículo",
                                    padding="15")
        form_frame.grid(row=1, column=0, columnspan=2,
                        sticky=(tk.W, tk.E), pady=(0, 15))

        # Placa
        ttk.Label(form_frame, text="Placa:",
                  style='Subtitle.TLabel').grid(row=0, column=0,
                                                sticky=tk.W, pady=5)
        self.entry_placa = ttk.Entry(form_frame, width=30, font=('Arial', 10))
        self.entry_placa.grid(row=0, column=1, padx=(10, 0), pady=5, sticky=tk.W)

        # Marca
        ttk.Label(form_frame, text="Marca:",
                  style='Subtitle.TLabel').grid(row=1, column=0,
                                                sticky=tk.W, pady=5)
        self.entry_marca = ttk.Entry(form_frame, width=30, font=('Arial', 10))
        self.entry_marca.grid(row=1, column=1, padx=(10, 0), pady=5, sticky=tk.W)

        # Propietario
        ttk.Label(form_frame, text="Propietario:",
                  style='Subtitle.TLabel').grid(row=2, column=0,
                                                sticky=tk.W, pady=5)
        self.entry_propietario = ttk.Entry(form_frame, width=30, font=('Arial', 10))
        self.entry_propietario.grid(row=2, column=1, padx=(10, 0), pady=5, sticky=tk.W)

    def crear_botones(self, parent):
        """Crea los botones de acción."""
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(0, 15))

        # Botón Agregar
        btn_agregar = ttk.Button(button_frame,
                                 text="➕ Agregar Vehículo",
                                 style='Action.TButton',
                                 command=self.agregar_vehiculo)
        btn_agregar.grid(row=0, column=0, padx=5)

        # Botón Eliminar
        btn_eliminar = ttk.Button(button_frame,
                                  text="❌ Eliminar Vehículo",
                                  style='Action.TButton',
                                  command=self.eliminar_vehiculo)
        btn_eliminar.grid(row=0, column=1, padx=5)

        # Botón Limpiar
        btn_limpiar = ttk.Button(button_frame,
                                 text="🗑️ Limpiar",
                                 style='Action.TButton',
                                 command=self.limpiar_campos)
        btn_limpiar.grid(row=0, column=3, padx=5)

        # Botón Exportar
        btn_exportar = ttk.Button(button_frame,
                                  text="💾 Exportar TXT",
                                  style='Action.TButton',
                                  command=self.exportar_txt)
        btn_exportar.grid(row=0, column=2, padx=5)

    def crear_tabla_vehiculos(self, parent):
        """Crea la tabla para mostrar los vehículos registrados."""
        list_frame = ttk.LabelFrame(parent,
                                    text="Vehículos Registrados",
                                    padding="15")
        list_frame.grid(row=3, column=0, columnspan=2,
                        sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear Treeview con scrollbar
        columns = ('placa', 'marca', 'propietario')
        self.tree = ttk.Treeview(list_frame, columns=columns,
                                 show='headings', height=10)

        # Definir encabezados
        self.tree.heading('placa', text='Placa')
        self.tree.heading('marca', text='Marca')
        self.tree.heading('propietario', text='Propietario')

        # Configurar columnas
        self.tree.column('placa', width=150, anchor=tk.CENTER)
        self.tree.column('marca', width=200, anchor=tk.CENTER)
        self.tree.column('propietario', width=250, anchor=tk.CENTER)

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL,
                                  command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Grid
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    # Validaciones

    def validar_placa(self, placa):
        """
        Valida formato de placa ecuatoriana: ABC-1234
        """
        patron = r'^[A-Z]{3}-\d{4}$'
        return re.match(patron, placa.upper())


    # Agregar vehículos al listado
    def agregar_vehiculo(self):
        """Maneja el evento de agregar un vehículo."""

        #Forzamos la entrada de mayúsculas automáticamente
        placa = self.entry_placa.bind("<KeyRelease>", lambda e: self.entry_placa.insert(0, self.entry_placa.get().upper()))
        marca = self.entry_marca.get().strip()
        propietario = self.entry_propietario.get().strip()

        # Validar campos vacíos
        if not placa or not marca or not propietario:
            messagebox.showwarning(
                "Campos vacíos",
                "Todos los campos son obligatorios."
            )
            return

        # Validar formato de placa
        if not self.validar_placa(placa):
            messagebox.showerror(
                "Placa inválida",
                "Formato de placa incorrecto.\nDebe ser: ABC-1234"
            )
            return

        vehiculo = Vehiculo(placa, marca, propietario)

        if self.servicio.agregar_vehiculo(vehiculo):

            self.tree.insert('', tk.END,
                             values=(vehiculo.placa,
                                     vehiculo.marca,
                                     vehiculo.propietario))

            self.limpiar_campos()

            messagebox.showinfo(
                "Éxito",
                f"Vehículo {placa} registrado correctamente."
            )

        else:
            messagebox.showerror(
                "Error",
                f"La placa {placa} ya está registrada."
            )
    # Eliminar vehículos del listado
    def eliminar_vehiculo(self):
        """Elimina el vehículo seleccionado de la tabla."""
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Selección requerida",
                                   "Seleccione un vehículo para eliminar.")
            return

        confirmacion = messagebox.askyesno(
            "Confirmar",
            "¿Está seguro de eliminar el vehículo seleccionado?"
        )

        if confirmacion:
            for item in seleccionado:
                self.tree.delete(item)

    # Limpiar campos de los inputs

    def limpiar_campos(self):
        """Limpia todos los campos del formulario."""
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)
        self.entry_placa.focus()

    # Exportar listado de vehículos a .txt
    def exportar_txt(self):
        """Exporta la lista de vehículos a un archivo TXT."""
        vehiculos = self.tree.get_children()

        if not vehiculos:
            messagebox.showwarning("Lista vacía",
                                   "No hay vehículos para exportar.")
            return

        try:
            with open("vehiculos.txt", "w", encoding="utf-8") as f:
                f.write("LISTA DE VEHÍCULOS\n")
                f.write("---------------------------\n")

                for item in vehiculos:
                    placa, marca, propietario = self.tree.item(item)["values"]
                    linea = f"Placa: {placa} | Marca: {marca} | Propietario: {propietario}\n"
                    f.write(linea)

            messagebox.showinfo("Exportación exitosa",
                                "La lista se guardó como vehiculos.txt")

        except Exception as e:
            messagebox.showerror("Error", str(e))


