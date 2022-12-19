from clases.Butacas import Butacas
from base_de_datos import BDD
from clases.Metodos_de_pago import Metodos_de_pago
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
        monto = Metodos_de_pago().darMonto(sala,id_usuario) 
        consulta_ = f"insert into Reserva values (NULL,{monto},{sala},{id_usuario})"
        butaca = Butacas()
        butacas = butaca.buscarXEstadoySala(sala,"NULL")
        print(butacas)
        option = int(input("Ingrese el id de la butaca: "))
        butaca.modificarButaca(option)
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
        butaca.modificarButacaReserva(idReserva)
        consulta_ = f"delete from Reserva where id_reserva = {idReserva} and id_usuario = {idUsuario})"
        BDD.consulta(conexion,consulta_)
        BDD.cerrar(conexion)
        
    

    
