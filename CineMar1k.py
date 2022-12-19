from base_de_datos import BDD
from clases import Sala
from clases import Salas
from clases import Historial
from clases import Descuentos
from clases import Butacas
from clases import Reservas
from clases.Usuario import Usuario
from clases.Historial import Historial
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


#Agrego datos a Usuario
# conexion = BDD.crear_conexion()
# # consulta_ = "insert into Usuario values ('123123123','Nombre','Apellido','0'),('11231231', 'Joaquin', 'Qasda', '1');"
# consulta_ = "UPDATE Historial SET fecha = '28/06/2023' WHERE UniqueID = 6"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)

# #Agrego datos a Sala
# conexion = BDD.crear_conexion()
# consulta_ = "INSERT INTO Sala VALUES ('4', '2d', 'Pelicula 1', '0', '300', '18:00', '50');"
# #consulta_ = "DELETE FROM Sala WHERE id_sala = 4"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)

#Prueba Historial

#Agrego datos a Historial
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Historial values ('2','123123123','Nombre','Apellido','0','Nombre Peli2','2d','22/12/2022','18:00','200.00'),('3','123123123','Nombre','Apellido','0','Nombre Peli3','3d','30/12/2022','18:00','300.00'),('4','123123123','Nombre','Apellido','0','Nombre Pel4','3d','07/02/2022','18:00','300.00'),('5','123123123','Nombre','Apellido','0','Nombre Peli5','3d','24/04/2022','18:00','300.00'),('6','123123123','Nombre','Apellido','0','Nombre Peli6','3d','28/06/2022','18:00','300.00');"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)


#histo = Historial.Historial()
#histo.validarTarjeta('123123123')
# id_Reserva= 0
# histo.buscarUsuario(id_Reserva)

<<<<<<< HEAD
#Prueba Butacas
#Agrego contenido a Butacas
# butacas = Butacas.Butacas()
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
# lS=Salas.Salas()
# # print(lS)
# lS.agregarSala()
# lS.eliminarSala(2)
# lS.modificar(2)
# lS.buscarSala()
# print(lS)
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Sala values ;"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)


#Agrego contenido a la tabla usuario
# conexion = BDD.crear_conexion()
# consulta_ = "insert into Usuario values('123123','Nombre','Apellido','0','contrasenia') ;"
# BDD.consulta(conexion,consulta_)
# BDD.cerrar(conexion)

#Prueba de Reservas
# reserva = Reservas.Reservas()
# reserva.agregarReserva(2,123123)
# reserva.eliminarReserva(2) 
# print(reserva.buscarXUsuario(123123))

#Prueba de Usuario
# user = Usuario()
# # user.crearUsuario(321321,"Joaquin","Otro Apellido","MiContrasenia")
# # user.crearUsuario(512312412,"Joaquin","Otro Apellido","MiContrasenia")
# # user.eliminarUsuario(512312412,"MiContrasenia")
# # user.modificarUsuario(321321)
# # print(user.verUsuarios())
# print(user.ingresar(123123,"contrasenia"))
# # print(user)
# # user.borrarReserva()
# # print(user.verReserva())
# # print(user.verSalas())
# print(user.pedirTarjeta())


#Prueba Historial
# historial = Historial()
# historial.agregarHistorial(1)
# print(historial.buscarUsuario(321321))
=======
import tkinter 

from tkinter import ttk, Button, Frame, messagebox, Tk
from login import Login
from registro import CrearCuenta

class App(Frame):
    
    def __init__(self, root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        
        
    def crear_widgets(self):
        self.button= Button(self)
        self.button["text"] = "Login"
        self.button["command"] = self.abrir_login 
        self.button.grid(padx=50, pady=15)
        
        self.button1= Button(self)
        self.button1["text"] = "Registro"
        self.button1["command"] = self.abrir_registro 
        self.button1.grid(padx=50, pady=15)
        
        
    def abrir_login(self):
        Login(self.root)
        
    
    def abrir_registro(self):
       CrearCuenta(self.root)
        

root=Tk()
app= App(root)
app.mainloop()
>>>>>>> Gonza-branch
