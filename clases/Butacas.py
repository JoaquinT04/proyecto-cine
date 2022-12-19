from base_de_datos import BDD 
class Butacas():
  def __init__(self, id = None,idSala = None,estado = None):
    self.__id = id
    self.__idSala = idSala
    self.__estado = estado
  
  @property
  def id(self):
    return self.__id
  @property
  def idSala(self):
    return self.__idSala
  @property
  def estado(self):
    return self.__estado
  
  @estado.setter
  def estado(self, nuevoestado):
    self.__estado = nuevoestado
  
  @idSala.setter
  def idSala(self,nuevoIdSala):
    self.__idSala = nuevoIdSala
  
  def __str__(self):
    cadena = "\nID: " + str(self.__id)
    cadena += "\nEstado: " + str(self.__estado)
    return cadena   
  
  def crearButaca(self,idSala):
    conexion = BDD.crear_conexion()
    consulta_ = f"insert into Butacas values (NULL,'{idSala}',NULL)"
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)

  def eliminarButacasSala(self,idSala):
    conexion = BDD.crear_conexion()
    consulta_ = f"delete from Butacas where salaID = {idSala}"
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)

  def modificarButaca(self,idButaca,nuevoEstado):
    conexion = BDD.crear_conexion()
    if nuevoEstado != "NULL":
      consulta_ = f"update Butacas set estado ={nuevoEstado} where UniqueID = {idButaca}"
    else:  
      consulta_ = f"update Butacas set estado = NULL where UniqueID = {idButaca}"
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)

  def modificarButacaSala(self,idSala,nuevoEstado):
    conexion = BDD.crear_conexion()
    if nuevoEstado != "NULL":
      consulta_ = f"update Butacas set estado ={nuevoEstado} where salaID = {idSala}"
    else:  
      consulta_ = f"update Butacas set estado = NULL where salaID = {idSala}"
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)

  def modificarButacaReserva(self,idReserva,nuevoEstado):
    conexion = BDD.crear_conexion()
    if nuevoEstado != "NULL":
      consulta_ = f"update Butacas set estado ={nuevoEstado} where estado = {idReserva}"
    else:
      consulta_ = f"update Butacas set estado = NULL where estado = {idReserva}"
      
    BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)


  def mostrarButacasDNI(self,idUsuario):
    conexion = BDD.crear_conexion()
    consulta_ = f"select * from Butacas where estado = {idUsuario}"
    butacas = BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)
    return butacas

  def buscarXEstadoySala(self,idSala,estado):
    conexion = BDD.crear_conexion()
    if estado != "NULL":
      consulta_ = f"select * from Butacas where estado= {estado} and salaID = {idSala}"
    else:
      consulta_ = f"select * from Butacas where estado IS NULL and salaID = {idSala}"
    salas = BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)
    return salas
