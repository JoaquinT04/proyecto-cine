from base_de_datos import BDD
from clases import Sala
from clases import Salas
from clases import Historial
from clases import Descuentos
from clases import Butacas

#Prueba Sala/Salas

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
# for i in range(1,8):
# 	print(desc.devolverDescuentoDia(i))
	

#Cargando la base de datos
# Agrego datos Descuentos
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Descuentos values ('1','20'),('2','15'),('3','20'),('4','15'),('5','10'),('6','10'),('7','10');"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)






#Prueba Historial

#Agrego datos a Historial
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Historial values ('0','123123123','Nombre','Apellido','0','Nombre Peli','3d','12/12/2022','18:00','300.00'),('1','11231231','Joaquin','Qasda','1','Pelicula112','2d','04/11/2022','17:20','200.00');"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)


# histo = Historial.Historial()
# histo.validarTarjeta('111')
# id_Reserva= 0
# histo.buscarUsuario(id_Reserva)

#Prueba Butacas
#Agrego contenido a Butacas
# butacas = Butacas.Butacas()
lS=Salas.Salas()
# print(lS)
lS.agregarSala()
# butacas.crearButaca(1)
# butacas.modificarButaca(3,"NULL")
# butacas.modificarButaca(4,3412421)
# butacas.modificarButaca(4,"NULL")
# butacas.modificarButacaSala(1,"NULL")
# butacas.eliminarButacasSala(1)
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Butacas values ;"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)



#Agrego contenido a Sala

# conexion = BDD.crear_conexion()
# consulta_ = "insert into Sala values ;"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)