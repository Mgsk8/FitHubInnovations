import mysql.connector
from mysql.connector import Error

def conexion_bd():
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
            
    except Error as ex:
        print("Error durante la conexion:", ex)
    finally:
        if conexion.is_connected():
            conexion.close()#se cerro la conexion 
            print("la conexion a finalizado.")