import sqlite3

from base_de_datos.BDD import crear_conexion


def select_producto(conexion):
    #conexion = crear_conexion()
    cursor= conexion.cursor()
    cursor.execute("SELECT id_sala, formato, pelicula, precio FROM Sala ")
    filas = cursor.fetchall()
    return filas

def select_producto_by_id(conexion,consulta):
    cursor= conexion.cursor()
    cursor.execute(consulta)
    fila= cursor.fetchall()
    return fila