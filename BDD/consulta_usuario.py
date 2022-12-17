import sqlite3
from base_de_datos.BDD import crear_conexion


def validar_usuario(conexion,consulta):
    cursor=conexion.cursor()
    cursor.execute(consulta)
    filas = cursor.fetchall()
    if len(filas)>0:
        return True
    else: 
        return False