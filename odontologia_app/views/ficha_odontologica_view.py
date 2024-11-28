from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo
import customtkinter
from controllers.cliente_controller import ClienteController
from controllers.ficha_odontologica_controller import FichaOdontologicaController
from datetime import datetime
from tkcalendar import DateEntry

def view_fichas_odontologicas(self, cliente_id):
    # Crear ventana para fichas odontológicas
    fichas_window = customtkinter.CTkToplevel(self)
    cliente = ClienteController.obtener_cliente_por_id(cliente_id)
    fichas_window.title(f"Fichas odontológicas de {cliente.nombre}")
    fichas_window.geometry("900x600")
    fichas_window.attributes('-topmost', True)
    fichas_window.after(100, lambda: fichas_window.attributes('-topmost', False))
    def calcular_saldo_total():
        saldo_total=0
        sum_costo=0
        sum_abono=0
        fichas = FichaOdontologicaController.obtener_fichas_por_cliente(cliente_id)
        for ficha in fichas:
            sum_costo+=ficha.costo
            sum_abono+=ficha.abono   
        saldo_total=sum_costo-sum_abono
        saldo_total_var.set(f"Saldo total: {saldo_total:.2f}")
        if saldo_total <= 0:
            saldo_label.configure(fg_color="#59C07A")  # Fondo verde
        else:
            saldo_label.configure(fg_color="#DD4151")     
        return saldo_total
    
    saldo_total=0
    # Etiqueta para el título
    saldo_total_var = customtkinter.StringVar(value=f"Saldo total: {saldo_total:.2f}")
    label = customtkinter.CTkLabel(fichas_window, text=f"Fichas Odontológicas de: {cliente.nombre}", font=("Arial", 16))
    label.pack(pady=10)
    saldo_label = customtkinter.CTkLabel(fichas_window, textvariable=saldo_total_var, font=("Arial", 16))
    saldo_label.pack(pady=10)
    calcular_saldo_total()
    # Frame para contener la tabla y el scrollbar
    frame = customtkinter.CTkFrame(fichas_window)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Tabla para mostrar las fichas
    tree_ficha_odonto = ttk.Treeview(
        frame,
        columns=("fecha", "tratamiento", "costo", "abono", "saldo"),
        show="headings",
        height=10
    )
    tree_ficha_odonto.heading("fecha", text="Fecha")
    tree_ficha_odonto.heading("tratamiento", text="Tratamiento")
    tree_ficha_odonto.heading("costo", text="Costo")
    tree_ficha_odonto.heading("abono", text="Abono")
    tree_ficha_odonto.heading("saldo", text="Saldo")
    tree_ficha_odonto.column("fecha", anchor="center", width=100)
    tree_ficha_odonto.column("tratamiento", anchor="w", width=200)
    tree_ficha_odonto.column("costo", anchor="center", width=80)
    tree_ficha_odonto.column("abono", anchor="center", width=80)
    tree_ficha_odonto.column("saldo", anchor="center", width=80)
    tree_ficha_odonto.pack(side="left", fill="both", expand=True)
    
    # Scrollbar vertical usando customtkinter
    scrollbar = customtkinter.CTkScrollbar(frame, orientation="vertical", command=tree_ficha_odonto.yview)
    scrollbar.pack(side="right", fill="y")
    tree_ficha_odonto.configure(yscrollcommand=scrollbar.set)
    # Configurar estilos para las filas
    tree_ficha_odonto.tag_configure("saldo_cero", background="#59C07A")  # Verde claro
    tree_ficha_odonto.tag_configure("saldo_no_cero", background="#DD4151")  # Rojo claro
    # Función para cargar datos en la tabla
    def cargar_datos():
        # Limpiar la tabla antes de cargar datos nuevos
        for row in tree_ficha_odonto.get_children():
            tree_ficha_odonto.delete(row)
        # Cargar datos de la base de datos
        
        fichas = FichaOdontologicaController.obtener_fichas_por_cliente(cliente_id)
        for ficha in fichas:
            tag = "saldo_cero" if (ficha.saldo <= 0 ) else "saldo_no_cero"
            tree_ficha_odonto.insert(
                "",
                "end",
                values=(ficha.fecha, ficha.tratamiento_realizado, ficha.costo, ficha.abono, ficha.saldo),
                iid=ficha.id, # Usar el ID de la ficha como identificador único
                tags=(tag,)  # Asignar etiqueta
            )

    # Llamar a la función para cargar datos
    cargar_datos()

    # Función para eliminar una ficha
    def eliminar_ficha():
        selected_item = tree_ficha_odonto.selection()  # Obtener el elemento seleccionado
        if selected_item:
            ficha_id = int(tree_ficha_odonto.selection()[0])  # Obtener el ID (iid) del elemento
            FichaOdontologicaController.eliminar_ficha(ficha_id)  # Eliminar ficha de la base de datos
            cargar_datos()  # Actualizar la tabla
            calcular_saldo_total()
    
    # Función para abrir ventana de edición
    def editar_ficha():
        selected_item = tree_ficha_odonto.selection()  # Obtener el elemento seleccionado
        if not selected_item:
            return  # No hacer nada si no hay selección
        ficha_id = int(selected_item[0])  # Obtener el ID (iid) del elemento
        ficha = FichaOdontologicaController.obtener_ficha_por_id(ficha_id)
        
        saldo_var_fichas = customtkinter.StringVar(value=f"{ficha.saldo:.2f}")
        
        def calcular_saldo():
            """Actualiza el campo de saldo calculando costo - abono."""
            try:
                costo = float(entries[2].get() or 0)
                abono = float(entries[3].get() or 0)
                saldo = costo - abono
                saldo_var_fichas.set(f"{saldo:.2f}")  # Actualizar el saldo
            except ValueError:
                saldo_var_fichas.set("0.00")
        if ficha:
            # Crear ventana para editar la ficha
            editar_window = customtkinter.CTkToplevel(fichas_window)
            editar_window.title("Editar Ficha Odontológica")
            editar_window.geometry("400x500")

            # Crear campos para editar
            labels = ["Fecha", "Tratamiento", "Costo", "Abono", "Saldo"]
            values = [
                ficha.fecha,
                ficha.tratamiento_realizado,
                ficha.costo,
                ficha.abono,
                ficha.saldo,
            ]
            entries = []

            for i, label_text in enumerate(labels):
                label = customtkinter.CTkLabel(editar_window, text=label_text)
                label.pack(pady=5)
                if i == 0:  # Campo de fecha con calendario
                    date_entry = DateEntry(editar_window, date_pattern="yyyy-mm-dd")
                    date_entry.pack(pady=5)
                    date_entry.set_date(values[i])
                    entries.append(date_entry)
                elif i==4:
                    entry = customtkinter.CTkEntry(editar_window, textvariable=saldo_var_fichas, state="disabled")
                    entry.pack(pady=5)
                    entry.insert(0, str(values[i]))
                    entries.append(entry)
                    
                else:
                    entry = customtkinter.CTkEntry(editar_window)
                    entry.pack(pady=5)
                    entry.insert(0, str(values[i]))
                    entries.append(entry)
            costo_entry = entries[2]
            abono_entry = entries[3]
            costo_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
            abono_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
            # Función para guardar cambios
            def guardar_cambios():
                nueva_fecha = entries[0].get_date().strftime("%Y-%m-%d")
                nuevo_tratamiento = entries[1].get()
                try:
                    nuevo_costo = float(entries[2].get() or 0)
                    nuevo_abono = float(entries[3].get() or 0)
                    nuevo_saldo = float(entries[4].get() or 0)
                except ValueError:
                    showwarning("Error de entrada", "Por favor, asegúrate de que 'Costo' y 'Abono' sean números válidos.", parent=fichas_window)
                    return

                FichaOdontologicaController.actualizar_ficha(
                    ficha_id=ficha_id,
                    fecha=nueva_fecha,
                    tratamiento_realizado=nuevo_tratamiento,
                    costo=nuevo_costo,
                    abono=nuevo_abono,
                    saldo=nuevo_saldo
                )
                cargar_datos()  # Actualizar la tabla
                calcular_saldo_total()
                editar_window.destroy()

            guardar_button = customtkinter.CTkButton(editar_window, text="Guardar", command=guardar_cambios)
            guardar_button.pack(pady=10)

            cancelar_button = customtkinter.CTkButton(editar_window, text="Cancelar", command=editar_window.destroy)
            cancelar_button.pack(pady=10)

    # Función para agregar una nueva ficha
    def agregar_ficha():
    
        fecha = date_entry.get_date().strftime("%Y-%m-%d")
        tratamiento = entries[1].get()
        try:
            costo = float(entries[2].get() or 0)
            abono = float(entries[3].get() or 0)
            saldo = float(entries[4].get() or 0)
        except ValueError:
            showwarning("Error de entrada", "Por favor, asegúrate de que 'Costo' y 'Abono' sean números válidos.", parent=fichas_window)
            return
        
        # Lógica para agregar ficha a la base de datos
        FichaOdontologicaController.crear_ficha(
            cliente_id=cliente_id,
            fecha=fecha,
            tratamiento_realizado=tratamiento,
            costo=costo,
            abono=abono,
            saldo=saldo
        )

        # Actualizar tabla
        cargar_datos()
        calcular_saldo_total()
        for entry in entries[1:]:  # Limpiar los campos (excepto la fecha)
            entry.delete(0, "end")
        date_entry.set_date(datetime.now())  # Restablecer la fecha a hoy
        saldo_var_fichas.set("0.00")
        
    def calcular_saldo():
        """Actualiza el campo de saldo calculando costo - abono."""
        try:
            costo = float(costo_entry.get() or 0)
            abono = float(abono_entry.get() or 0)
            saldo = costo - abono
            saldo_var_fichas.set(f"{saldo:.2f}")  # Actualizar el valor del saldo
        except ValueError:
            saldo_var_fichas.set("0.00")
    # Crear botones para eliminar y editar fichas
    botones_frame = customtkinter.CTkFrame(fichas_window)
    botones_frame.pack(pady=10)

    eliminar_button = customtkinter.CTkButton(botones_frame, text="Eliminar", command=eliminar_ficha, fg_color="#F24236")
    eliminar_button.grid(row=0, column=0, padx=10)

    editar_button = customtkinter.CTkButton(botones_frame, text="Editar", command=editar_ficha)
    editar_button.grid(row=0, column=1, padx=10)
    # Crear campos para agregar nueva ficha
    form_frame_odntologia = customtkinter.CTkFrame(fichas_window)
    form_frame_odntologia.pack(pady=10)

    labels = ["Fecha", "Tratamiento", "Costo", "Abono", "Saldo"]
    entries = []
    saldo_var_fichas = customtkinter.StringVar(value="0.00")
    for i, label_text in enumerate(labels):
        label = customtkinter.CTkLabel(form_frame_odntologia, text=label_text)
        label.grid(row=0, column=i, padx=5)
        if i == 0:  # Campo de fecha con calendario
            date_entry = DateEntry(form_frame_odntologia, date_pattern="yyyy-mm-dd")
            date_entry.grid(row=1, column=i, padx=5)
            date_entry.set_date(datetime.now())
            entries.append(date_entry)
        elif i==4:
            entry = customtkinter.CTkEntry(form_frame_odntologia, textvariable=saldo_var_fichas, state="disabled")
            entry.grid(row=1, column=i, padx=5)
            entries.append(entry)
            
        else:
            entry = customtkinter.CTkEntry(form_frame_odntologia)
            entry.grid(row=1, column=i, padx=5)
            entries.append(entry)
    costo_entry = entries[2]
    abono_entry = entries[3]

    costo_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
    abono_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
    # Botón para agregar ficha
    add_button = customtkinter.CTkButton(fichas_window, text="Agregar Ficha", command=agregar_ficha)
    add_button.pack(pady=10)
    # Botón para cerrar
    close_button = customtkinter.CTkButton(fichas_window, text="Cerrar", command=fichas_window.destroy)
    close_button.pack(pady=10)