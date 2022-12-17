from base_de_datos import BDD
from clases import Sala
from clases import Salas
from clases import Historial
from clases import Descuentos
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

# #print(c)

# #c=Sala.Sala(0,"7d",10,"la chancla voladora",1,600,"16:30",3) #creacion manual del objeto sala, solo para pruevas
# #print(c)
# #c.verReservas()
# #print(c.verReservas())
# #c.modificarSala()


# consul="SELECT * FROM Sala;"
# a=Sala.BDD.consulta(p,consul)
# Sala.BDD.cerrar(p)
# lS=Salas.Salas(a)
# print(lS)




#Prueba de Descuentos


# desc = Descuentos.Descuentos()

# desc.modificarDescuento()
# print(desc.devolverDescuentoDia(10))

#Cargando la base de datos
# conexion = BDD.crear_conexion()
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)

#Agrego datos Descuentos
# consulta_ = "insert into Descuentos values ('1','20'),('2','15'),('3','20'),('4','15'),('5','10'),('6','10'),('7','10');"

#Agrego datos a Usuario
# conexion = BDD.crear_conexion()
# # consulta_ = "insert into Usuario values ('123123123','Nombre','Apellido','0'),('11231231', 'Joaquin', 'Qasda', '1');"
# consulta_ = "UPDATE Historial SET fecha = '28/06/2023' WHERE UniqueID = 6"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)



#Prueba Historial

#Agrego datos a Historial
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Historial values ('2','123123123','Nombre','Apellido','0','Nombre Peli2','2d','22/12/2022','18:00','200.00'),('3','123123123','Nombre','Apellido','0','Nombre Peli3','3d','30/12/2022','18:00','300.00'),('4','123123123','Nombre','Apellido','0','Nombre Pel4','3d','07/02/2022','18:00','300.00'),('5','123123123','Nombre','Apellido','0','Nombre Peli5','3d','24/04/2022','18:00','300.00'),('6','123123123','Nombre','Apellido','0','Nombre Peli6','3d','28/06/2022','18:00','300.00');"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)


histo = Historial.Historial()
histo.validarTarjeta('123123123')
# id_Reserva= 0
# histo.buscarUsuario(id_Reserva)