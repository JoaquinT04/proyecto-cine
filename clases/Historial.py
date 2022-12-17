
from base_de_datos import BDD
from datetime import timedelta, datetime

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
        BDD.cerrar(conexion)
        return print("EL usuario ya es super cliente")
      else:
        band = False
        consulta_ = f"SELECT UniqueID FROM Historial WHERE documento={id_usuario}"
        #print(BDD.consulta(conexion, consulta_))
        lista = BDD.consulta(conexion, consulta_)
        reservas = len(BDD.consulta(conexion, consulta_))
        #print(reservas)
        #Me hago una lista con todas las fechas de todas las reservas del usuario
        lista_de_fechas = []
        for elemento in lista:
          consulta_ = f"SELECT fecha FROM Historial WHERE UniqueID={elemento[0]}"
          fecha = BDD.consulta(conexion, consulta_)[0][0]
          lista_de_fechas.append(fecha)
        #print(len(lista_de_fechas))
        for i in range(len(lista_de_fechas)):
          primer_fecha = lista_de_fechas[i]
          primer_fecha = primer_fecha.split("/")
          primer_fecha = datetime(int(primer_fecha[2]), int(primer_fecha[1]), int(primer_fecha[0]))
          #print("Primer fecha: ", primer_fecha)
          despues_de_3meses = primer_fecha + timedelta(days=90)
          #print("Despues de 3 meses: ", despues_de_3meses)
          try:
            sexta_fecha = lista_de_fechas[i+5]
            sexta_fecha = sexta_fecha.split("/")
            sexta_fecha = datetime(int(sexta_fecha[2]), int(sexta_fecha[1]), int(sexta_fecha[0]))
            if despues_de_3meses >= sexta_fecha:
              band = True
          except:
            break

        if reservas >= 6 and band==True:
          consulta_ = f"UPDATE Usuario SET Super_Cliente = '1' WHERE DNI={id_usuario}" 
          BDD.consulta(conexion, consulta_)
          consulta_ = f"UPDATE Historial SET Super_Cliente = '1' WHERE documento={id_usuario}"
          BDD.consulta(conexion, consulta_)
          BDD.cerrar(conexion)
          return print("El usuario ahora es un super cliente")
        else:
          BDD.cerrar(conexion)
          return print("El susuario no cumple con las condiciones para ser super cliente")
