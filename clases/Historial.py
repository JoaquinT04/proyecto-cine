class Historial():
    def __init__(self):
        self.__sala = None
        self.__reserva = None
    
    @property
    def sala(self):
      return self.__sala
    @sala.setter
    def sala(self, nuevosala):
      self.__sala = nuevosala
    
    @property
    def reserva(self):
      return self.__reserva
    @reserva.setter
    def reserva(self, nuevoreserva):
      self._reserva = nuevoreserva
    
    def __str__(self):
        cadena = "Sala: " + str(self.__sala)
        cadena += "\nReserva: " + str(self.__reserva)
        return cadena
    
    def buscarUsuario(self):
        pass

    def validarTarjeta(self):
        pass