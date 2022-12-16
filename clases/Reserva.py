class Reserva():
    def __init__(self):
      self.__id = None
      self.__usuario = None
      self.__sala = None
      self.__pagoEfectuado = None
    
    @property
    def id(self):
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
    
    def __str__(self):
      cadena = "ID: " + str(self.__id)
      cadena += "\nUsuario: " + str(self.__usuario)
      cadena += "\nSala: " + str(self.__sala)
      cadena += "\nPago Efectuado: " + str(self.__pagoEfectuado)
      return cadena

    def modificarReserva(self):
      pass

