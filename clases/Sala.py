from base_de_datos import BDD
class Sala():
    def __init__(self,id=None,formato=None,pelicula=None,descuento=None,precio=None,frcha=None,horario=None,butacas=None,nro=None):
        self.__id=id
        self.__formato=formato
        self.__butacas=butacas
        self.__pelicula=pelicula
        self.__descuento=descuento
        self.__precio=precio
        self.__fecha #dd/mm/aa
        self.__horario=horario #hh:mm
        self.__nroButacasReservadas=nro

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nId):
        self.__id=nId

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, nFormato):
        self.__formato=nFormato

    @property
    def butacas(self):
        return self.__butacas

    @butacas.setter
    def butacas(self, nButacas):
        self.__butacas=nButacas

    @property
    def pelicula(self):
        return self.__pelicula

    @pelicula.setter
    def pelicula(self, nPelicula):
        self.__pelicula=nPelicula

    @property
    def descuento(self):
        return self.__descuento

    @descuento.setter
    def descuento(self, nDescuento):
        self.__descuento=nDescuento

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, nPrecio):
        self.__precio=nPrecio

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, nHorario):
        self.__hiorario=nHorario

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nFecha):
        self.__fecha=nFecha

    @property
    def nroButacasReservadas(self):
        return self.__nroButacasReservadas

    @nroButacasReservadas.setter
    def nroButacasReservadas(self, nNro):
        self.__nroButacasReservadas=nNro

    def __str__(self):
        cadena = 'id: ' + str(self.__id)
        cadena += '\nformato: ' + str(self.__formato)
        cadena += '\nbutacas: ' + str(self.__butacas)
        cadena += '\npelicula: ' + str(self.__pelicula)
        cadena += '\ndescuento: ' + str(self.__descuento)
        cadena += '\nprecio: ' + str(self.__precio)
        cadena += '\nfecha: ' + str(self.__fecha)
        cadena += '\nhorario: ' + str(self.__horario)
        cadena += '\nnroButacas reservadas: ' + str(self.__nroButacasReservadas)
        return cadena


    def verReservas(self):

        conexion = BDD.crear_conexion()
        consulta=f"SELECT * FROM Reserva WHERE sala = {self.id};"
        vReservas=BDD.consulta(conexion,consulta)#[0][0]
        BDD.cerrar(conexion)
        return vReservas        


    def modificarSala(self):
        print(self)
        self.formato=input("ingrese formato 2d o 3d ")
        self.butacas=int(input("ingrese cantidad de butacas "))
        self.pelicula=input("ingrese nombre de la pelicula ")
        self.descuento=int(input("ingrese indice del descuento 1 a 7 "))
        self.precio=float(input("ingrese precio de la entrada "))
        self.fecha=input("ingrese fecha en formato dd/mm/aa ")
        self.horario=input("ingrese horario en formato HH:MM ")
        print("ESTOS DATOS SON CORRECTOS? ")
        _r=input("para confirmar escriba Y , cualquier otro caracter para cancelar ")
        if _r == "Y":
            consulta=f"UPDATE Sala SET formato = '{self.formato}', pelicula = '{self.pelicula}', descuento = '{self.descuento}', precio = '{self.precio}', fecha = '{self.fecha}', horario = '{self.horario}', nro_Butacas = '{self.butacas}' WHERE id_sala = {self.id};"
            #print(consulta)
            conexion=BDD.crear_conexion()
            mSala=BDD.consulta(conexion,consulta)
            BDD.cerrar(conexion)
            print("registro modificado")
            return "registro actualizado"

        else:
            print("descartando los datos")
            return "operacion cancelada"
    