class Usuario():
  documento = 0
  rol = 0
  nombre = ''
  direccion = ''
  telefono = ''
  contraseña = ''
  prestamos = []

  def __init__(self, documento, nombre, direccion, telefono, contraseña):
    self.documento = documento
    self.nombre = nombre
    self.direccion = direccion
    self.telefono = telefono
    self.contraseña = contraseña


  def registrar_usuario(self, Biblioteca):
    if self.documento not in Biblioteca.usuarios:
      Biblioteca.usuarios[self.documento] = self
      print(f"Usuario {self.nombre} registrado exitosamente.")
    else:
      print('Usuario ya registrado')

  def iniciar_sesion(self, Biblioteca,id ,contraseña):
    if id in Biblioteca.usuarios and Biblioteca.usuarios[self.documento].contraseña == contraseña:
      return Biblioteca.usuarios[self.documento]
    else:
      return None

  def elimina_usuario(self,Biblioteca):
    if self.documento in Biblioteca.usuarios:
      del Biblioteca.usuarios[self.documento]
      print(f"Usuario {self.nombre} eliminado exitosamente de la biblioteca.")

  def consulta_usuario(self, Biblioteca, documento):
    if documento in Biblioteca.usuarios:
      return Biblioteca.usuarios[documento]
    else:
      print('No existe el usuario')
      return None