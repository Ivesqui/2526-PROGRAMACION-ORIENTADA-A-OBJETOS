from servicios.usuario_servicio import UsuarioServicio


def main():
    servicio = UsuarioServicio()

    print("=== SISTEMA DE REGISTRO DE USUARIOS ===")

    u1 = servicio.registrar_usuario("Christian", "ci.estupinanq@uea.edu.ec")
    u2 = servicio.registrar_usuario("Ana", "ana.ejemplo@uea.edu.ec")

    servicio.listar_usuarios()

    print("\nEliminando un usuario...\n")
    servicio.eliminar_usuario(u1)

    print("Fin del programa")


if __name__ == "__main__":
    main()
