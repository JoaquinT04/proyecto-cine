from base_de_datos import BDD
from clases.Reservas import Reservas
from clases.Salas import Salas
from clases.Historial import Historial
class Usuario():
  def __init__(self, nombre = None, apellido=None, dni=None,contrasenia = None):
    self.__dni_id = dni
    self.__nombre = nombre
    self.__apellido = apellido
    self.__superCliente = '0'
    self.__contrasenia = contrasenia
  
  @property
  def dni_id(self):
    return self.__dni_id
  @dni_id.setter
  def dni_id(self, nuevodni):
    self.__dni_id = nuevodni
  
  @property
  def contrasenia(self):
    return self.__contrasenia
  
  @contrasenia.setter
  def contrasenia(self,nuevaContrasenia):
    self.__contrasenia = nuevaContrasenia

  @property
  def historial(self):
    return self.__historial
  @historial.setter
  def historial(self, nuevohistorial):
    self.__historial = nuevohistorial
  
  @property
  def nombre(self):
    return self.__nombre
  @nombre.setter
  def nombre(self, nuevonombre):
    self.__nombre = nuevonombre
  
  @property
  def apellido(self):
    return self.__apellido
  @apellido.setter
  def apellido(self, nuevoapellido):
    self.__apellido = nuevoapellido
  
  @property
  def superCliente(self):
    return self.__superCliente
  @superCliente.setter
  def superCliente(self, nuevosuperCliente):
    self.__superCliente = nuevosuperCliente
  
  def __str__(self):
    cadena = "DNI: " + str(self.__dni_id)
    cadena += "\nNombre: " + str(self.__nombre)
    cadena += "\nApellido: " + str(self.__apellido)
    cadena += "\nSuper Cliente: " + str(self.__superCliente)
    cadena += "\nContrasenia: "+str(self.__contrasenia)
    return cadena
  
  def validarDNI(self):
    pass

  def crearUsuario(self,DNI,nombre,apellido,contrasenia):
    conexion = BDD.crear_conexion()
    consulta_ = f"insert into Usuario values('{DNI}','{nombre}','{apellido}','0','{contrasenia}');"
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)
  
  def eliminarUsuario(self,DNI,contrasenia):
    conexion = BDD.crear_conexion()
    consulta_ = f"delete from Usuario where DNI = '{DNI}' and Contrasenia = '{contrasenia}';"
    #Borrar todas las reservas de este usuario
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)

  def modificarUsuario(self,DNI):
    conexion = BDD.crear_conexion()
    nombre = input("Ingrese un nuevo Nombre: ")
    apellido = input("Ingrese un nuevo Apellido: ")
    contrasenia = input("Ingrese un nuevo contrasenia: ")

    consulta_ = f"update Usuario set nombre = '{nombre}', apellido = '{apellido}', contrasenia = '{contrasenia}' where DNI = {DNI};"
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)
  
  def verUsuarios(self,DNI = None):
    conexion = BDD.crear_conexion()
    if DNI == None:
      consulta_ = f"select * from Usuario;"
    else:  
      consulta_ = f"select * from Usuario where DNI = {DNI};"
    usuarios = BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)
    return usuarios

  def crearReserva(self,idSala):
    reserva = Reservas()
    reserva.agregarReserva(idSala,self.__dni_id)

  def borrarReserva(self):
    reserva = Reservas()
    print(reserva.buscarXUsuario(self.dni_id))
    option = int(input("Ingrese el id de la reserva que quiere eliminar: "))
    reserva.eliminarReserva(option)

  def verReserva(self):
    reserva = Reservas()
    return reserva.buscarXUsuario(self.dni_id)
    

  def verHistorialDeUsuarioPropio(self):
    pass

  def verSalas(self):
    sala = Salas()
    return sala

  def ingresar(self,DNI,contrasenia):
    conexion = BDD.crear_conexion()
    consulta_ = f"select * from Usuario where DNI = {DNI} and Contrasenia = '{contrasenia}';"
    usuario = BDD.consulta(conexion,consulta_)
    if usuario == []:
      BDD.cerrar(conexion)
      return False
    else:
      self.dni_id = usuario[0][0]
      self.nombre = usuario[0][1]
      self.apellido = usuario[0][2]
      self.superCliente = usuario[0][3]
      self.contrasenia = usuario[0][4]
      BDD.cerrar(conexion)
      return True

  def pedirTarjeta(self):
    historial = Historial()
    return historial.validarTarjeta(self.dni_id)