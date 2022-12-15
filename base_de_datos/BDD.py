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
	DNI INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(30) NOT NULL,
	Apellido TEXT(30) NOT NULL,
	Super_Cliente BOOL NOT NULL,
	reserva INTEGER,
	FOREIGN KEY (reserva) REFERENCES Reserva(id_reserva));"""),
	("""CREATE TABLE IF NOT EXISTS Historial (
	UniqueID INTEGER PRIMARY KEY AUTOINCREMENT,
	salaID INTEGER,
	reservaID INTEGER,
	FOREIGN KEY (salaID) REFERENCES Sala(id_sala),
	FOREIGN KEY (reservaID) REFERENCES Reserva(id_reserva));"""),
	("""CREATE TABLE IF NOT EXISTS Butacas (
	UniqueID INTEGER PRIMARY KEY AUTOINCREMENT,
	salaID INTEGER,
	estado BOOL,
	FOREIGN KEY (salaID) REFERENCES Sala(id_sala),
	FOREIGN KEY (estado) REFERENCES Usuario(DNI));"""),
	("""CREATE TABLE IF NOT EXISTS Descuentos (
	dia INTEGER PRIMARY KEY ,
	descuento FLOAT);"""),
	("""CREATE TABLE IF NOT EXISTS Reserva(
	id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
	sala INTEGER,
	pagoEfectuado INTEGER,
	FOREIGN KEY (sala) REFERENCES Sala(id_sala),
	FOREIGN KEY (pagoEfectuado) REFERENCES Metodos_de_pago(id));"""),
	("""CREATE TABLE IF NOT EXISTS Sala(id_sala INTEGER PRIMARY KEY AUTOINCREMENT,
	formato TEXT NOT NULL,
	pelicula TEXT NOT NULL,
	descuento INTEGER NOT NULL,
	precio FLOTA NOT NULL,
	horario TEXT NOT NULL,
	nro_Butacas INTEGER NOT NULL,
	FOREIGN KEY (descuento) REFERENCES Descuentos(dia));"""),
	("""CREATE TABLE IF NOT EXISTS Metodos_de_pago (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	opcionesdepago TEXT(100));""")]
	for c in cmd:
		#print(c)
		#print("---------------")
		cursor.execute(c)

	conexion.commit()
	conexion.close()

#generarDB()