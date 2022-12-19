from base_de_datos import BDD
from clases.Descuentos import myError,os 
from clases.Metodos_de_pago import Metodos_de_pago
class Reserva():
  def __init__(self,id_reserva = None,monto = None,sala = None,id_usuario = None,butaca = None):
    self.__id_reserva = id_reserva
    self.__monto = monto
    self.__sala = sala
    self.__id_usuario = id_usuario
    self.__butaca = butaca
  
  @property
  def id_reserva(self):
    return self.__id
  
  @property
  def usuario(self):
    return self.__usuario
  @usuario.setter
  def usuario(self, nuevousuario):
    self.__usuario = nuevousuario
  
  @property
  def sala(self):
    return self.__sala
  @sala.setter
  def sala(self, nuevosala):
    self.__sala = nuevosala
  
  @property
  def pagoEfectuado(self):
    return self.__pagoEfectuado
  @pagoEfectuado.setter
  def pagoEfectuado(self, nuevopagoEfectuado):
    self.__pagoEfectuado = nuevopagoEfectuado
  @property
  def butaca(self):
    return self.__butaca
  
  @butaca.setter
  def butaca(self,nuevaButaca):
    self.__butaca = nuevaButaca

  def __str__(self):
    cadena = "ID: " + str(self.__id_reserva)
    cadena += "\nUsuario: " + str(self.__id_usuario)
    cadena += "\nMonto: "+ str(self.__monto)
    cadena += "\nSala: " + str(self.__sala)
    cadena += "\nPago Efectuado: " + str(self.__pagoEfectuado)
    return cadena
  
  def modificarReserva(self):
    pass

