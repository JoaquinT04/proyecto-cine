from clases import Sala
class Salas():
    def __init__(self,listaSala=[]):
        self.__listaSalas=listaSala

    @property
    def listaSala(self):
        return self.__listaSalas

    def __str__(self):
        cadena=""
        for l in self.__listaSalas:
            cadena += str(l) + "\n"
            cadena += "(----------------)" + "\n"
        return cadena

    def agregarSala():
        pass

    def eliminarSala():
        pass

    def modificar(idSala):
        _id=idSala
    
        pass

    def buscarSala():
        pass





