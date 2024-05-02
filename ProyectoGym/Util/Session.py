from flask import session
from database import * 

#https://pynative.com/python-mysql-database-connection/
#https://pynative.com/python-mysql-select-query-to-fetch-data/


#creando una funcion y dentro de la misma una data (un diccionario)
#con valores del usuario ya logueado
def dataLoginSesion():
    inforLogin = {
        "cedula_usuario"             :session['cedula_usuario'],
        "tipo_usuario"           :session['tipo_usuario'],
        "nombre"              :session['nombre'],
        "apellido"            :session['apellido'],
        #"fecha_nacimiento"                :session['fecha_nacimiento'],
        "email"          :session['email'],
        "estado"                      :session['estado']
    }
    return inforLogin

def dataPerfilUsuario():
    conexion_MySQLdb = conectar()
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    cedulaUsuario         = session['cedula_usuario']
    
    querySQL  = ("SELECT * FROM usuario WHERE cedula_usuario='%s'" % (cedulaUsuario,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return datosUsuario


