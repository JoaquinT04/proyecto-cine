from base_de_datos import BDD
import os

class myError(Exception):
	def __init__(self, msj) :
		self.__msj = msj
	
	@property
	def msj(self):
		return self.__msj

class Descuentos:
	def __init__(self):
		self.__dia = None
		self.__descuento = None
	
	@property
	def id(self):
		return self.__id
	
	@property
	def dia(self):
		return self.__dia
	
	@dia.setter
	def dia(self,dia):
		self.__dia = dia
	
	#Funcion privada para verificar que el dia ingresado ya sea por parametro o por consola sea valido
	def __validarDia(self,dia = None):
		while True:
			try:
				if dia == None:
					dia = int(input("Ingrese un dia: "))
				else: 
					#Para lanzar error ValueError si es un caracter
					dia =int(dia)
				if dia>7 or dia<1:
					raise myError("Ingreso un dia no valido!")
				break
			except myError as err:
				print(err.msj)
				input()
				os.system("cls")  
				dia = input("Ingrese un dia: ")
			except ValueError :
				print("No se pueden ingresar letras o caracteres!")
				input()
				os.system("cls")  
				dia = input("Ingrese un dia: ")
		return dia
	
	#Funcion privada para verificar que el descuento ingresado ya sea por parametro o por consola sea valido
	def __validarDescuento(self,nuevoDesc = None):
		while True:
			try:
				if nuevoDesc == None:
					nuevoDesc = float(input("Ingrese un nuevo descuento: "))
				else:
					nuevoDesc = float(nuevoDesc)
				if nuevoDesc<0:
					raise myError("No se puede ingresar un valor negativo! ")
				break
			except myError as err:
				print(err.msj)
				input()
				nuevoDesc = input("Ingrese un nuevo descuento: ")
				os.system("cls")  
			except ValueError :
				print("No se pueden ingresar letras o caracteres!")
				input()
				nuevoDesc = input("Ingrese un nuevo descuento: ")
				os.system("cls")  
		return nuevoDesc

	def modificarDescuento(self):

		#Verifico que se ingrese un número positivo para el dia
		dia = self.__validarDia()
		#Verifico que se ingrese un número positivo para el descuento
		nuevoDesc = self.__validarDescuento()
		
		conexion = BDD.crear_conexion()
		# print(conexion)
		#Creo la consulta sql para modificar los datos de descuento del dia indicado
		consulta = f"update descuentos set descuento = {nuevoDesc} where dia = {dia};"
		BDD.consulta(conexion,consulta)
		BDD.cerrar(conexion)

	def devolverDescuentoDia(self,dia):
		#Verifico que se ingrese un número positivo para el dia
		dia = self.__validarDia(dia)
		print(dia)

		conexion = BDD.crear_conexion()
		consulta = f"select descuento from Descuentos where dia = {dia};"
		descuento = BDD.consulta(conexion,consulta)[0][0]
		BDD.cerrar(conexion)
		return descuento