from clases import Sala
from clases import Descuentos
from base_de_datos import BDD
from clases import Butacas
import os

class miError(Exception):
	def __init__(self, msj) :
		self.__msj = msj
	
	@property
	def msj(self):
		return self.__msj

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

    def validarSala(self,id = None):
        p=Sala.BDD.crear_conexion()
        while True:
            try:
                if id == None:
                    id = int(input("Ingrese un id: "))
                else:
                    #Para lanzar error ValueError si es un caracter
                    id =int(id)

                if id<=0:
                    raise miError("Ingreso un id no valido!")

                consul=f"SELECT * FROM Sala WHERE id_sala = {id};"
                a=Sala.BDD.consulta(p,consul)

                if not a==[]:
                    raise miError("Ingreso un id no valido!")
                break

            except miError as err:
                print(err.msj)
                input()
                os.system("cls")  
                id = input("Ingrese un id: ")
            except ValueError :
                print("No se pueden ingresar letras o caracteres!")
                input()
                os.system("cls")  
                id = input("Ingrese un id: ")
        Sala.BDD.cerrar(p)
        return id

    def agregarSala(self):
        self.__idSala=self.validarSala(id=input("ingrese el id "))
        self.__formato=input("ingrese formato 2d o 3d ")
        self.__butacas=int(input("ingrese cantidad de butacas "))
        self.__pelicula=input("ingrese nombre de la pelicula ")
        desc=Descuentos.Descuentos()
        self.__descuento=desc._Descuentos__validarDia(input("ingrese un dia del 1 al 7 "))
        self.__precio=float(input("ingrese precio de la entrada "))
        self.__fecha=input("ingrese fecha de la funbcion en formato dd/mm/aa")
        self.__horario=input("ingrese horario en formato HH:MM ")
        print("ESTOS DATOS SON CORRECTOS? ")
        _r=input("para confirmar escriba Y , cualquier otro caracter para cancelar ")
        if _r == "Y":
            consulta=f"INSERT INTO Sala VALUES ({self.__idSala},'{self.__formato}','{self.__pelicula}','{self.__descuento}','{self.__precio}','{self.__fecha}','{self.__horario}','{self.__butacas}');"
            print(consulta)
            conexion=BDD.crear_conexion()
            mSala=BDD.consulta(conexion,consulta)
            BDD.cerrar(conexion)
            print("registro modificado")
            for i in range(self.__butacas):
                b=Butacas.Butacas()
                b.crearButaca(self.__idSala)
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
            b=Butacas.Butacas()
            b.eliminarButacasSala(_id)
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
        print("consulta:",a)
        c=Sala.Sala(a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7])
        c.modificarSala()

    def buscarSala(self):
        op=input("ingrese el nombre de la pelicula")
        p=Sala.BDD.crear_conexion()
        consul=f"SELECT * FROM Sala WHERE pelicula = '{op}';"
        a=Sala.BDD.consulta(p,consul)
        Sala.BDD.cerrar(p)
        self.__listaSalas=a
