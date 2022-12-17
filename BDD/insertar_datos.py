import sqlite3
from base_de_datos.BDD import crear_conexion 


def crear_datos(conexion,consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()


conexion= crear_conexion()
