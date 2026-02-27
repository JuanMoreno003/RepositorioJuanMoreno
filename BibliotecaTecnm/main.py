from Modelos.Biblioteca import Biblioteca
from Modelos import Usuario
from Modelos import Libro

def menu_principal(biblioteca):
    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Gestion de Libros")
        print("2. Gestion de Usuarios")
        print("3. Prestamos y Devoluciones")
        print("4. Reportes")
        print("5. Mostrar Catalogo")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_libros(biblioteca)
        elif opcion == "2":
            menu_usuarios(biblioteca)
        elif opcion == "3":
            menu_prestamos(biblioteca)
        elif opcion == "4":
            menu_reportes(biblioteca)
        elif opcion == "5":
            biblioteca.muestra_catalogo()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida")

def menu_libros(biblioteca):
    while True:
        print("\n--- Gestion de Libros ---")
        print("1. Registrar libro")
        print("2. Consultar disponibilidad")
        print("3. Buscar por titulo")
        print("4. Buscar por autor")
        print("5. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            isbn = input("ISBN: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            ejemplares = int(input("Ejemplares: "))
            libro = Libro(isbn, titulo, autor, ejemplares)
            libro.registrar_libro(biblioteca)

        elif opcion == "2":
            isbn = input("Ingrese ISBN: ")
            biblioteca.consultar_disponibilidad(isbn)

        elif opcion == "3":
            titulo = input("Ingrese titulo: ")
            resultados = []
            for libro in biblioteca.catalogo.values():
                if libro.titulo.lower() == titulo.lower():
                    resultados.append(libro)
            if resultados:
                for libro in resultados:
                    print(libro.titulo, "-", libro.autor)
            else:
                print("No encontrado")

        elif opcion == "4":
            autor = input("Ingrese autor: ")
            resultados = []
            for libro in biblioteca.catalogo.values():
                if libro.autor.lower() == autor.lower():
                    resultados.append(libro)
            if resultados:
                for libro in resultados:
                    print(libro.titulo)
            else:
                print("No encontrado")

        elif opcion == "5":
            break
        else:
            print("Opcion invalida")


def menu_usuarios(biblioteca):
    while True:
        print("\n--- Gestion de Usuarios ---")
        print("1. Registrar usuario")
        print("2. Consultar usuarios")
        print("3. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            documento = int(input("Documento: "))
            nombre = input("Nombre: ")
            direccion = input("Direccion: ")
            telefono = input("Telefono: ")
            contraseña = input("Contraseña: ")
            usuario = Usuario(documento, nombre, direccion, telefono, contraseña)
            usuario.registrar_usuario(biblioteca)

        elif opcion == "2":
            biblioteca.consultar_usuarios()

        elif opcion == "3":
            break
        else:
            print("Opcion invalida")

def menu_prestamos(biblioteca):
    while True:
        print("\n--- Prestamos y Devoluciones ---")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Ver prestamos activos")
        print("4. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            documento = int(input("Documento usuario: "))
            isbn = input("ISBN libro: ")

            usuario = biblioteca.usuarios.get(documento)
            libro = biblioteca.catalogo.get(isbn)

            if usuario and libro:
                biblioteca.genera_prestamo(libro, usuario)
            else:
                print("Usuario o libro no encontrado")

        elif opcion == "2":
            documento = int(input("Documento usuario: "))
            isbn = input("ISBN libro: ")

            usuario = biblioteca.usuarios.get(documento)
            libro = biblioteca.catalogo.get(isbn)

            if usuario and libro:
                biblioteca.devuelve_libro(libro, usuario)
            else:
                print("Usuario o libro no encontrado")

        elif opcion == "3":
            biblioteca.listar_prestamos_activos()

        elif opcion == "4":
            break
        else:
            print("Opcion invalida")

def menu_reportes(biblioteca):
    while True:
        print("\n--- Reportes ---")
        print("1. Top 3 libros mas prestados")
        print("2. Listado prestamos activos")
        print("3. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            biblioteca.libros_mas_prestados()

        elif opcion == "2":
            biblioteca.listar_prestamos_activos()

        elif opcion == "3":
            break
        else:
            print("Opcion invalida")

biblioteca = Biblioteca()
menu_principal(biblioteca)