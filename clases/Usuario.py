class Usuario():
    def __init__(self, nombre, apellido, dni=None):
        self.__dni_id = dni
        self.__historial = None
        self.__nombre = nombre
        self.__apellido = apellido
        self.__superCliente = None
    
    @property
    def dni_id(self):
      return self.__dni_id
    @dni_id.setter
    def dni_id(self, nuevodni):
      self.__dni_id = nuevodni
    
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
        cadena += "\nHistorial: " + str(self.__historial)
        cadena += "\nNombre: " + str(self.__nombre)
        cadena += "\nApellido: " + str(self.__apellido)
        cadena += "\nSuper Cliente: " + str(self.__superCliente)
        return cadena
    
    def crearReserva(self):
        pass

    def modificarReserva(self):
        pass

    def verReserva(self):
        pass

    def verHistorialDeUsuarioPropio(self):
        pass

    def verSalas(self):
        pass

    def registrarse(self):
        pass

    def ingresar(self):
        pass

    def pedirTarjeta(self):
        pass