from clases import Salas
from clases import Descuentos
class Administrado():
	def __init__(self,contraseña = None):
		self.__usuario_id = None
		self.__contraseña = None
	
	@property
	def usuario_id (self):
		return self.__usuario_id
	
	@property 
	def contraseña(self,contraseña):
		self.__contraseña = contraseña
	
	def usuarios():
		pass

	def historial_de_salas():
		pass

	def crearSala(self):
		lS=Salas.Salas()
		lS.agregarSala()
	
	def modificaSala(self):
		lS=Salas.Salas()
		print(lS)
		op=input("ingrese id de la sala a modificar")
		lS.modificar(op)

	def verSalas(sef):
		lS=Salas.Salas()
		print(lS)

	def modificarDescuentos(self):
		desc=Descuentos.Descuentos()
		desc.modificarDescuento()

	def ver_la_disponibilidad_de_butacas(self,idSala):

		pass

	def gestion_de_venta_y_descuentos():
		pass

	def darTarjeta():
		pass