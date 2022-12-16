class Butacas():
    def __init__(self):
        self.__id = None
        self.__estado = None
    
    @property
    def id(self):
      return self.__id
    
    @property
    def estado(self):
      return self.__estado
    @estado.setter
    def estado(self, nuevoestado):
      self.__estado = nuevoestado
    
    def __str__(self):
        cadena = "\nID: " + str(self.__id)
        cadena += "\nEstado: " + str(self.__estado)
        return cadena   