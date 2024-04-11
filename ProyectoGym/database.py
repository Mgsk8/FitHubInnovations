import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            user='root', 
            password = '',
            host = 'localhost', 
            database='fit_hub_innovations',
            port ='3306')
        if conexion.is_connected():
            print("conexion exitosa.")
            infoserver = conexion.get_server_info()
            print("informacion del servidor:", infoserver)
            return conexion
    except Error as ex:
        print("Error durante la conexion:", ex)
        return None

def desconectar(conexion):
    try:
        if conexion.is_connected():
            conexion.close()
            print("Conexion cerrada correctamente.")
    except Error as ex:
        print("Error al cerrar la conexion:", ex)
