from base_de_datos import BDD
class Metodos_de_pago():
  def __init__(self):
    self.__id = None
    self.__opcionesdepago = [None ,None]
  
  @property
  def id(self):
    return self.__id
  
  @property
  def opcionesdepago(self):
    return self.__opcionesdepago
  @opcionesdepago.setter
  def opcionesdepago(self, nuevoopcionesdepago):
    self.__opcionesdepago = nuevoopcionesdepago
  
  def __str__(self):
    cadena = "ID: " + str(self.__id)
    cadena += "\nOpciones de pago: " + str(self.__opcionesdepago)
    return cadena
  
  
  def darMonto(self, idSala, idUsuario):
    conexion = BDD.crear_conexion()
    descuento = 0
    id_sala = idSala
    id_usuario = idUsuario
    consulta_ = f"SELECT precio FROM Sala WHERE id_sala={id_sala}"
    precio = float(BDD.consulta(conexion, consulta_)[0][0])
    consulta_ = f"SELECT Super_Cliente FROM Usuario WHERE DNI={id_usuario}"
    supercliente = BDD.consulta(conexion, consulta_)[0][0]  #0 si es falso, 1 si es verdadero
    if supercliente:
      consulta_ = f"SELECT descuento FROM Sala WHERE id_sala = {id_sala};"
      dia = float(BDD.consulta(conexion, consulta_)[0][0])
      consulta_ = f"select descuento from Descuentos WHERE dia = {dia};"
      descuento = float(BDD.consulta(conexion, consulta_)[0][0])
    monto = precio - precio*(descuento/100)
    return monto
