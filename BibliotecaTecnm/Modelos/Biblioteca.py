import datetime
from .Libro import Libro
from .Usuario import Usuario
from collections import Counter
class Biblioteca():
  catalogo = {
    "9780001": Libro("9780001", "Cien Anios de Soledad", "Gabriel Garcia Marquez", 5),
    "9780002": Libro("9780002", "Don Quijote de la Mancha", "Miguel de Cervantes", 5),
    "9780003": Libro("9780003", "La Odisea", "Homero", 4),
    "9780004": Libro("9780004", "El Principito", "Antoine de Saint-Exupery", 5),
    "9780005": Libro("9780005", "1984", "George Orwell", 2),
    "9780006": Libro("9780006", "El Hobbit", "J.R.R. Tolkien", 4),
    "9780007": Libro("9780007", "Orgullo y Prejuicio", "Jane Austen", 5),
    "9780008": Libro("9780008", "Crimen y Castigo", "Fiodor Dostoyevski", 5),
    "9780009": Libro("9780009", "Rayuela", "Julio Cortazar", 1),
    "9780010": Libro("9780010", "El Alquimista", "Paulo Coelho", 2),
    "9780011": Libro("9780011", "IT", "Stephen King", 1),
    "9780012": Libro("9780012", "El Resplandor", "Stephen King", 1)
}
  usuarios = {
    1: Usuario(1, 'Juan', 'cll10', '3101111111', 'Clave123'),
    2: Usuario(2, 'Pedro', 'cll12', '3105555556', 'Contraseña'),
    3: Usuario(3, 'Maria', 'cll15', '3102222222', 'Segura456'),
    4: Usuario(4, 'Laura', 'cll18', '3103333333', 'Password789'),
    5: Usuario(5, 'Carlos', 'cll20', '3104444444', 'Clave321'),
    6: Usuario(6, 'Andres', 'cll22', '3106666666', 'MiPass123'),
    7: Usuario(7, 'Sofia', 'cll25', '3107777777', 'Segura987'),
    8: Usuario(8, 'Valentina', 'cll30', '3108888888', 'Pass456'),
    9: Usuario(9, 'Miguel', 'cll35', '3109999999', 'Clave999'),
    10: Usuario(10, 'Camila', 'cll40', '3101234567', 'ContraABC')
}
  prestamos = []
  historialPrestamos = []

  def __init__(self):
    print('Biblioteca abierta')

  def muestra_catalogo(self):
    print("Catalogo de libros:")
    for libro in self.catalogo.values():
      print(f"ISBN: {libro.isbn}, Titulo: {libro.titulo}, Autor: {libro.autor}")

  def genera_prestamo(self, libro, usuario):
      contador = 0
      for prestamo in self.prestamos:
          if prestamo[0] == usuario.documento:
              contador += 1
      if contador >= 3:
          print("El usuario ya tiene 3 prestamos activos")
          return
      if libro.ejemplares <= 0:
          print("No hay ejemplares disponibles")
          return
      for prestamo in self.prestamos:
          if prestamo[0] == usuario.documento and prestamo[1] == libro.isbn:
              print("El libro ya ha sido prestado por este usuario")
              return
      fecha = datetime.datetime.now()
      self.prestamos.append((usuario.documento, libro.isbn, fecha))
      self.historialPrestamos.append((usuario.documento, libro.isbn, fecha))
      libro.ejemplares -= 1
      print("El libro ha sido prestado correctamente")

  def devuelve_libro(self, libro, usuario):
    for prestamo in self.prestamos:
      if prestamo[0] == usuario.documento and prestamo[1] == libro.isbn:
        self.prestamos.remove(prestamo)
        print('El libro ha sido devuelto')
        libro.ejemplares += 1

  def consultar_usuarios(self):
    for usuario in self.usuarios.values():
      print(f'Usuario numero {usuario.documento}: nombre:{usuario.nombre} telefono:{usuario.telefono}')

  def listar_prestamos_activos(self):
    if len(self.prestamos) == 0:
        print("No hay prestamos activos")
        return
    print("Prestamos activos:")
    for prestamo in self.prestamos:
        usuario = self.usuarios.get(prestamo[0])
        libro = self.catalogo.get(prestamo[1])
        fecha = prestamo[2]
        print("Usuario:", usuario.nombre,
              "| Libro:", libro.titulo,
              "| Fecha:", fecha)
        
  def consultar_disponibilidad(self, isbn):
      if isbn in self.catalogo:
          libro = self.catalogo[isbn]
          print("Titulo:", libro.titulo)
          print("Ejemplares disponibles:", libro.ejemplares)
      else:
          print("Libro no encontrado")

  def libros_mas_prestados(self):
    if len(self.historialPrestamos) == 0:
      print("No hay historial")
    titulos = []
    for registro in self.historialPrestamos:
      libro = self.catalogo[registro[1]]
      titulos.append(libro.titulo)
    conteo = Counter(titulos)
    top3 = conteo.most_common(3)
    print("\nTop 3 libros mas prestados:")
    for titulo, cantidad in top3:
      print(titulo, "->", cantidad, "prestamos")