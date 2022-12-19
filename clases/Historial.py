
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
  

  # def __rangoTiempo(self,fechaInicial):
  #   #TE devuelve una fecha final
  #   pass
  def agregarHistorial(self,idSala):
    #Traigo una lista de reservas con el idSala
    #Osea todas las reservas de una sala
    conexion = BDD.crear_conexion()
    consulta_ = f"select * from Reserva where sala = {idSala};"
    reservas = BDD.consulta(conexion,consulta_)
    #Recorro cada reserva de la lista de reservas
    for reserva in reservas:
      print(reserva)
      #Traigo los datos del Usuario
      consulta_ =  f"select * from Usuario where DNI = {reserva[3]}"
      usuario = BDD.consulta(conexion,consulta_)[0]
      dni=usuario[0]
      nombre=usuario[1]
      apellido=usuario[2]
      superCliente= usuario[3]
      #Traigo los datos de la Sala
      consulta_ =  f"select * from Sala where id_sala = {reserva[2]}"
      sala = BDD.consulta(conexion,consulta_)[0]
      formato=sala[1]
      pelicula=sala[2]
      monto= sala[4]
      fecha=sala[5]
      horario=sala[6]

      #Envio los valores necesarios para la creacion de un Historial
      consulta_ =  f"insert into Historial values (NULL, {dni},'{nombre}','{apellido}',{superCliente},'{pelicula}','{formato}','{fecha}','{horario}',{monto})"
      BDD.consulta(conexion,consulta_)
    BDD.cerrar(conexion)

  def buscarUsuario(self, idUsuario):
    conexion = BDD.crear_conexion()
    id_usuario = idUsuario
    consulta_ = f"SELECT * FROM Historial WHERE documento ={id_usuario}"
    historial = BDD.consulta(conexion, consulta_)
    # consulta_ = f"SELECT id_reserva FROM Reserva WHERE id_reserva={reserva}"
    # veces = BDD.consulta(conexion, consulta_)[0][0]
    BDD.cerrar(conexion)
    return historial

  def validarTarjeta(self, idUsuario):
    conexion = BDD.crear_conexion()
    id_usuario = idUsuario
    consulta_ = f"SELECT Super_Cliente FROM Historial WHERE documento={id_usuario}"
    try:
      supercliente = BDD.consulta(conexion, consulta_)[0][0]  #0 si es falso, 1 si es verdadero
    except IndexError as err:
      print("el cliente no esta en el historial")
      supercliente = []
    
    if supercliente != []:
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
          # consulta_ = f"UPDATE Historial SET Super_Cliente = '1' WHERE documento={id_usuario}"
          # BDD.consulta(conexion, consulta_)
          BDD.cerrar(conexion)
          # print("El usuario ahora es un super cliente")
          return True
        else:
          BDD.cerrar(conexion)
          # print("El susuario no cumple con las condiciones para ser super cliente")
          return False 
    else:
      return False
