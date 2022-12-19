
import sqlite3

def crear_conexion():
    conexion= sqlite3.connect("base_de_datos\cineDB.db")
    return conexion

def consulta(conexion,consulta):
	cursor= conexion.cursor()
	cursor.execute(consulta)
	datos = cursor.fetchall()
	conexion.commit()
	return datos


def cerrar(conexion):
	conexion.close()

def generarDB():
	conexion= sqlite3.connect("base_de_datos\cineDB.db")
	cursor= conexion.cursor()
	cmd=[("""CREATE TABLE IF NOT EXISTS Usuario (
	DNI INTEGER PRIMARY KEY,
	Nombre TEXT(30) NOT NULL,
	Apellido TEXT(30) NOT NULL,
	Super_Cliente BOOL NOT NULL,
<<<<<<< HEAD
	Contrasenia TEXT(30));"""),
=======
	Contrasenia TEXT(20) NOT NULL);"""),
>>>>>>> Gonza-branch
	("""CREATE TABLE IF NOT EXISTS Historial (
	UniqueID INTEGER PRIMARY KEY AUTOINCREMENT,
	documento INTEGER NOT NULL,
	Nombre TEXT(30) NOT NULL,
	Apellido TEXT(30) NOT NULL,
	Super_Cliente BOOL NOT NULL,
	pelicula TEXT (30) NOT NULL,
	formato TEXT (30) NOT NULL,
	fecha TEXT (30) NOT NULL,
	horario TEXT (10) NOT NULL,
	monto FLOAT NOT NULL);"""),
	("""CREATE TABLE IF NOT EXISTS Butacas (
	UniqueID INTEGER PRIMARY KEY,
	salaID INTEGER,
	estado INTEGER,
	FOREIGN KEY (salaID) REFERENCES Sala(id_sala),
	FOREIGN KEY (estado) REFERENCES Reserva(id_reserva));"""),
	("""CREATE TABLE IF NOT EXISTS Descuentos (
	dia INTEGER PRIMARY KEY,
	descuento FLOAT);"""),
	("""CREATE TABLE IF NOT EXISTS Reserva(
	id_reserva INTEGER PRIMARY KEY,
	monto FLOAT,
	sala INTEGER,
	id_usuario INTEGER,
	butaca BOOL,
	FOREIGN KEY (sala) REFERENCES Sala(id_sala),
	FOREIGN KEY (id_usuario) REFERENCES Usuario(DNI));"""),
	("""CREATE TABLE IF NOT EXISTS Sala(id_sala INTEGER PRIMARY KEY,
	formato TEXT NOT NULL,
	pelicula TEXT NOT NULL,
	descuento INTEGER NOT NULL,
	precio FLOTA NOT NULL,
	fecha TEXT NOT NULL,
	horario TEXT NOT NULL,
	nro_Butacas INTEGER NOT NULL,
	FOREIGN KEY (descuento) REFERENCES Descuentos(dia));"""),
	("""CREATE TABLE IF NOT EXISTS Metodos_de_pago (
	id INTEGER PRIMARY KEY,
	opcionesdepago TEXT(100));""")]
	for c in cmd:
		#print(c)
		#print("---------------")
		cursor.execute(c)

	conexion.commit()
	conexion.close()

<<<<<<< HEAD
# generarDB()
=======

generarDB()
>>>>>>> Gonza-branch
