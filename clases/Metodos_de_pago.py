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
    
    
    def darMonto(self):
        pass

    def darCVU(self):
        pass

    def modificarMetodoDePago(self):
        pass