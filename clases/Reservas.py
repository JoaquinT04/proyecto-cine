class Reservas():
    def __init__(self):
        self.__listaReservas = []

    @property
    def listaReservas(self):
      return self.__listaReservas
    @listaReservas.setter
    def listaReservas(self, nuevolistaReservas):
      self.__listaReservas = nuevolistaReservas
    
    def __str__(self):
        cadena = "Lista Reservas: " + str(self.__listaReservas)
        return cadena

    def agregarReserva(self):
        pass

    def modificar(self):
        pass
    
    def buscarUsuario(self):
        pass

    def eliminarReserva(self):
        pass
    

    
