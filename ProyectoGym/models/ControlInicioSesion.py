from flask import redirect
from models.consultas import inicio_sesion
from flask import session
from Util.Session import *
def validar_usuario(email, password):
    # En este ejemplo, se simula la validación con un diccionario    
    # Busca el usuario en la base de datos
    existeUsuario = inicio_sesion(email, password)
    if existeUsuario:
        return True
    else:
        return False
    #return existeUsuario
    
def inicio_sesion_prueba(email, password):
    if 'conectado' in session:
        print("Ya estaba conectado nea")
        return dataLoginSesion()
        #return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion())
    else:
        usuario = inicio_sesion(email, password)
        if usuario:
            # Crear datos de sesión, para poder acceder a estos datos en otras rutas 
            session['conectado']        = True
            session['cedula_usuario']   = usuario[0]
            session['tipo_usuario']     = usuario[6]
            session['nombre']           = usuario[1]
            session['apellido']         = usuario[2]
            #session['fechaNacimiento'] = usuario[3]
            session['email']            = usuario[5]
            session['estado']           = usuario[8]

            msg = "Ha iniciado sesión correctamente."
            return dataLoginSesion()
            #return render_template('public/dashboard/home.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion())                    
        else:
            msg = "Usuarios inexistente."
            return None
            #return render_template('public/modulo_login/index.html', msjAlert = msg, typeAlert=0)