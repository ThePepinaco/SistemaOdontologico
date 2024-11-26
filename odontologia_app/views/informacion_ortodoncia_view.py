from tkinter import font as tkFont
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo
import customtkinter
from controllers.cliente_controller import ClienteController
from controllers.informacion_ortodoncia_controller import InformacionOrtodonciaController
from controllers.tabla_ortodoncia_controller import TablaOrtodonciaController
from controllers.ficha_ortodoncia_controller import FichaOrtodonciaController
from datetime import datetime
from tkcalendar import DateEntry

def view_otros_registros(self, cliente_id):
    
    # Crear ventana para otros registros
    registros_window = customtkinter.CTkToplevel(self)
    cliente = ClienteController.obtener_cliente_por_id(cliente_id)
    registros_window.title(f"Ortodoncia de {cliente.nombre}")
    registros_window.geometry("1450x750")
    registros_window.attributes('-topmost', True)
    registros_window.after(100, lambda: registros_window.attributes('-topmost', False))
    # Crear los tabs
    tabs = customtkinter.CTkTabview(registros_window, width=900, height=650)
    tabs.pack(padx=10, pady=10, fill="both", expand=True)

    # Tab de Información Ortodoncia
    tab_informacion = tabs.add("Información Ortodoncia")

    # Obtener información de ortodoncia existente
    informacion = InformacionOrtodonciaController.obtener_por_cliente(cliente_id)

    # Función auxiliar para crear filas de entradas
    def create_row(frame, labels_entries, start_row):
        """Crea una fila con etiquetas y campos de entrada."""
        for col, (label_text, var_name) in enumerate(labels_entries):
            if var_name != "":
                label = customtkinter.CTkLabel(frame, text=label_text)
                label.grid(row=start_row, column=col * 2, padx=5, pady=5, sticky="w")

                entry = customtkinter.CTkEntry(frame)
                entry.grid(row=start_row, column=col * 2 + 1, padx=5, pady=5, sticky="ew")

                # Rellenar automáticamente si existe información
                if informacion and var_name in informacion.__dict__:
                    value = informacion.__dict__[var_name]
                    if value is not None:
                        entry.insert(0, str(value))

                entries[var_name] = entry
            else:
                label = customtkinter.CTkLabel(frame, text=label_text)
                label.grid(row=start_row, column=col * 2, padx=5, pady=5, sticky="w")

    # Marco para las entradas de Información Ortodoncia
    entries = {}  # Almacenar referencias a los campos de entrada
    info_frame = customtkinter.CTkFrame(tab_informacion)
    info_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Distribuir los campos en filas lógicas
    create_row(info_frame, [("Hábitos", "habitos"),
                            ("Medicamentos", "medicamentos"),
                            ("Respiración", "respiracion"),
                            ("Frenillo Labial", "frenillo_labial")
                            ], 0)

    create_row(info_frame, [("Tercio Aumentado", "tercio_aumentado"),
                            ("Cierre Labial", "cierre_labial"),
                            ("Posición Lengua", "posicion_lengua")
                            ], 1)

    create_row(info_frame, [("Estudios Modelos:", "")], 2)

    create_row(info_frame, [("Compresión", "em_compresion"),
                            ("Expansión", "em_expansion"),
                            ("Normal", "em_normal")
                            ], 3)

    create_row(info_frame, [("Sentido Sagital: Maxilar superior", ""),
                            ("", ""),
                            ("Sentido Sagital: Maxilar inferior", "")
                            ], 4)

    create_row(info_frame, [("Prostusión-Retrusión Incisivo", "ss_ms_pr_incisivo"),
                            ("", ""),
                            ("Prostusión-Retrusión Incisivo", "ss_mi_pr_incisivo")
                            ], 5)

    create_row(info_frame, [("Migración de", "migragacion"),
                            ("Piezas Ausentes por Extracción", "piezas_auesentes_extraccion"),
                            ("No Erupción", "no_erupcion")
                            ], 6)

    create_row(info_frame, [("Sentido Vertical: Maxilar superior", "")], 7)

    create_row(info_frame, [("Piezas Intruidas", "sv_ms_piezas_intruidas"),
                            ("Piezas Extruidas", "sv_ms_piezas_extruidas"),
                            ("Piezas Sumergidas", "sv_ms_piezas_sumergidas")
                            ], 8)

    create_row(info_frame, [("Sentido Vertical: Maxilar inferior", "")], 9)

    create_row(info_frame, [("Piezas Intruidas", "sv_mi_piezas_intruidas"),
                            ("Piezas Extruidas", "sv_mi_piezas_extruidas"),
                            ("Piezas Sumergidas", "sv_mi_piezas_sumergidas")
                            ], 10)

    create_row(info_frame, [("Terceros Molares Superior", "terceros_molares_superior"),
                            ("Terceros Molares Inferior", "terceros_molares_inferior")
                            ], 11)

    create_row(info_frame, [("Oclusión: Mordida Abierta", "oclusion_mordida_abierta"),
                            ("Mordida Profunda", "oclusion_mordida_profunda"),
                            ("Mordida Normal", "oclusion_mordida_normal")
                            ], 12)

    create_row(info_frame, [("Resalte u Overejet", "resalte_overejet"),
                            ("Overvite o Escalón", "overvite_escalon"),
                            ("Línea Media Central", "linea_media_central")
                            ], 13)

    create_row(info_frame, [("Laterales Derecha RM", "laterales_derecha_rm"),
                            ("Laterales Derecha RC", "laterales_derecha_rc"),
                            ("Laterales Derecha Cruzada", "laterales_derecha_cruzada"),
                            ("Laterales Derecha Vis a Vis", "laterales_derecha_vis_a_vis")
                            ], 14)

    create_row(info_frame, [("Laterales Izquierda RM", "laterales_izquierda_rm"),
                            ("Laterales Izquierda RC", "laterales_izquierda_rc"),
                            ("Laterales Izquierda Cruzada", "laterales_izquierda_cruzada"),
                            ("Laterales Izquierda Vis a Vis", "laterales_izquierda_vis_a_vis")
                            ], 15)

    # Botones para guardar o cancelar
    button_frame = customtkinter.CTkFrame(tab_informacion)
    button_frame.pack(pady=10)

    def guardar_informacion():
        # Recolectar datos de los campos
        #print(entries.items())
        data = {key: entry.get() for key, entry in entries.items()}
        InformacionOrtodonciaController.guardar_o_actualizar(cliente_id, **data)
        showinfo("Éxito", "Información Ortodoncia guardada correctamente.", parent=registros_window)

    guardar_button = customtkinter.CTkButton(button_frame, text="Guardar", command=guardar_informacion)
    guardar_button.pack(side="left", padx=10)

    cancelar_button = customtkinter.CTkButton(button_frame, text="Cancelar", command=registros_window.destroy)
    cancelar_button.pack(side="right", padx=10)
    

    tab_tabla = tabs.add("Tabla Ortodoncia")

    # Frame para contener la tabla y el scrollbar
    frame = customtkinter.CTkFrame(tab_tabla)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    s= ttk.Style() 
    s.configure('ortodoncia.Treeview', rowheight=45)
    # Crear tabla para la ortodoncia
    tree = ttk.Treeview(
        frame,
        columns=("campo", "norma", "desviacion", "valor", "informacion"),
        show="headings",
        style="ortodoncia.Treeview"
    )
    witdh_info=450
    witdh_valor=140
    tree.heading("campo", text="RICKETTS")
    tree.heading("norma", text="NORMA")
    tree.heading("desviacion", text="DESV/S")
    tree.heading("valor", text="VALOR ")
    tree.heading("informacion", text="INTERPRETACIÓN")

    tree.column("campo", anchor="w", width=200)
    tree.column("norma", anchor="center", width=50)
    tree.column("desviacion", anchor="center", width=30)
    tree.column("valor", anchor="center", width=witdh_valor)
    tree.column("informacion", anchor="w", width=witdh_info)
    tree.pack(side="left", fill="both", expand=True)

    # Scrollbar vertical usando customtkinter
    scrollbar = customtkinter.CTkScrollbar(frame, orientation="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    # Diccionario para almacenar los valores modificados temporalmente
    valores_modificados = {}

    # Datos predefinidos para cada campo
    datos_ortodoncia = [
        ("Relación Molar", "-1.6", "-0.7", "relacion_molar", "Valor -6mm CLASEIII, VALOR+6 CLASE II MOLAR"),
        ("Overejet (mm)", "3.4", "2.5", "overejet", ">:sobremor horiz < mordida cruzada ant.o clase III"),
        ("Overbite (mm)", "2.8", "2.0", "overbite", ">:sobremordida vertical < mordida abierta anterior"),
        ("Mandibular Incisivo Extrusión (mm)", "2.4", "2.0", "mandibular_incisivo_extrusion", ">sobreerupcion dec inc.inferior, curva de spee severe< curva de spee aplanada (infra erupcion del inc. inf)"),
        ("Interincisal Ángulo (U1-L1) (°)", "124", "6", "interincisal_angulo", ">retroinclinacion puede relacionars con mordida profu < proclinacion de incisivos superiores e inferiores"),
        ("U Incisivo Protusión (U1-APo) (mm)", "6.7", "2.3", "u_incisivo_protusion", "Relación indica la posicion del incisivo superior en relacion al perfil de 1/3 inferior de la cara."),
        ("L1 Protusión (U1-APo) (mm)", "3.6", "2.3", "l1_protusion", "Indica la ubicación de los incisivos inferiores con respecto al plano maxilomandibular, prostusión de la arc. inferior"),
        ("U Incisivo Inclinación(U1-APo) (°)", "28.0", "4.0", "u_incisivo_inclinacio", ">indica proclinacion del incisivo superior. <retroinclinacion del incisivo superior "),
        ("L1-A-PO (°)", "27.7", "4.0", "l1_a_po", ">Proclinacion del inc. inf (clase III) ver por compensaci < retro inclinación del inc.inf Clase II ver compensación"),
        ("OCCL PLANO-FH (°)", "7.5", "5.0", "occl_plano_fh", ">mordida abierta < mordida profunda (Downs)"),
        ("U6 PT Vertical (mm)", "21 Masculino - 18 Femenino", "+-3mm", "u6_pt_vertical", "Determina si la maloclusion es causada por la posición del primer molar superior"),
        ("Convexidad (A-NPo) (mm)", "2.8", "2.0", "convexidad", ">perfil convexo .clase II esqueletal <perfil cóncavo .clase II esqueletal"),
        ("Arco Mandíbula (°)", "34.7", "4.0", "arco_mandibula", ">rotac del mentón hacia arriba y delante (rama larga) < rotación del mentón habia abajo y atrás (rama corta)"),
        ("FMA (MP-FH) (°)", "22.9", "4.5", "fma", ">crecimiento mandibular hiperdivergente < crecimiento mandibular hipordivergente (Tweed)"),
        ("Depth Maxilar (FH-NA)(°) Profundidad", "93.4", "3.0", "depth_maxilar", ">mayor indica un maxilar protusivo < menor indica un maxiliar retruido "),
        ("Facial Axis Eje Ricketts (NABa-PtGN) (°)", "89.2 o", "3.5", "facial_axis_eje_rickets", ">de 6 a 10 favorable de 10 a 12 mordi.cerrada con tendecia a dim.vertical corta, mentón protrusivo < cara larga con retroposicion de menton"),
        ("Ángulo/Profundidad Facial (FH-NPo) (°)", "91.6", "3.0", "angulo_profundidad_facial", ">mand avanzada determi clase III (ver base craneal)<mandibul deficient en sent.Ant.post. clase II esq"),
        ("Facial Taper Na-Gn-Go (°) CONO", "68.5", "3.5", "facial_taper_na_gn_go", ">CLASE III relaciona dirección de crecimiento con mand < caras largas y clase II determina situaciones estetucas"),
        ("Localización Porion (mm)", "-37.0", "2.2", "lozalizacion_porion", "Val menores indica crecimiento en clase III esqueletíca. Val mayores un porion por detrás clase II esquelética"),
        ("Craneal Deflección (°)", "29.6", "3.0", "craneal_defleccion", ">ind base craneal con patrón de crec. Horizontal braquic < base craneal plana con patron vertical es dolicocefalico"),
        ("Rama Posición (°)", "77.5", "3.0", "rama_posicion", ">ubicac anterior de la rama, puede manifest en claseIII < ubicacion posterior de la rama, puede manif en clase III"),
        ("Lower Face Height (ANS-Xi-Pm) (°) Altura", "44.5", "4.0", "lower_face_height", ">valores altos indica mordida abierta esquelética < valores bajos mordidas profundas"),
        ("Lower Lip-Plano E (mm)", "-2.0", "2.0", "lower_lip_plano_e", "Se analiza el labio y el perfil línea E (posición de in sup)"),
        ("Resumen", "", "", "resumen", ""),
    ]
    tree.tag_configure("gray", background="#363a3b")  #  gray
    tree.tag_configure("darkgray", background="#2a2d2e")  #  darkray
    # Cargar datos en la tabla
    def wrap_text(text, max_width, font=("Arial", 14)):
        """Divide el texto en líneas para ajustarlo al ancho máximo dado."""
        from tkinter import font as tkFont

        # Crear una fuente para medir texto
        test_font = tkFont.Font(family=font[0], size=font[1])

        words = text.split()  # Dividir el texto en palabras
        wrapped_lines = []
        current_line = ""

        for word in words:
            # Comprobar si añadir otra palabra excede el ancho máximo
            if test_font.measure(current_line + " " + word) > max_width:
                wrapped_lines.append(current_line.strip())  # Añadir línea completa
                current_line = word  # Comenzar una nueva línea
            else:
                current_line += " " + word  # Añadir palabra a la línea actual

        # Añadir la última línea
        if current_line:
            wrapped_lines.append(current_line.strip())

        return "\n".join(wrapped_lines) 
    
    def ajustar_altura_filas(tree, texto, font=("Arial", 14), max_width=witdh_info):
        """Ajusta la altura de todas las filas según el contenido más largo."""
        
        test_font = tkFont.Font(family=font[0], size=font[1])
        max_lines = 1  # Contador para líneas más largas

        for row in texto:
            # Dividir el texto en líneas basándose en max_width
            wrapped_lines = wrap_text(row, max_width, font=font).split("\n")
            if len(wrapped_lines) > max_lines:
                max_lines = len(wrapped_lines)  # Obtener el máximo de líneas

        # Calcular nueva altura en píxeles (15px por línea es aproximado)
        nueva_altura = max_lines * test_font.metrics("linespace")

        # Aplicar al estilo de Treeview
        style = ttk.Style()
        style.configure("ortodoncia.Treeview", rowheight=nueva_altura)
        
    def cargar_datos():
        """Carga los datos de la tabla ortodoncia desde la base de datos."""
        for row in tree.get_children():
            tree.delete(row)
        texto = [str(informacion) for _, _, _, _, informacion in datos_ortodoncia]

    # Ajustar altura de las filas en base al contenido
        ajustar_altura_filas(tree, texto)
        registros = TablaOrtodonciaController.obtener_por_cliente(cliente_id)
        start=2
        for campo, norma, desviacion, atributo, informacion in datos_ortodoncia:
            modulo=start%2
            start+=1
            tag = "gray" if modulo == 0 else "darkgray"
            informacion_envuelta = wrap_text(str(informacion), max_width=witdh_info*1.5)
            
            valor_actual =""
            if registros and atributo in registros.__dict__:
                    value = registros.__dict__[atributo]
                    if value is not None:
                        valor_actual = value
                    else:
                        valor_actual = ""
            valor_actual = wrap_text(str(valor_actual), max_width=witdh_valor*3)
            tree.insert(
                "",
                "end",
                values=(campo, norma, desviacion, valor_actual, informacion_envuelta),
                iid=atributo,  # Identificador único basado en el atributo
                tags=(tag,)
            )

    cargar_datos()
    entrada_activa = None

    # Función para editar directamente en la columna "valor"
    def iniciar_edicion(event):
        """Inicia la edición de la celda seleccionada en 'valor'."""
        global entrada_activa

        item = tree.selection()
        if not item:
            return

        item_id = item[0]
        column = tree.identify_column(event.x)  # Identifica la columna por el clic
        if column != "#4":  # Permitir edición solo en la columna 4 (valor)
            return

        bbox = tree.bbox(item_id, column)
        if not bbox:
            return

        x, y, width, height = bbox
        entrada_activa = ttk.Entry(tree)
        entrada_activa.place(x=x, y=y, width=width, height=height)
        entrada_activa.focus()

        def guardar_edicion(event):
            global entrada_activa
            nuevo_valor = entrada_activa.get()
            try:
                if item_id == "resumen":
                    # Permitir texto libre para el campo "resumen"
                    valores_modificados[item_id] = nuevo_valor if nuevo_valor else None
                else:
                    # Intentar convertir a número
                    valores_modificados[item_id] = float(nuevo_valor) if nuevo_valor else None

                # Actualizar el valor en la tabla
                tree.set(item_id, column, nuevo_valor)

            except ValueError:
                # Mostrar cuadro de diálogo en caso de error
                showwarning("Error de Valor", f"El valor ingresado para {tree.item(item_id, 'values')[0]} debe ser un número.", parent=registros_window)

            finally:
                # Eliminar el campo de entrada
                entrada_activa.destroy()
                entrada_activa = None

        entrada_activa.bind("<Return>", guardar_edicion)
        entrada_activa.bind("<FocusOut>", guardar_edicion)

    tree.bind("<Double-1>", iniciar_edicion)


    # Función para guardar cambios
    def guardar_cambios():
        """Guardar los valores modificados en la base de datos."""
        global entrada_activa

        # Forzar cierre de cualquier edición activa
        if entrada_activa is not None:
            entrada_activa.event_generate("<Return>")  # Simular que el usuario presiona Enter

        if not valores_modificados:
            showinfo("Información", "No hay cambios para guardar.", parent=registros_window)
            return

        TablaOrtodonciaController.actualizar_campos(cliente_id=cliente_id, valores=valores_modificados)

        showinfo("Éxito", "Todos los cambios han sido guardados.", parent=registros_window)
        cargar_datos()  # Recargar la tabla
        valores_modificados.clear()

    # Botón para guardar todos los cambios
    guardar_button = customtkinter.CTkButton(
        tab_tabla,
        text="Guardar Cambios",
        command=guardar_cambios
    )
    guardar_button.pack(pady=10)

    tab_ficha = tabs.add("Fichas Ortodoncia")
    label = customtkinter.CTkLabel(tab_ficha, text="Fichas Odontológicas", font=("Arial", 16))
    label.pack(pady=10)

    # Frame para contener la tabla y el scrollbar
    frame = customtkinter.CTkFrame(tab_ficha)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    def calcular_saldo_total():
        saldo_total=0
        sum_costo=0
        sum_abono=0
        fichas = FichaOrtodonciaController.obtener_fichas_por_cliente(cliente_id)
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
    saldo_total_var = customtkinter.StringVar(value=f"Saldo total: {saldo_total:.2f}")
    saldo_label = customtkinter.CTkLabel(frame, textvariable=saldo_total_var, font=("Arial", 16))
    saldo_label.pack(pady=10)
    calcular_saldo_total()
    # Tabla para mostrar las fichas
    tree2 = ttk.Treeview(
        frame,
        columns=("fecha","brack", "actividad", "costo", "abono", "saldo"),
        show="headings",
        height=10
    )
    tree2.heading("fecha", text="Fecha")
    tree2.heading("actividad", text="Actividad")
    tree2.heading("brack", text="Brack")
    tree2.heading("costo", text="Costo")
    tree2.heading("abono", text="Abono")
    tree2.heading("saldo", text="Saldo")
    tree2.column("fecha", anchor="center", width=100)
    tree2.column("actividad", anchor="w", width=200)
    tree2.column("brack", anchor="center", width=80)
    tree2.column("costo", anchor="center", width=80)
    tree2.column("abono", anchor="center", width=80)
    tree2.column("saldo", anchor="center", width=80)
    tree2.pack(side="left", fill="both", expand=True)

    # Scrollbar vertical usando customtkinter
    scrollbar = customtkinter.CTkScrollbar(frame, orientation="vertical", command=tree2.yview)
    scrollbar.pack(side="right", fill="y")
    tree2.configure(yscrollcommand=scrollbar.set)
    tree2.tag_configure("saldo_cero", background="#59C07A")  # Verde claro
    tree2.tag_configure("saldo_no_cero", background="#DD4151")  # Rojo claro
    # Función para cargar datos en la tabla
    def cargar_datos():
        # Limpiar la tabla antes de cargar datos nuevos
        for row in tree2.get_children():
            tree2.delete(row)
        # Cargar datos de la base de datos
        fichas = FichaOrtodonciaController.obtener_fichas_por_cliente(cliente_id)
        for ficha in fichas:
            tag = "saldo_cero" if ficha.saldo == 0 else "saldo_no_cero"
            tree2.insert(
                "",
                "end",
                values=(ficha.fecha, ficha.actividad, ficha.brack, ficha.costo, ficha.abono, ficha.saldo),
                iid=ficha.id,  # Usar el ID de la ficha como identificador único
                tags=(tag,)
            )

    # Llamar a la función para cargar datos
    cargar_datos()

    # Función para eliminar una ficha
    def eliminar_ficha():
        selected_item = tree2.selection()  # Obtener el elemento seleccionado
        if selected_item:
            ficha_id = int(tree2.selection()[0])  # Obtener el ID (iid) del elemento
            FichaOrtodonciaController.eliminar_ficha(ficha_id)  # Eliminar ficha de la base de datos
            cargar_datos()  # Actualizar la tabla
            calcular_saldo_total()
    
    # Función para abrir ventana de edición
    def editar_ficha():
        selected_item = tree2.selection()  # Obtener el elemento seleccionado
        if not selected_item:
            return  # No hacer nada si no hay selección
        ficha_id = int(selected_item[0])  # Obtener el ID (iid) del elemento
        ficha = FichaOrtodonciaController.obtener_ficha_por_id(ficha_id)
        
        saldo_var = customtkinter.StringVar(value=f"{ficha.saldo:.2f}")
        
        def calcular_saldo():
            """Actualiza el campo de saldo calculando costo - abono."""
            try:
                costo = float(entries[3].get() or 0)
                abono = float(entries[4].get() or 0)
                saldo = costo - abono
                saldo_var.set(f"{saldo:.2f}")  # Actualizar el saldo
            except ValueError:
                saldo_var.set("0.00")
        if ficha:
            # Crear ventana para editar la ficha
            editar_window = customtkinter.CTkToplevel(tab_ficha)
            editar_window.title("Editar Ficha Odontológica")
            editar_window.geometry("400x500")

            # Crear campos para editar
            labels = ["Fecha", "Actividad","Brack", "Costo", "Abono", "Saldo"]
            values = [
                ficha.fecha,
                ficha.actividad,
                ficha.brack,
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
                elif i==5:
                    entry = customtkinter.CTkEntry(editar_window, textvariable=saldo_var, state="disabled")
                    entry.pack(pady=5)
                    entry.insert(0, str(values[i]))
                    entries.append(entry)
                    
                else:
                    entry = customtkinter.CTkEntry(editar_window)
                    entry.pack(pady=5)
                    entry.insert(0, str(values[i]))
                    entries.append(entry)
            costo_entry = entries[3]
            abono_entry = entries[4]
            costo_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
            abono_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
            # Función para guardar cambios
            def guardar_cambios():
                

                nueva_fecha = entries[0].get_date().strftime("%Y-%m-%d")
                nueva_actividad = entries[1].get()
                nuevo_brack = entries[2].get()
                try:
                    nuevo_costo = float(entries_ficha[3].get() or 0)
                    nuevo_abono = float(entries_ficha[4].get() or 0)
                    nuevo_saldo = float(entries_ficha[5].get() or 0)
                except ValueError:
                    showwarning("Error de entrada", "Por favor, asegúrate de que 'Costo' y 'Abono' sean números válidos.", parent=registros_window)
                    return

                FichaOrtodonciaController.actualizar_ficha(
                    ficha_id=ficha_id,
                    fecha=nueva_fecha,
                    actividad=nueva_actividad,
                    brack=nuevo_brack,
                    costo=nuevo_costo,
                    abono=nuevo_abono,
                    saldo=nuevo_saldo
                )
                cargar_datos()
                calcular_saldo_total()
                editar_window.destroy()

            guardar_button = customtkinter.CTkButton(editar_window, text="Guardar", command=guardar_cambios)
            guardar_button.pack(pady=10)

            cancelar_button = customtkinter.CTkButton(editar_window, text="Cancelar", command=editar_window.destroy)
            cancelar_button.pack(pady=10)

    # Función para agregar una nueva ficha
    def agregar_ficha():

        fecha = date_entry.get_date().strftime("%Y-%m-%d")
        actividad = entries_ficha[1].get()
        brack = entries_ficha[2].get()
        try:
            costo = float(entries_ficha[3].get() or 0)
            abono = float(entries_ficha[4].get() or 0)
            saldo = float(entries_ficha[5].get() or 0)
        except ValueError:
            showwarning("Error de entrada", "Por favor, asegúrate de que 'Costo' y 'Abono' sean números válidos.", parent=registros_window)
            return
        # Lógica para agregar ficha a la base de datos
        FichaOrtodonciaController.crear_ficha(
            cliente_id=cliente_id,
            fecha=fecha,
            actividad=actividad,
            brack=brack,
            costo=costo,
            abono=abono,
            saldo=saldo
        )

        # Actualizar tabla
        cargar_datos()
        calcular_saldo_total()
        for entry in entries_ficha[1:]:  # Limpiar los campos (excepto la fecha)
            entry.delete(0, "end")
        date_entry.set_date(datetime.now())  # Restablecer la fecha a hoy
        saldo_var.set("0.00")
        
    def calcular_saldo():
        """Actualiza el campo de saldo calculando costo - abono."""
        try:
            costo = float(costo_entry.get() or 0)
            abono = float(abono_entry.get() or 0)
            saldo = costo - abono
            saldo_var.set(f"{saldo:.2f}")  # Actualizar el valor del saldo
        except ValueError:
            saldo_var.set("0.00")
    # Crear botones para eliminar y editar fichas
    botones_frame = customtkinter.CTkFrame(tab_ficha)
    botones_frame.pack(pady=10)

    eliminar_button = customtkinter.CTkButton(botones_frame, text="Eliminar", command=eliminar_ficha, fg_color="#F24236")
    eliminar_button.grid(row=0, column=0, padx=10)

    editar_button = customtkinter.CTkButton(botones_frame, text="Editar", command=editar_ficha)
    editar_button.grid(row=0, column=1, padx=10)
        # Crear campos para agregar nueva ficha
    form_frame = customtkinter.CTkFrame(tab_ficha)
    form_frame.pack(pady=10)

    labels = ["Fecha", "Actividad", "Brack", "Costo", "Abono", "Saldo"]
    entries_ficha = []
    saldo_var = customtkinter.StringVar(value="0.00")
    for i, label_text in enumerate(labels):
        label = customtkinter.CTkLabel(form_frame, text=label_text)
        label.grid(row=0, column=i, padx=5)
        if i == 0:  # Campo de fecha con calendario
            date_entry = DateEntry(form_frame, date_pattern="yyyy-mm-dd")
            date_entry.grid(row=1, column=i, padx=5)
            date_entry.set_date(datetime.now())
            entries_ficha.append(date_entry)
        elif i==5:
            entry = customtkinter.CTkEntry(form_frame, textvariable=saldo_var, state="disabled")
            entry.grid(row=1, column=i, padx=5)
            entries_ficha.append(entry)
            
        else:
            entry = customtkinter.CTkEntry(form_frame)
            entry.grid(row=1, column=i, padx=5)
            entries_ficha.append(entry)
    costo_entry = entries_ficha[3]
    abono_entry = entries_ficha[4]

    costo_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
    abono_entry.bind("<KeyRelease>", lambda event: calcular_saldo())
    # Botón para agregar ficha
    add_button = customtkinter.CTkButton(tab_ficha, text="Agregar Ficha", command=agregar_ficha)
    add_button.pack(pady=10)