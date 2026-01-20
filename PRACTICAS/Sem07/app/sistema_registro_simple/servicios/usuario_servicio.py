from modelos.usuario import Usuario


class UsuarioServicio:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, correo):
        usuario = Usuario(nombre, correo)
        self.usuarios.append(usuario)
        return usuario

    def listar_usuarios(self):
        print("\nUsuarios registrados en memoria:")
        for usuario in self.usuarios:
            print(usuario.obtener_datos())

    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            del usuario
