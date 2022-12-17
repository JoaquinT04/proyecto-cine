from clases import Sala
from clases import Descuentos
from base_de_datos import BDD

class Salas():
    p=Sala.BDD.crear_conexion()
    consul="SELECT * FROM Sala;"
    def __init__(self,listaSala=Sala.BDD.consulta(p,consul)):
        self.__listaSalas=listaSala

    Sala.BDD.cerrar(p)
    @property
    def listaSala(self):
        return self.__listaSalas

    def __str__(self):
        cadena=""
        for l in self.__listaSalas:
            cadena += str(l) + "\n"
            cadena += "(----------------)" + "\n"
        return cadena

    def agregarSala(self):
        self.__formato=input("ingrese formato 2d o 3d ")
        self.__butacas=input("ingrese cantidad de butacas ")
        self.__pelicula=input("ingrese nombre de la pelicula ")
        desc=Descuentos.Descuentos()
        self.__descuento=desc._Descuentos__validarDia(input("1 al 7"))
        self.__precio=float(input("ingrese precio de la entrada "))
        self.__horario=input("ingrese horario en formato HH:MM ")
        print("ESTOS DATOS SON CORRECTOS? ")
        _r=input("para confirmar escriba Y , cualquier otro caracter para cancelar ")
        if _r == "Y":
            consulta=f"INSERT INTO Sala VALUES (NULL,'{self.__formato}','{self.__pelicula}','{self.__descuento}','{self.__precio}','{self.__horario}','{self.__butacas}');"
            print(consulta)
            conexion=BDD.crear_conexion()
            mSala=BDD.consulta(conexion,consulta)
            BDD.cerrar(conexion)
            print("registro modificado")
            return "registro actualizado"

        else:
            print("descartando los datos")
            return "operacion cancelada"
        pass

    def eliminarSala(self,idSala):
        print("idSala: "+str(idSala))
        borrar=bool(input("ingrese cualquiere caracter para confirmar, dejar vacio para cancelar. "))
        if borrar == True:
            _id=idSala
            p=Sala.BDD.crear_conexion()
            consul=f"DELETE FROM Sala WHERE id_sala = {_id};"
            a=Sala.BDD.consulta(p,consul)
            Sala.BDD.cerrar(p)
            print("datos de la sala eliminados")
            return "sala borrada"
        else:
            print("operacion cancelada")
            return "no se borro ningun dato"

    def modificar(self,idSala):
        _id=idSala
        p=Sala.BDD.crear_conexion()
        consul=f"SELECT * FROM Sala WHERE id_sala = {_id};"
        a=Sala.BDD.consulta(p,consul)
        Sala.BDD.cerrar(p)
        c=Sala.Sala(a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6])
        c.modificarSala()

    def buscarSala(self):
        op=input("ingrese el nombre de la pelicula")
        p=Sala.BDD.crear_conexion()
        consul=f"SELECT * FROM Sala WHERE pelicula = '{op}';"
        a=Sala.BDD.consulta(p,consul)
        Sala.BDD.cerrar(p)
        self.__listaSalas=a






