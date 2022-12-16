from base_de_datos.BDD import *
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
    
    def __rangoTiempo(self,fechaInicial):
      #TE devuelve una fecha final
      pass

    def buscarUsuario(self, idUsuario):
      conexion = BDD.crear_conexion()
      id_usuario = idUsuario
      consulta_ = f"SELECT reserva FROM Usuario WHERE DNI={id_usuario}"
      reserva = BDD.consulta(conexion, consulta_)[0][0]
      consulta_ = f"SELECT id_reserva FROM Reserva WHERE id_reserva={reserva}"
      veces = BDD.consulta(conexion, consulta_)[0][0]
      BDD.cerrar(conexion)
      return veces

    def validarTarjeta(self, idUsuario):
      conexion = BDD.crear_conexion()
      id_usuario = idUsuario
      consulta_ = f"SELECT Super_Cliente FROM Historial WHERE documento={id_usuario}"
      supercliente = BDD.consulta(conexion, consulta_)[0][0]  #0 si es falso, 1 si es verdadero
      if supercliente==1:
        return "EL usuario ya es super cliente"
      else:
        consulta_ = f"SELECT reserva FROM Usuario WHERE DNI={id_usuario}"
        reserva = BDD.consulta(conexion, consulta_)[0][0]
        consulta_ = f"SELECT id_reserva FROM Reserva WHERE id_reserva={reserva}"
        veces = len(BDD.consulta(conexion, consulta_)[0])
        BDD.cerrar(conexion)
        if veces >= 6:
          consulta_ = f"UPDATE Usuario SET Super_Cliente = '1' WHERE DNI={id_usuario}"
          return "El usuario ahora es un super cliente"
        else:
          return "El susuario no cumple con las condiciones para ser super cliente"
      


