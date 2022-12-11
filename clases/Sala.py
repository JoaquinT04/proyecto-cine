class Sala():
    def __init__(self,id=none,formato=none,butacas=none,pelicula=none,descuento=none,horario=none,nro=none):
        self.__id=id
        self.__formato=formato
        self.__butacas=butacas
        self.__pelicula=pelicula
        self.__descuento=descuento
        self.__horario=horario #hh:mm
        self.__nroButacasReservadas=nro

    @property
    def id(self):
        return self.__id

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
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, nHorario):
        self.__hiorario=nHorario

    @property
    def nroButacasReservadas(self):
        return self.__nroButacasReservadas

    @nroButacasReservadas.setter
    def nroButacasReservadas(self, nNro):
        self.__nroButacasReservadas=nNro

    def __str__(self):
        cadena = 'id: ' + str(self.__id)
        cadena += '\nformato: ' + self.__formato
        cadena += '\nbutacas: ' + str(self.__butacas)
        cadena += '\npelicula: ' + self.__pelicula
        cadena += '\ndescuento: ' + str(self.__descuento)
        cadena += '\nhorario: ' + self.__horario
        cadena += '\nnroButacas: ' + str(self.__nroButacasReservadas)
        return cadena

    def verRservas():
        pass

    def modificarSala():
        pass 