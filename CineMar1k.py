from base_de_datos import BDD
from clases import Sala
from clases import Salas #¡comentar esta importacon cuando quiean regenerar la base de datos!
from clases import Historial
from clases import Descuentos
from clases import Administrador
# p=Sala.BDD.crear_conexion()
# #consul="SELECT * FROM Sala WHERE id_sala = 1;"
# #a=Sala.BDD.consulta(p,consul)
# #Sala.BDD.cerrar(p)
# #print(a)
# #_a=f"{a[0][0]},{a[0][1]},{a[0][2]},{a[0][3]},{a[0][4]},{a[0][5]},{a[0][6]}"
# #print(_a)
# #c=Sala.Sala(a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6])
# #print(c)
# #c.modificarSala()


#c=Sala.Sala(3,"7d",10,"la chancla voladora",1,600,"16:30") #creacion manual del objeto sala, solo para pruevas
# print(c)
#c.verReservas()
# #print(c.verReservas())
# #c.modificarSala()


# consul="SELECT * FROM Sala;"
# a=Sala.BDD.consulta(p,consul)
# Sala.BDD.cerrar(p)
#lS=Salas.Salas()
#print(lS)
#lS.buscarSala()
#print(lS)
#lS.agregarSala()
#lS.modificar(5)
#lS.eliminarSala(4)
#BDD.generarDB()

#####ADMINISTRADOR---------------------------
ad=Administrador.Administrado()
#ad.crearSala()
#ad.verSalas()
#ad.modificaSala()
ad.modificarDescuentos()
#Prueba de Descuentos
# desc = Descuentos.Descuentos()

# desc.modificarDescuento()
# print(desc.devolverDescuentoDia(10))

#Cargando la base de datos
#conexion = BDD.crear_conexion()
#BDD.consulta(conexion,consulta_)
#BDD.cerrar(conexion)

#Agrego datos Descuentos
#consulta_ = "insert into Descuentos values ('1','20'),('2','15'),('3','20'),('4','15'),('5','10'),('6','10'),('7','10');"

#Agrego datos Sala
#consulta_ = "insert into Sala values (NULL,'3d','la chancla voladora','1','600','16:30','10'),(NULL,'2d','Pizza Warfare Z','1','200','7:00','100');"

#conexion = BDD.crear_conexion()
#BDD.consulta(conexion,consulta_)
#BDD.cerrar(conexion)


#Prueba Historial

#Agrego datos a Historial
#conexion = BDD.crear_conexion()
#consulta_ = "insert into Historial values (NULL,'123123123','Nombre','Apellido','0','Nombre Peli','3d','12/12/2022','18:00','300.00'),(NULL,'11231231','Joaquin','Qasda','1','Pelicula112','2d','04/11/2022','17:20','200.00');"
#BDD.consulta(conexion,consulta_)
#BDD.cerrar(conexion)


# histo = Historial.Historial()
# histo.validarTarjeta('111')
# id_Reserva= 0
# histo.buscarUsuario(id_Reserva)