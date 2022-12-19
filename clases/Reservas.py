from clases.Butacas import Butacas
from base_de_datos import BDD
from clases.Metodos_de_pago import Metodos_de_pago
from clases.Descuentos import myError
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

    def agregarReserva(self,sala,id_usuario):
        conexion = BDD.crear_conexion()
        #Creo la reserva
        monto = Metodos_de_pago().darMonto(sala,id_usuario) 
        consulta_ = f"insert into Reserva values (NULL,{monto},{sala},{id_usuario},'0')"
        BDD.consulta(conexion,consulta_)
        #Actualizo la butaca
        butaca = Butacas()
        butacas = butaca.buscarXEstadoySala(sala,"NULL")
        print(butacas)
        #Me aseguro de que haya butacas disponibles para elegir
        if butacas == [] :
            #Aqui no hay butacas disponibles
            self.eliminarReserva(idReserva)
        else:
            #Aqui si hay butacas disponibles
            try:
                option = int(input("Ingrese el id de la butaca: "))
                consulta_ = f"select id_reserva from Reserva where sala = {sala} and id_usuario = {id_usuario} and butaca = '0';"
                idReserva = BDD.consulta(conexion,consulta_)[0][0]
                print(idReserva)
                butaca.modificarButaca(option,idReserva)
                #Actualizo la butaca de la Reserva
                self.modificarXButaca(idReserva,1)
            except ValueError :
                self.eliminarReserva(idReserva)

        BDD.cerrar(conexion)
        
    def modificarXButaca(self,idReserva,butaca):
        conexion = BDD.crear_conexion()
        consulta_ = f"update Reserva set butaca = {butaca} where id_reserva = {idReserva};"
        BDD.consulta(conexion,consulta_)
        BDD.cerrar(conexion)

    # def modificarReserva(self):
    #     conexion = BDD.crear_conexion()

    #     #Que puedo modificar?

    #     consulta_ = f"upadate Reserva set "
    #     BDD.consulta(conexion,consulta_)
    #     BDD.cerrar(conexion)


    def buscarXUsuario(self,id_usuario):
        conexion = BDD.crear_conexion()
        consulta_ = f"select * from Reserva where id_usuario = {id_usuario}"
        usuarios = BDD.consulta(conexion,consulta_)
        BDD.cerrar(conexion)
        return usuarios
        
    def eliminarReserva(self,idReserva):
        conexion = BDD.crear_conexion()
        butaca = Butacas()
        butaca.modificarButacaReserva(idReserva,"NULL")
        consulta_ = f"delete from Reserva where id_reserva = {idReserva};"
        BDD.consulta(conexion,consulta_)
        BDD.cerrar(conexion)