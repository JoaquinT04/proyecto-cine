#from base_de_datos import BDD
from clases import Sala
from clases import Salas

p=Sala.BDD.crear_conexion()
#consul="SELECT * FROM Sala WHERE id_sala = 1;"
#a=Sala.BDD.consulta(p,consul)
#Sala.BDD.cerrar(p)
#print(a)
#_a=f"{a[0][0]},{a[0][1]},{a[0][2]},{a[0][3]},{a[0][4]},{a[0][5]},{a[0][6]}"
#print(_a)
#c=Sala.Sala(a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6])
#print(c)
#c.modificarSala()

#print(c)

#c=Sala.Sala(0,"7d",10,"la chancla voladora",1,600,"16:30",3) #creacion manual del objeto sala, solo para pruevas
#print(c)
#c.verReservas()
#print(c.verReservas())
#c.modificarSala()


consul="SELECT * FROM Sala;"
a=Sala.BDD.consulta(p,consul)
Sala.BDD.cerrar(p)
lS=Salas.Salas(a)
print(lS)