from views.main_view import MainView
from models.database import init_db
import customtkinter
import socket
import sys
from tkinter import messagebox

def check_single_instance():
    try:
        # Crea un socket local para evitar múltiples instancias
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", 65432))  # Puerto único para la aplicación
        return sock
    except OSError:
        # Si el puerto ya está en uso, muestra un error y cierra
        messagebox.showerror("Error", "La aplicación ya está en ejecución.")
        sys.exit()

def main():
    # Verifica que no haya otra instancia en ejecución
    lock_socket = check_single_instance()

    # Inicializa la base de datos y la ventana principal
    init_db()
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    app = MainView()  # Instancia la ventana principal
    app.mainloop()    # Ejecuta el bucle principal de la app
    

if __name__ == "__main__":
    main()
