from views.main_view import MainView
from models.database import init_db
import customtkinter

def main():
    init_db()
    customtkinter.set_appearance_mode("Dark")  # Opciones: "System", "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Tema de colores

    app = MainView()  # Instancia la ventana principal
    app.mainloop()    # Ejecuta el bucle principal de la app
    

if __name__ == "__main__":
    main()
    