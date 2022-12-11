class Salas():
    def __init__(self,listaSala=[]):
        self.__listaSalas=listaSala

    @property
    def listaSala(self):
        return self.__listaSalas

    def __str__(self):
        for l in self.__listaSalas:
            cadena += l
            cadena += "(----------------)"
        return cadena

def agregarSala():
    pass

def eliminarSala():
    pass

def modificar():
    pass

def buscarSala():
    pass





