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

conexion = crear_conexion()
#consulta(conexion, "INSERT INTO Usuario VALUES ('111','Ramiro', 'Patron','0','1');")
#consulta(conexion, "INSERT INTO Reserva VALUES ('1','0','1');")