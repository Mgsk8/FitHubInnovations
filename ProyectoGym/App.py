from flask import Flask,render_template, request, redirect, url_for, session
from models.ControlInicioSesion import validar_usuario
from models.controlRegistro import registro_usuario
from models.ControlOlvidarContraseña import validarCorreo, enviarCorreo
from models.consultas import *


app = Flask(__name__)

app.secret_key = '12345'

@app.route("/")
def Inicio_secion():
    return render_template('VistaInicioSesion.html')
@app.route("/register")
def register():
    return render_template('Registrarse.html')

@app.route("/password_reset")
def reset_password():
    return render_template('OlvidarContraseña.html')

@app.route("/vista_menu_inicio")
def vista_menu_inicio():
    return render_template('VistaMenuInicio.html')

@app.route("/vista_menu_inicio_admin")
def vista_menu_inicio_admin():
    return render_template('administrador/VistaMenuInicioAdmin.html')

@app.route("/vista_admins_admin")
def vista_admins_admin():
    return render_template('administrador/VistaAdministradoresAdmin.html')

@app.route("/control_menu_inicio", methods=["POST"])
def controlMenuInicio():
    email = request.form["email"]
    password = request.form["password"]
    validar = validar_usuario(email, password)
    if validar:
        return redirect(url_for('vista_menu_inicio'))
    else:
        return redirect(url_for('Inicio_secion'))
    
@app.route("/Control_Cambio_Contraseña", methods=["POST"])
def controlCambioContraseña():
    email = request.form["email"]
    validar = validarCorreo(email)
    if validar:
        session['email'] = email
        enviarCorreo(email)
        return render_template('MsjCambioPass.html')
    else:
        return redirect(url_for('Inicio_secion'))
    
@app.route("/controlregistro", methods=["POST"])
def controlregistro():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    cedula = request.form["cedula_usuario"]
    email = request.form["email"]
    password = request.form["password"]
    registro_usuario(cedula, nombre, apellido, email, password)
    print (nombre, apellido, cedula, email, password)
    return register()
    
@app.route("/cambio")
def cambio():
    return render_template('CambioContraseña.html')

@app.route("/restablecerPassword", methods=["POST"])
def restablecerContraseña():
    email = session.get('email', '')
    print(email)
    password = request.form["password"]
    confirmPassword = request.form["confirmPassword"]
    if password == confirmPassword:
        if verificarContraseña(password, email):
            error_message = "la contraseña ya existe. Por favor Intentalo de nuevo"
            return render_template('cambioContraseña.html',errorVerificar = error_message)
        else:
            actualizarContraseña(password, email)
            return redirect(url_for('Inicio_secion'))
    else:
        error_message = "Las contraseñas no coinciden. Por favor Intentalo de nuevo"
        return render_template('cambioContraseña.html',error = error_message)

app.run(host='0.0.0.0',port=81, debug=True)