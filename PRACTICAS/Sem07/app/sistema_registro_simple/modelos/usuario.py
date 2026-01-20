import os


class Usuario:
    def __init__(self, nombre, correo):
        """
        Constructor:
        Inicializa los datos del usuario y crea el archivo si no existe.
        """
        self.nombre = nombre
        self.correo = correo

        # Crear carpeta data si no existe
        if not os.path.exists("data"):
            os.makedirs("data")

        # Abrir o crear archivo
        self.archivo = open("data/usuarios.txt", "a", encoding="utf-8")
        self.archivo.write(f"Usuario creado: {self.nombre} - {self.correo}\n")

        print(f"[INIT] Usuario registrado: {self.nombre}")

    def obtener_datos(self):
        return f"{self.nombre} | {self.correo}"

    def __del__(self):
        """
        Destructor:
        Cierra el archivo abierto.
        """
        try:
            self.archivo.write(f"Usuario eliminado: {self.nombre}\n")
            self.archivo.close()
            print(f"[DEL] Archivo cerrado para {self.nombre}")
        except:
            pass
