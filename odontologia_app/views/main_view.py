from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo
import customtkinter
from controllers.cliente_controller import ClienteController
from controllers.ficha_odontologica_controller import FichaOdontologicaController
from controllers.ficha_ortodoncia_controller import FichaOrtodonciaController
from controllers.responsable_controller import ResponsableController
from .informacion_ortodoncia_view import view_otros_registros
from .ficha_odontologica_view import view_fichas_odontologicas
class MainView(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión Odontológica")
        self.geometry("800x750")
        self.minsize(1090,400)
        # Marco para el formulario de creación
        self.form_frame = customtkinter.CTkFrame(self, width=400)
        self.form_frame.pack(side="left", fill="both", expand=False, padx=10, pady=10)

        # Marco para la lista de clientes
        self.list_frame = customtkinter.CTkFrame(self, width=400)
        self.list_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.large_font = ("Arial", 18, "bold")
        self.medium_font = ("Arial", 16)
        self.small_font = ("Arial", 14)
        
        self.create_form()
        self.create_list()

    def create_form(self):
        # Marco contenedor principal (usando grid para controlar posiciones)
        container = customtkinter.CTkFrame(self.form_frame)
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Configuración del grid en el contenedor
        container.grid_rowconfigure(0, weight=1)  # Frame desplazable ocupa espacio ajustable
        container.grid_rowconfigure(1, weight=0)  # Espacio fijo para el botón
        container.grid_columnconfigure(0, weight=1)  # Ajusta el ancho dinámicamente

        # Marco para los datos desplazables
        form_frame_datos = customtkinter.CTkScrollableFrame(container, width=250, height=600)
        form_frame_datos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Etiqueta del formulario
        form_label = customtkinter.CTkLabel(form_frame_datos, text="Registrar Cliente", font=self.large_font)
        form_label.pack(pady=10)

        # Campos de información personal
        self.nombre_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Nombre", font=self.medium_font)
        self.nombre_entry.pack(pady=5, fill="x")

        self.edad_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Edad", font=self.medium_font)
        self.edad_entry.pack(pady=5, fill="x")

        self.direccion_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Dirección", font=self.medium_font)
        self.direccion_entry.pack(pady=5, fill="x")

        self.telefono_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Teléfono", font=self.medium_font)
        self.telefono_entry.pack(pady=5, fill="x")
        
        self.cedula_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Cédula", font=self.medium_font)
        self.cedula_entry.pack(pady=5, fill="x")

        # Campos médicos como entradas de texto
        medical_label = customtkinter.CTkLabel(form_frame_datos, text="Información Médica", font=self.large_font)
        medical_label.pack(pady=10)

        self.alergias_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Alergias (especificar)", font=self.medium_font)
        self.alergias_entry.pack(pady=5, fill="x")

        self.medicamentos_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Medicamentos Actuales", font=self.medium_font)
        self.medicamentos_entry.pack(pady=5, fill="x")

        self.hemorragias_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Hemorragias (Sí/No)", font=self.medium_font)
        self.hemorragias_entry.pack(pady=5, fill="x")

        self.problemas_cardiacos_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Problemas Cardíacos (Sí/No)", font=self.medium_font)
        self.problemas_cardiacos_entry.pack(pady=5, fill="x")

        self.diabetes_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Diabetes (Sí/No)", font=self.medium_font)
        self.diabetes_entry.pack(pady=5, fill="x")

        self.hipertension_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Hipertensión (Sí/No)", font=self.medium_font)
        self.hipertension_entry.pack(pady=5, fill="x")
        
        self.alergia_medicamentos_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Alergía a medicamentos (Sí/No)", font=self.medium_font)
        self.alergia_medicamentos_entry.pack(pady=5, fill="x")

        self.embarazo_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Embarazo (Sí/No)", font=self.medium_font)
        self.embarazo_entry.pack(pady=5, fill="x")

        self.anestesia_previa_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Anestesia previa (Sí/No)", font=self.medium_font)
        self.anestesia_previa_entry.pack(pady=5, fill="x")

        self.anemia_entry = customtkinter.CTkEntry(form_frame_datos, placeholder_text="Anemia (Sí/No)", font=self.medium_font)
        self.anemia_entry.pack(pady=5, fill="x")

        # Botón para guardar el cliente (fuera del scrollable frame)
        save_button = customtkinter.CTkButton(container, text="Guardar Cliente", command=self.save_cliente, font=self.medium_font)
        save_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10)  # Ocupa toda la fila en el contenedor

    def create_list(self):
        # Crear un estilo personalizado para el Treeview
        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=self.small_font)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        rowheight=40,
                        font=self.small_font,
                        padding=(1, 10))
        style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])

        # Campo de búsqueda
       # Marco para búsqueda
        search_frame = customtkinter.CTkFrame(self.list_frame)
        search_frame.pack(pady=10)

        # Marco para búsqueda por cédula (izquierda)
        search_cedula_frame = customtkinter.CTkFrame(search_frame)
        search_cedula_frame.pack(side="left", padx=10)

        search_cedula_label = customtkinter.CTkLabel(search_cedula_frame, text="Buscar por Cédula", font=self.large_font)
        search_cedula_label.pack(pady=5)

        self.search_cedula_entry = customtkinter.CTkEntry(search_cedula_frame, placeholder_text="Cédula", font=self.medium_font)
        self.search_cedula_entry.pack(pady=5)

        search_cedula_button = customtkinter.CTkButton(search_cedula_frame, text="Buscar", command=self.search_cliente_by_cedula, font=self.medium_font)
        search_cedula_button.pack(pady=5)

        # Marco para búsqueda por nombre (derecha)
        search_nombre_frame = customtkinter.CTkFrame(search_frame)
        search_nombre_frame.pack(side="right", padx=10)

        search_nombre_label = customtkinter.CTkLabel(search_nombre_frame, text="Buscar por Nombre", font=self.large_font)
        search_nombre_label.pack(pady=5)

        self.search_nombre_entry = customtkinter.CTkEntry(search_nombre_frame, placeholder_text="Nombre", font=self.medium_font)
        self.search_nombre_entry.pack(pady=5)

        search_nombre_button = customtkinter.CTkButton(search_nombre_frame, text="Buscar", command=self.search_cliente, font=self.medium_font)
        search_nombre_button.pack(pady=5)
        
        search_nombre_button = customtkinter.CTkButton(self.list_frame, text="Restablecer", command=self.update_list, font=self.medium_font)
        search_nombre_button.pack(pady=5)
        s_saldo= ttk.Style() 
        s_saldo.configure('saldo.Treeview.Heading', rowheight=45)
        # Tabla de clientes
        self.tree_principal = ttk.Treeview(
            self.list_frame,
            columns=("id", "numero", "nombre", "cedula","saldo_odontologico","saldo_ortodoncia"),
            show="headings",
            style="Treeview",
        )
        self.tree_principal.heading("numero", text="#")
        self.tree_principal.heading("nombre", text="Nombre")
        self.tree_principal.heading("cedula", text="Cédula")
        self.tree_principal.heading("saldo_odontologico", text="Saldo Od.")
        self.tree_principal.heading("saldo_ortodoncia", text="Saldo Or.")
        self.tree_principal.column("id", width=0, stretch="no")  # Columna oculta para el ID
        self.tree_principal.column("numero", anchor="center", width=50, stretch="no")
        self.tree_principal.column("nombre", anchor="w", width=250)
        self.tree_principal.column("cedula", anchor="center", width=170, stretch="no")
        self.tree_principal.column("saldo_odontologico", anchor="center", width=100, stretch="no")
        self.tree_principal.column("saldo_ortodoncia", anchor="center", width=100, stretch="no")
        self.tree_principal["displaycolumns"]=("numero", "nombre", "cedula","saldo_odontologico","saldo_ortodoncia")
        self.tree_principal.tag_configure("gray", background="#363a3b")  #  gray
        self.tree_principal.tag_configure("darkgray", background="#2a2d2e")  #  darkray
        # Crear scrollbar vertical
        tree_scrollbar = customtkinter.CTkScrollbar(self.list_frame, orientation="vertical", command=self.tree_principal.yview)
        tree_scrollbar.pack(side="right", fill="y")  # Colocarlo a la derecha del Treeview
        self.tree_principal.configure(yscrollcommand=tree_scrollbar.set)
        
        # Empaquetar Treeview
        self.tree_principal.pack(pady=10, side="left", fill="both", expand=True)
        # Asociar doble clic para mostrar detalles
        self.tree_principal.bind("<Double-1>", self.show_details)

        self.update_list()
        # Inicializar la lista
    def clear_form(self):
        self.nombre_entry.delete(0, "end")
        self.edad_entry.delete(0, "end")
        self.direccion_entry.delete(0, "end")
        self.telefono_entry.delete(0, "end")
        self.cedula_entry.delete(0, "end")
        self.alergias_entry.delete(0, "end")
        self.medicamentos_entry.delete(0, "end")
        self.hemorragias_entry.delete(0, "end")
        self.problemas_cardiacos_entry.delete(0, "end")
        self.diabetes_entry.delete(0, "end")
        self.hipertension_entry.delete(0, "end")
        self.alergia_medicamentos_entry.delete(0, "end")
        self.embarazo_entry.delete(0, "end")
        self.anestesia_previa_entry.delete(0, "end")
        self.anemia_entry.delete(0, "end")
         
    def save_cliente(self):
        # Obtener los valores del formulario
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()
        cedula = self.cedula_entry.get()
        alergias = self.alergias_entry.get()
        medicamentos = self.medicamentos_entry.get()
        hemorragias = self.hemorragias_entry.get()
        problemas_cardiacos = self.problemas_cardiacos_entry.get()
        diabetes = self.diabetes_entry.get()
        hipertension = self.hipertension_entry.get()
        alergia_medicamentos = self.alergia_medicamentos_entry.get()
        embarazo = self.embarazo_entry.get()
        anestesia_previa = self.anestesia_previa_entry.get()
        anemia = self.anemia_entry.get()

        # Validar entrada
        if not nombre or not edad:
            showwarning("Error", "Por favor completa los campos obligatorios (Nombre, edad).")
            return
        if not edad.isdigit():
            showwarning("Error", "La edad debe ser un número.")
            return


        # Guardar cliente usando el controlador
        ClienteController.crear_cliente(
            nombre=nombre,
            edad=int(edad),
            direccion=direccion,
            telefono=telefono,
            cedula=cedula,
            alergias=alergias,
            hemorragias=hemorragias,
            problemas_cardiacos=problemas_cardiacos,
            diabetes=diabetes,
            hipertension=hipertension,
            anemia=anemia,
            alergia_medicamentos=alergia_medicamentos,
            embarazo=embarazo,
            anestesia_previa=anestesia_previa,
            medicamentos=medicamentos,
        )

        showinfo("Éxito", "Cliente guardado correctamente.")
        self.update_list()  # Actualizar lista
        self.clear_form()   # Limpiar formulario

    def update_list(self):
        self.tree_principal.tag_configure("saldo_cero", background="#59C07A")  # Verde claro
        self.tree_principal.tag_configure("saldo_no_cero", background="#DD4151")  # Rojo claro
        # Limpiar lista
        for row in self.tree_principal.get_children():
            self.tree_principal.delete(row)
        # Obtener clientes del controlador
        clientes = ClienteController.obtener_clientes()
        start=2
        for idx, cliente in enumerate(clientes, start=1):
            modulo=start%2
            start+=1
            tag = "gray" if modulo == 0 else "darkgray"
            self.tree_principal.insert("", "end", values=(cliente.id, idx, cliente.nombre, cliente.cedula, cliente.saldo_total_od, cliente.saldo_total_or), tags=(tag,))

    def search_cliente_by_cedula(self):
        cedula = self.search_cedula_entry.get()
        if not cedula:
            self.update_list()  # Si no hay búsqueda, recarga la lista completa
            return

        # Filtrar clientes por cédula
        clientes = ClienteController.buscar_por_cedula(cedula)
        self.tree_principal.delete(*self.tree_principal.get_children())  # Limpiar tabla actual
        start=2
        for idx, cliente in enumerate(clientes, start=1):
            modulo=start%2
            start+=1
            tag = "gray" if modulo == 0 else "darkgray"
            self.tree_principal.insert("", "end", values=(cliente.id, idx, cliente.nombre, cliente.cedula, cliente.saldo_total_od, cliente.saldo_total_or), tags=(tag,))

    def search_cliente(self):
        nombre = self.search_nombre_entry.get()
        if not nombre:
            self.update_list()  # Si no hay búsqueda, recarga la lista completa
            return

        # Filtrar clientes por nombre
        clientes = ClienteController.buscar_por_nombre(nombre)
        self.tree_principal.delete(*self.tree_principal.get_children())  # Limpiar tabla actual
        start=2
        for idx, cliente in enumerate(clientes, start=1):
            modulo=start%2
            start+=1
            tag = "gray" if modulo == 0 else "darkgray"
            self.tree_principal.insert("", "end", values=(cliente.id, idx, cliente.nombre, cliente.cedula, cliente.saldo_total_od, cliente.saldo_total_or), tags=(tag,))

    def show_details(self, event):
        # Obtener la selección actual
        selected_item = self.tree_principal.selection()
        if not selected_item:
            return  # Salir si no hay ningún elemento seleccionado

        # Obtener el id del cliente desde la primera columna (oculta)
        values = self.tree_principal.item(selected_item, "values")
        if not values or len(values) < 1:
            return

        cliente_id = values[0]

        # Buscar cliente en la base de datos por ID
        cliente = ClienteController.obtener_cliente_por_id(cliente_id)
        if not cliente:
            showwarning("Error", "Cliente no encontrado.")
            return

        # Crear ventana para mostrar detalles
        details_window = customtkinter.CTkToplevel(self)
        details_window.title(f"Detalles de {cliente.nombre}")
        details_window.geometry("670x620")
        details_window.minsize(630,550)

        # Crear un frame con scroll
        scroll_frame = customtkinter.CTkScrollableFrame(
            details_window,
            width=360,
            height=400
        )
        scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Función para crear una fila de información
        def create_info_row(label, value,color):
            if (color=="gray"):
                row_frame = customtkinter.CTkFrame(scroll_frame, fg_color="#363a3b")
                row_frame.pack(fill="x", pady=2)
            if(color=="dark_gray"):
                row_frame = customtkinter.CTkFrame(scroll_frame, fg_color="#2a2d2e")
                row_frame.pack(fill="x", pady=2)
            
            label_widget = customtkinter.CTkLabel(
                row_frame,
                text=f"{label}:",
                font=self.large_font,
                width=150
            )
            label_widget.pack(side="left", padx=5)
            
            value_widget = customtkinter.CTkLabel(
                row_frame,
                text=str(value),
                font=self.medium_font,
                wraplength=200,  # Permite que el texto largo se envuelva
                justify="left"
            )
            value_widget.pack(side="left", padx=5, fill="x", expand=True)

        # Crear filas de información
        create_info_row("Nombre", cliente.nombre,"gray")
        create_info_row("Edad", cliente.edad,"dark_gray")
        create_info_row("Dirección", cliente.direccion,"gray")
        create_info_row("Teléfono", cliente.telefono,"dark_gray")
        create_info_row("Cédula", cliente.cedula,"gray")
        create_info_row("Alergias", cliente.alergias,"dark_gray")
        create_info_row("Medicamentos", cliente.medicamentos,"gray")
        create_info_row("Hemorragias", cliente.hemorragias,"dark_gray")
        create_info_row("Problemas Cardiacos", cliente.problemas_cardiacos,"gray")
        create_info_row("Diabetes", cliente.diabetes,"dark_gray")
        create_info_row("Hipertensión", cliente.hipertension,"gray")
        create_info_row("Alergias a medicamentos", cliente.alergia_medicamentos,"dark_gray")
        create_info_row("Embarazo", cliente.embarazo,"gray")
        create_info_row("Anestesia previa", cliente.anestesia_previa,"dark_gray")
        create_info_row("Anemia", cliente.anemia,"gray")

        # Frame para botones
        button_frame = customtkinter.CTkFrame(details_window)
        button_frame.pack(pady=10, padx=10, fill="x")

        # Botones
        edit_button = customtkinter.CTkButton(
            button_frame,
            text="Editar Cliente",
            command=lambda: self.edit_cliente(cliente.id, details_window),
            font=self.medium_font
        )
        edit_button.pack(side="left", padx=5, expand=True)

        odontologia_button = customtkinter.CTkButton(
            button_frame,
            text="Ver Fichas Odontológicas",
            command=lambda: view_fichas_odontologicas(self, cliente.id),
            font=self.medium_font
        )
        odontologia_button.pack(side="left", padx=5, expand=True)

        other_button = customtkinter.CTkButton(
            button_frame,
            text="Ver Fichas Ortodoncia",
            command=lambda: view_otros_registros(self, cliente.id),
            font=self.medium_font
        )
        other_button.pack(side="left", padx=5, expand=True)
        
        responsable_button = customtkinter.CTkButton(
            details_window,
            text="Ver Responsable",
            command=lambda: self.resposable_edit_view(cliente.id, details_window),
            font=self.medium_font
        )
        responsable_button.pack(pady=10)
        
        # Botón para cerrar
        close_button = customtkinter.CTkButton(
            details_window,
            text="Cerrar",
            command=details_window.destroy,
            font=self.medium_font
        )
        close_button.pack(pady=10)

    # Métodos adicionales para los botones
    def edit_cliente(self, cliente, parent_window):
        parent_window.destroy()  # Cerrar la ventana de detalles
        cliente = ClienteController.obtener_cliente_por_id(cliente)
        
        # Crear ventana de edición
        edit_window = customtkinter.CTkToplevel(self)
        edit_window.title(f"Editar Cliente: {cliente.nombre}")
        edit_window.geometry("500x750")
        edit_window.minsize(450,300)
        container_editar = customtkinter.CTkFrame(edit_window)
        container_editar.pack(fill="both", expand=True, padx=10, pady=10)

        # Configuración del grid en el contenedor
        container_editar.grid_rowconfigure(0, weight=1)  # Frame desplazable ocupa espacio ajustable
        container_editar.grid_rowconfigure(1, weight=0)  # Espacio fijo para el botón
        container_editar.grid_columnconfigure(0, weight=1)  # Ajusta el ancho dinámicamente

        # Marco para los datos desplazables
        form_frame_editar = customtkinter.CTkScrollableFrame(container_editar, width=200, height=600)
        form_frame_editar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Crear un marco para organizar los campos
        form_frame = customtkinter.CTkFrame(form_frame_editar)
        form_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Función auxiliar para crear etiquetas y entradas
        def create_labeled_entry(frame, label_text, initial_value):
            # Contenedor para cada fila
            row_frame = customtkinter.CTkFrame(frame)
            row_frame.pack(pady=5, fill="x")

            # Entrada de texto
            entry = customtkinter.CTkEntry(row_frame, font=self.medium_font)
            entry.insert(0, initial_value)
            entry.pack(side="right", padx=5, fill="x", expand=True)

            # Etiqueta a la derecha
            label = customtkinter.CTkLabel(row_frame, text=label_text, font=self.medium_font)
            label.pack(side="left", padx=5)

            return entry

        # Crear los campos con etiquetas
        nombre_entry = create_labeled_entry(form_frame, "Nombre", cliente.nombre)
        edad_entry = create_labeled_entry(form_frame, "Edad", str(cliente.edad))
        direccion_entry = create_labeled_entry(form_frame, "Dirección", cliente.direccion)
        telefono_entry = create_labeled_entry(form_frame, "Teléfono", cliente.telefono)
        cedula_entry = create_labeled_entry(form_frame, "Cédula", cliente.cedula)
        alergias_entry = create_labeled_entry(form_frame, "Alergias", cliente.alergias)
        hemorragias_entry = create_labeled_entry(form_frame, "Hemorragias", cliente.hemorragias)
        problemas_cardiacos_entry = create_labeled_entry(form_frame, "Problemas Cardiacos", cliente.problemas_cardiacos)
        diabetes_entry = create_labeled_entry(form_frame, "Diabetes", cliente.diabetes)
        hipertension_entry = create_labeled_entry(form_frame, "Hipertensión", cliente.hipertension)
        anemia_entry = create_labeled_entry(form_frame, "Anemia", cliente.anemia)
        alergia_medicamentos_entry = create_labeled_entry(form_frame, "Alergia a Medicamentos", cliente.alergia_medicamentos)
        embarazo_entry = create_labeled_entry(form_frame, "Embarazo", cliente.embarazo)
        anestesia_previa_entry = create_labeled_entry(form_frame, "Anestesia Previa", cliente.anestesia_previa)
        medicamentos_entry = create_labeled_entry(form_frame, "Medicamentos", cliente.medicamentos)

        # Botón para guardar cambios
        save_button = customtkinter.CTkButton(
            container_editar,
            text="Guardar Cambios",
            command=lambda: self.save_edits(
                cliente.id,
                nombre_entry.get(),
                edad_entry.get(),
                direccion_entry.get(),
                telefono_entry.get(),
                cedula_entry.get(),
                alergias_entry.get(),
                hemorragias_entry.get(),
                problemas_cardiacos_entry.get(),
                diabetes_entry.get(),
                hipertension_entry.get(),
                anemia_entry.get(),
                alergia_medicamentos_entry.get(),
                embarazo_entry.get(),
                anestesia_previa_entry.get(),
                medicamentos_entry.get(),
                edit_window
            ), font=self.medium_font
        )
        #save_button.pack(pady=10)
        save_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10) 
        # Botón para cerrar la ventana sin guardar
        close_button = customtkinter.CTkButton(container_editar, text="Cancelar", command=edit_window.destroy, font=self.medium_font)
        #close_button.pack(pady=10)
        close_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10) 
    def save_edits(self, cliente_id, nombre, edad, direccion, telefono, cedula, alergias, hemorragias, problemas_cardiacos, diabetes, hipertension, anemia, alergia_medicamentos, embarazo, anestesia_previa, medicamentos, edit_window):
        # Validar entrada
        if not nombre or not edad:
            showwarning("Error", "Por favor completa los campos obligatorios (Nombre, edad).", parent=edit_window)
            return
        if not edad.isdigit():
            showwarning("Error", "La edad debe ser un número.", parent=edit_window)
            return

        # Actualizar cliente usando el controlador
        ClienteController.actualizar_cliente(
            cliente_id=cliente_id,
            nombre=nombre,
            edad=int(edad),
            direccion=direccion,
            telefono=telefono,
            cedula=cedula,
            alergias=alergias,
            hemorragias = hemorragias,
            problemas_cardiacos = problemas_cardiacos,
            diabetes = diabetes,
            hipertension = hipertension,
            anemia = anemia,
            alergia_medicamentos = alergia_medicamentos,
            embarazo = embarazo,
            anestesia_previa = anestesia_previa,
            medicamentos=medicamentos
        )

        showinfo("Éxito", "Cliente actualizado correctamente.",  parent=edit_window)
        self.update_list()  # Actualizar la lista de clientes
        edit_window.destroy()  # Cerrar la ventana de edición
        
            # Métodos adicionales para los botones
    def resposable_edit_view(self, cliente, parent_window):
        
        responsable = ResponsableController.obtener_responsable_por_id(cliente)
        cliente = ClienteController.obtener_cliente_por_id(cliente)
        
        if responsable is None:
            responsable = type('Responsable', (object,), {
                'nombre': '',
                'edad': '',
                'direccion': '',
                'telefono': '',
                'cedula': '',
                'correo': ''
            })()
        
        # Crear ventana de edición
        responsable_window = customtkinter.CTkToplevel(self)
        responsable_window.title(f"Responsable de: {cliente.nombre}")
        responsable_window.geometry("500x750")
        responsable_window.minsize(450,300)
        responsable_window.attributes('-topmost', True)
        responsable_window.after(100, lambda: responsable_window.attributes('-topmost', False))
        container_editar = customtkinter.CTkFrame(responsable_window)
        container_editar.pack(fill="both", expand=True, padx=10, pady=10)

        # Configuración del grid en el contenedor
        container_editar.grid_rowconfigure(0, weight=1)  # Frame desplazable ocupa espacio ajustable
        container_editar.grid_rowconfigure(1, weight=0)  # Espacio fijo para el botón
        container_editar.grid_columnconfigure(0, weight=1)  # Ajusta el ancho dinámicamente

        # Marco para los datos desplazables
        form_frame_editar = customtkinter.CTkScrollableFrame(container_editar, width=200, height=600)
        form_frame_editar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Crear un marco para organizar los campos
        form_frame = customtkinter.CTkFrame(form_frame_editar)
        form_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Función auxiliar para crear etiquetas y entradas
        def create_labeled_entry(frame, label_text, initial_value):
            # Contenedor para cada fila
            row_frame = customtkinter.CTkFrame(frame)
            row_frame.pack(pady=5, fill="x")

            # Entrada de texto
            entry = customtkinter.CTkEntry(row_frame, font=self.medium_font)
            entry.insert(0, initial_value)
            entry.pack(side="right", padx=5, fill="x", expand=True)

            # Etiqueta a la derecha
            label = customtkinter.CTkLabel(row_frame, text=label_text, font=self.medium_font)
            label.pack(side="left", padx=5)

            return entry

        # Crear los campos con etiquetas
        nombre_entry = create_labeled_entry(form_frame, "Nombre", responsable.nombre)
        edad_entry = create_labeled_entry(form_frame, "Edad", str(responsable.edad))
        direccion_entry = create_labeled_entry(form_frame, "Dirección", responsable.direccion )
        telefono_entry = create_labeled_entry(form_frame, "Teléfono", responsable.telefono )
        cedula_entry = create_labeled_entry(form_frame, "Cédula", responsable.cedula)
        correo_entry = create_labeled_entry(form_frame, "Correo electrónico", responsable.correo)
        # Botón para guardar cambios
        save_button = customtkinter.CTkButton(
            container_editar,
            text="Guardar Cambios",
            command=lambda: self.save_responsable(
                cliente.id,
                nombre_entry.get(),
                edad_entry.get(),
                direccion_entry.get(),
                telefono_entry.get(),
                cedula_entry.get(),
                correo_entry.get(),
                responsable_window
            ), font=self.medium_font
        )
        #save_button.pack(pady=10)
        save_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10) 
        # Botón para cerrar la ventana sin guardar
        close_button = customtkinter.CTkButton(container_editar, text="Cancelar", command=responsable_window.destroy, font=self.medium_font)
        #close_button.pack(pady=10)
        close_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10) 
    def save_responsable(self, cliente_id, nombre, edad, direccion, telefono, cedula, correo, responsable_window):
        # Validar entrada
        if not edad.isdigit():
            showwarning("Error", "La edad debe ser un número.", parent=responsable_window)
            return

        # Verificar si ya existe un responsable
        responsable = ResponsableController.obtener_responsable_por_id(cliente_id)

        if responsable:
            # Actualizar responsable existente
            ResponsableController.actualizar_responsable(
                cliente_id=cliente_id,
                nombre=nombre,
                edad=int(edad),
                direccion=direccion,
                telefono=telefono,
                cedula=cedula,
                correo=correo
            )
            showinfo("Éxito", "Responsable actualizado correctamente.", parent=responsable_window)
        else:
            # Crear un nuevo responsable
            ResponsableController.crear_responsable(
                cliente_id=cliente_id,
                nombre=nombre,
                edad=int(edad),
                direccion=direccion,
                telefono=telefono,
                cedula=cedula,
                correo=correo
            )
            showinfo("Éxito", "Responsable creado correctamente.", parent=responsable_window)
