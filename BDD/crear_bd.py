import sqlite3


def crear_conexion(db_name):
    conexion= sqlite3.connect(db_name)
    return conexion


#crear_conexion("cm7\Supermark\BDD\Supermarket.db")