import sqlite3

def crear_conexion():
    conexion= sqlite3.connect("cineDB.db")
    return conexion

def consulta(conexion,consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()

def cerrar(conexion):
	conexion.close()

def generarDB():
	conexion= sqlite3.connect("cineDB.db")
	cursor= conexion.cursor()
	cmd=[("""CREATE TABLE IF NOT EXISTS Usuario (
	DNI INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(30) NOT NULL,
	Apellido TEXT(30) NOT NULL,
	Super_Cliente BOOL NOT NULL,
	Historial INTEGER,
	FOREIGN KEY (Historial) REFERENCES Historial(UniqueID));"""),
	("""CREATE TABLE IF NOT EXISTS Historial (
	UniqueID INTEGER PRIMARY KEY AUTOINCREMENT,
	salaID INTEGER,
	reservaID INTEGER,
	FOREIGN KEY (salaID) REFERENCES Sala(id_sala),
	FOREIGN KEY (reservaID) REFERENCES Reserva(ID));"""),
	("""CREATE TABLE IF NOT EXISTS Butacas (
	UniqueID INTEGER PRIMARY KEY AUTOINCREMENT,
	estado BOOL,
	FOREIGN KEY (estado) REFERENCES Usuario(DNI));"""),
	("""CREATE TABLE IF NOT EXISTS Descuentos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	listaDias TEXT(100));"""),
	("""CREATE TABLE IF NOT EXISTS Reserva(
	id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
	usuario INTEGER,
	sala INTEGER,
	pagoEfectuado INTEGER,
	FOREIGN KEY (usuario) REFERENCES Usuario(DNI),
	FOREIGN KEY (sala) REFERENCES Sala(id_sala),
	FOREIGN KEY (pagoEfectuado) REFERENCES Metodos_de_pagos(id));"""),
	("""CREATE TABLE IF NOT EXISTS Sala(id_sala INTEGER PRIMARY KEY AUTOINCREMENT,
	butacas INTEGER NOT NULL,
	formato TEXT NOT NULL,
	pelicula TEXT NOT NULL,
	descuento FLOAT NOT NULL,
	horario TEXT NOT NULL,
	nro_Butacas INTEGER NOT NULL,
	FOREIGN KEY (butacas) REFERENCES Butacas(UniqueID),
	FOREIGN KEY (descuento) REFERENCES Descuentos(id));"""),
	("""CREATE TABLE IF NOT EXISTS Metodos_de_pago (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	opcionesdepago TEXT(100));""")]
	for c in cmd:
		#print(c)
		#print("---------------")
		cursor.execute(c)

	conexion.commit()
	conexion.close()

generarDB()