class Libro():
  isbn = ''
  titulo = ''
  autor = ''
  ejemplares = 0


  def __init__ (self,isbn,titulo, autor, ejemplares):
    self.isbn = isbn
    self.titulo = titulo
    self.autor = autor
    self.ejemplares = ejemplares

  #def __del__(self):
   # print(f'El libro {self.titulo} se ha eliminado')

  def registrar_libro(self, Biblioteca):
    if self.isbn not in Biblioteca.catalogo:
      Biblioteca.catalogo[self.isbn] = self
      print(f"Libro {self.titulo} registrado exitosamente.")

  def eliminar_libro(self, Biblioteca):
    if self.isbn in Biblioteca.catalogo:
      del Biblioteca.catalogo[self.isbn]
      print(f"Libro {self.titulo} eliminado exitosamente de la biblioteca.")

  def consultar_libro(self, Biblioteca, isbn):
    if isbn in Biblioteca.catalogo:
      return Biblioteca.catalogo[isbn]
    else:
      return None

  def consultar_libros_por_autor(self, Biblioteca, autor):
    libros_autor = []
    for libro in Biblioteca.catalogo.values():
      if libro.autor == autor:
        libros_autor.append(libro)
    return libros_autor

  def consultar_libros_por_titulo(self, Biblioteca, titulo):
    libros_titulo = []
    for libro in Biblioteca.catalogo.values():
      if libro.titulo == titulo:
        libros_titulo.append(libro)
    return libros_titulo
