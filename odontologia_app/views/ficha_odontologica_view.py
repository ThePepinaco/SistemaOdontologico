from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo
import customtkinter
from controllers.cliente_controller import ClienteController
from controllers.ficha_odontologica_controller import FichaOdontologicaController
from controllers.odontograma_controller import OdontogramaController
from datetime import datetime
from tkcalendar import DateEntry

def view_fichas_odontologicas(self, cliente_id):
    # Crear ventana para fichas odontológicas
    fichas_window_main = customtkinter.CTkToplevel(self)
    cliente = ClienteController.obtener_cliente_por_id(cliente_id)
    fichas_window_main.title(f"Fichas odontológicas de {cliente.nombre}")
    fichas_window_main.geometry("1130x600")
    fichas_window_main.minsize(1130,500)
    fichas_window_main.attributes('-topmost', True)
    fichas_window_main.after(100, lambda: fichas_window_main.attributes('-topmost', False))
    
    large_font = ("Arial", 18, "bold")
    medium_font = ("Arial", 16)
    small_font = ("Arial", 12)
    
    tabs = customtkinter.CTkTabview(fichas_window_main, width=900, height=650)
    tabs.pack(padx=10, pady=10, fill="both", expand=True)
    tabs._segmented_button.configure(font=medium_font)
    fichas_window = tabs.add("Fichas Odontológicas")
    def calcular_saldo_total():
        saldo_total=0
        sum_costo=0
        sum_abono=0
        fichas = FichaOdontologicaController.obtener_fichas_por_cliente(cliente_id)
        for ficha in fichas:
            sum_costo+=ficha.costo
            sum_abono+=ficha.abono   
        saldo_total=sum_abono-sum_costo
        saldo_total_var.set(f"Saldo total: {saldo_total:.2f}")
        if saldo_total >= 0:
            saldo_label.configure(fg_color="#59C07A")  # Fondo verde
        else:
            saldo_label.configure(fg_color="#DD4151")     
        return saldo_total
    
    saldo_total=0
    # Etiqueta para el título
    saldo_total_var = customtkinter.StringVar(value=f"Saldo total: {saldo_total:.2f}")
    label = customtkinter.CTkLabel(fichas_window, text=f"Fichas Odontológicas de: {cliente.nombre}", font=medium_font)
    label.pack(pady=10)
    saldo_label = customtkinter.CTkLabel(fichas_window, textvariable=saldo_total_var, font=("Arial", 16))
    saldo_label.pack(pady=10)
    
    
    container_ficha_odo = customtkinter.CTkFrame(fichas_window)
    container_ficha_odo.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Configuración del grid en el contenedor
    container_ficha_odo.grid_rowconfigure(0, weight=1)  # Frame desplazable ocupa espacio ajustable
    container_ficha_odo.grid_rowconfigure(1, weight=0)  # Espacio fijo para el botón
    container_ficha_odo.grid_columnconfigure(0, weight=1)  # Ajusta el ancho dinámicamente
    calcular_saldo_total()
    # Frame para contener la tabla y el scrollbar
    frame = customtkinter.CTkFrame(container_ficha_odo)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    #frame.pack(fill="both", expand=True, padx=10, pady=10)

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
    tree_ficha_odonto.column("fecha", anchor="center", width=115, stretch="no")
    tree_ficha_odonto.column("tratamiento", anchor="w", width=200)
    tree_ficha_odonto.column("costo", anchor="center", width=110, stretch="no")
    tree_ficha_odonto.column("abono", anchor="center", width=110, stretch="no")
    tree_ficha_odonto.column("saldo", anchor="center", width=110, stretch="no")
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
            tag = "saldo_cero" if (ficha.saldo >= 0 ) else "saldo_no_cero"
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
                saldo = abono - costo
                saldo_var_fichas.set(f"{saldo:.2f}")  # Actualizar el saldo
            except ValueError:
                saldo_var_fichas.set("0.00")
        if ficha:
            # Crear ventana para editar la ficha
            editar_window = customtkinter.CTkToplevel(fichas_window)
            editar_window.title("Editar Ficha Odontológica")
            editar_window.geometry("300x500")
            editar_window.minsize(300,500)
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
                label = customtkinter.CTkLabel(editar_window, text=label_text, font=medium_font)
                label.pack(pady=5)
                if i == 0:  # Campo de fecha con calendario
                    date_entry = DateEntry(editar_window, date_pattern="yyyy-mm-dd", font=small_font)
                    date_entry.pack(pady=5)
                    date_entry.set_date(values[i])
                    entries.append(date_entry)
                elif i==4:
                    entry = customtkinter.CTkEntry(editar_window, textvariable=saldo_var_fichas, state="disabled", font=medium_font)
                    entry.pack(pady=5)
                    entry.insert(0, str(values[i]))
                    entries.append(entry)
                    
                else:
                    entry = customtkinter.CTkEntry(editar_window, font=medium_font)
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

            guardar_button = customtkinter.CTkButton(editar_window, text="Guardar", command=guardar_cambios, font=medium_font)
            guardar_button.pack(pady=10)

            cancelar_button = customtkinter.CTkButton(editar_window, text="Cancelar", command=editar_window.destroy, font=medium_font)
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
            saldo = abono - costo
            saldo_var_fichas.set(f"{saldo:.2f}")  # Actualizar el valor del saldo
        except ValueError:
            saldo_var_fichas.set("0.00")
    # Crear botones para eliminar y editar fichas
    botones_frame = customtkinter.CTkFrame(container_ficha_odo)
    botones_frame.grid(row=1, column=0, sticky="", padx=10, pady=10)

    eliminar_button = customtkinter.CTkButton(botones_frame, text="Eliminar", command=eliminar_ficha, fg_color="#F24236", font=medium_font)
    eliminar_button.grid(row=0, column=0, padx=10)

    editar_button = customtkinter.CTkButton(botones_frame, text="Editar", command=editar_ficha, font=medium_font)
    editar_button.grid(row=0, column=1, padx=10)
    # Crear campos para agregar nueva ficha
    form_frame_odntologia = customtkinter.CTkFrame(container_ficha_odo)
    form_frame_odntologia.grid(row=2, column=0, sticky="", padx=10, pady=10)

    labels = ["Fecha", "Tratamiento", "Costo", "Abono", "Saldo"]
    entries = []
    saldo_var_fichas = customtkinter.StringVar(value="0.00")
    for i, label_text in enumerate(labels):
        label = customtkinter.CTkLabel(form_frame_odntologia, text=label_text, font=medium_font)
        label.grid(row=0, column=i, padx=5)
        if i == 0:  # Campo de fecha con calendario
            date_entry = DateEntry(form_frame_odntologia, date_pattern="yyyy-mm-dd", font=small_font)
            date_entry.grid(row=1, column=i, padx=5)
            date_entry.set_date(datetime.now())
            entries.append(date_entry)
        elif i==4:
            entry = customtkinter.CTkEntry(form_frame_odntologia, textvariable=saldo_var_fichas, state="disabled", font=medium_font)
            entry.grid(row=1, column=i, padx=5)
            entries.append(entry)
            
        else:
            entry = customtkinter.CTkEntry(form_frame_odntologia, font=medium_font)
            entry.grid(row=1, column=i, padx=5)
            entries.append(entry)
    costo_entry = entries[2]
    abono_entry = entries[3]

    costo_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
    abono_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
    # Botón para agregar ficha
    add_button = customtkinter.CTkButton(container_ficha_odo, text="Agregar Ficha", command=agregar_ficha, font=medium_font)
    add_button.grid(row=3, column=0, sticky="", padx=10, pady=10)
    # Botón para cerrar
    close_button = customtkinter.CTkButton(container_ficha_odo, text="Cerrar", command=fichas_window.destroy, font=medium_font)
    close_button.grid(row=4, column=0, sticky="", padx=10, pady=10)
    
    
    # Función para cambiar el color al hacer clic en un cuadro
    def cambiar_color(event):
        color = color_seleccionado.get()
        cuadro_id = event.widget.find_closest(event.x, event.y)[0]  # Obtener el id del cuadro
        canvas.itemconfig(cuadro_id, fill=color)  # Cambiar el color en el canvas

        # Guardar el color en la base de datos
        OdontogramaController.agregar_o_actualizar(cliente_id, cuadro_id, color)

    # Crear la pestaña de odontograma
    # Agregar la pestaña "Odontograma"
    tab_odontograma = tabs.add("Odontograma")
    # Variable para guardar el color seleccionado
    color_seleccionado = customtkinter.StringVar(value="white")

    # Crear un Frame para alinear los Radiobuttons en una fila
    frame_radiobuttons = customtkinter.CTkFrame(tab_odontograma)
    frame_radiobuttons.pack(pady=10)
    
    customtkinter.CTkRadioButton(frame_radiobuttons, text="Sano", variable=color_seleccionado, value="white").pack(side='left')
    customtkinter.CTkRadioButton(frame_radiobuttons, text="Carie", variable=color_seleccionado, value="red").pack(side='left')
    customtkinter.CTkRadioButton(frame_radiobuttons, text="Verde", variable=color_seleccionado, value="green").pack(side='left')
    customtkinter.CTkRadioButton(frame_radiobuttons, text="Azul", variable=color_seleccionado, value="blue").pack(side='left')
    customtkinter.CTkRadioButton(frame_radiobuttons, text="Amarillo", variable=color_seleccionado, value="yellow").pack(side='left')

    canvas = customtkinter.CTkCanvas(tab_odontograma, width=1300, height=400, bg="white")  # Ajusta el tamaño del canvas
    canvas.pack(pady=20)

    # Crear cuadros en posiciones específicas
    rectangulos = []

    def crear_fila(x_inicial, y, cantidad, ancho, alto, separacion, numero_ini, numero_fin):
        if numero_ini != 0:
            canvas.create_text(x_inicial - 20 - ancho, y, text=str(numero_ini), font=medium_font, anchor="center")
        for i in range(cantidad):
            # Crear el cuadro central
            x = x_inicial + i * (ancho + separacion)
            rect = canvas.create_oval(x - ancho//2, y - alto//2, x + ancho//2, y + alto//2, fill="white", outline="black") 
            rectangulos.append(rect)
            canvas.tag_bind(rect, "<Button-1>", cambiar_color)
            # Crear el cuadro adicional a la izquierda
            x_izq = x - (ancho)
            rect_izq = canvas.create_oval(x_izq - ancho//5, y - alto//2, x_izq + ancho//2, y + alto//2, fill="white", outline="black") 
            rectangulos.append(rect_izq)
            canvas.tag_bind(rect_izq, "<Button-1>", cambiar_color)
            # Crear el cuadro adicional a la derecha
            x_der = x + (ancho)
            rect_der = canvas.create_oval(x_der - ancho//2, y - alto//2, x_der + ancho//5, y + alto//2, fill="white", outline="black") 
            rectangulos.append(rect_der)
            canvas.tag_bind(rect_der, "<Button-1>", cambiar_color)
            # Crear el cuadro adicional arriba
            y_arr = y + (alto)
            rect_arr = canvas.create_oval(x - ancho//2, y_arr - alto//2, x + ancho//2, y_arr + alto//5, fill="white", outline="black") 
            rectangulos.append(rect_arr)
            canvas.tag_bind(rect_arr, "<Button-1>", cambiar_color)
            # Crear el cuadro adicional abajo
            y_aba = y - (alto)
            rect_aba = canvas.create_oval(x - ancho//2, y_aba - alto//5, x + ancho//2, y_aba + alto//2, fill="white", outline="black") 
            rectangulos.append(rect_aba)
            canvas.tag_bind(rect_aba, "<Button-1>", cambiar_color)
        # Crear el número al final de la fila (si no es 0)
        if numero_fin != 0:
            x_final = x_inicial + (cantidad - 1) * (ancho + separacion)
            canvas.create_text(x_final + ancho + 20, y, text=str(numero_fin), font=medium_font, anchor="center")
    # Crear filas según la distribución indicada
    crear_fila(75, 100, 8, 20, 20, 36, 1, 0 )   # Primera mitad fila 1
    crear_fila(625, 100, 8, 20, 20, 36, 0, 2)  # Segunda mitad fila 1
    
    crear_fila(245, 175, 5, 20, 20, 36, 5, 0)  # Primera mitad fila 3
    crear_fila(625, 175, 5, 20, 20, 36, 0, 6)  # Segunda mitad fila 3
    
    crear_fila(245, 250, 5, 20, 20, 36, 8, 0)  # Primera mitad fila 4
    crear_fila(625, 250, 5, 20, 20, 36, 0, 7)  # Segunda mitad fila 4
    
    crear_fila(75, 325, 8, 20, 20, 36, 4, 0)   # Primera mitad fila 2
    crear_fila(625, 325, 8, 20, 20, 36, 0, 3)  # Segunda mitad fila 2
    def cargar_colores_en_canvas(cliente_id):
        # Obtener los colores desde la base de datos
        colores_cliente = OdontogramaController.obtener_por_cliente(cliente_id)
        for odontograma in colores_cliente:
            cuadro_id = odontograma.cuadro_id
            color = odontograma.color
            # Establecer el color de cada cuadro en el canvas
            # Encuentra el cuadro correspondiente en el canvas por cuadro_id y actualiza su color
            canvas.itemconfig(cuadro_id, fill=color)

    # Cuando se abre la ventana, cargamos los colores del cliente:
    # Este es el ID del cliente actual, debe ser dinámico
    cargar_colores_en_canvas(cliente_id)