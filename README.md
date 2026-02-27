Sistema de Gestion de Biblioteca

Sistema desarrollado en Python utilizando Programacion Orientada a Objetos para la gestion de libros, usuarios y prestamos en una biblioteca.

Descripcion General

El sistema permite registrar libros y usuarios, generar prestamos y devoluciones, consultar disponibilidad y obtener reportes estadisticos. La arquitectura esta basada en tres clases principales: Libro, Usuario y Biblioteca.

CLASES DEL SISTEMA

Claae Libro()-----------------------------------------------------

Descripcion:
Clase encargada de representar un libro dentro del catalogo de la biblioteca.

Input:

isbn: str
titulo: str
autor: str
ejemplares: int

Output:
Objeto de tipo Libro.

Atributos:

isbn: Identificador unico del libro.
titulo: Nombre del libro.
autor: Autor del libro.
ejemplares: Cantidad de ejemplares disponibles.

Metodos:

registrar_libro(Biblioteca):
Registra el libro en el catalogo si no existe previamente.

eliminar_libro(Biblioteca):
Elimina el libro del catalogo.

consultar_libro(Biblioteca, isbn):
Retorna un libro segun su ISBN.

consultar_libros_por_autor(Biblioteca, autor):
Retorna una lista de libros que pertenecen a un mismo autor.

consultar_libros_por_titulo(Biblioteca, titulo):
Retorna una lista de libros con el mismo titulo.

Clase Usuario()----------------------------------------------------

Descripcion:
Clase encargada de representar los usuarios registrados en la biblioteca.

Input:

documento: int
nombre: str
direccion: str
telefono: str
contrasña: str

Output:
Objeto de tipo Usuario.

Atributos:

documento: Identificador unico del usuario.
nombre: Nombre del usuario.
direccion: Direccion del usuario.
telefono: Numero telefonico.
contraseña: Clave de acceso del usuario.

Metodos:

registrar_usuario(Biblioteca):
Registra el usuario en la biblioteca si no existe previamente.

iniciar_sesion(Biblioteca, id, contraseña):
Permite validar credenciales de acceso.

elimina_usuario(Biblioteca):
Elimina un usuario del sistema.

consulta_usuario(Biblioteca, documento):
Retorna un usuario segun su documento.

Clase Biblioteca()---------------------------------------------------

Descripcion:
Clase principal del sistema. Gestiona el catalogo de libros, los usuarios y los prestamos.

Atributos:

catalogo: Diccionario de libros con estructura {isbn: Libro}.
usuarios: Diccionario de usuarios con estructura {documento: Usuario}.
prestamos: Lista de prestamos activos almacenados como tuplas (documento, isbn, fecha).
historialPrestamos: Lista con todos los prestamos realizados.

Metodos:

muestra_catalogo():
Muestra todos los libros registrados en el sistema.

genera_prestamo(libro, usuario):
Genera un prestamo validando las reglas de negocio:

Maximo 3 prestamos activos por usuario.

No permite prestamos duplicados del mismo libro al mismo usuario.

No permite prestar si no hay ejemplares disponibles.

devuelve_libro(libro, usuario):
Elimina el prestamo activo correspondiente y aumenta el numero de ejemplares disponibles.

consultar_usuarios():
Muestra los usuarios registrados.

listar_prestamos_activos():
Muestra todos los prestamos vigentes.

consultar_disponibilidad(isbn):
Muestra la cantidad de ejemplares disponibles de un libro.

libros_mas_prestados():
Calcula los libros mas prestados utilizando un contador de frecuencias.

