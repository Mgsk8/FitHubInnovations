from flask import Flask,render_template, request, redirect, url_for, session
from controllers.ControlInicioSesion import validar_usuario, inicio_sesion_prueba
from controllers.ControlOlvidarContraseña import validarCorreo, enviarCorreo
from controllers.consultas import *
from Util.Session import *
from controllers import ControlmodalUsuarios, controlRegistro


app = Flask(__name__)
clase_actual = ""

app.secret_key = '12345'

@app.route("/")
def Inicio_secion():
    global clase_actual
    clase_actual = "VistaInicioSesion.html"
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('cedula_usuario', None)
    session.pop('email', None)
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
    if 'conectado' in session:
        return render_template('administrador/VistaMenuInicioAdmin.html', dataLogin = dataLoginSesion())
    return redirect(url_for('Inicio_sesion'))

@app.route("/vista_admins_admin")
def vista_admins_admin():
    if 'conectado' in session:
        global clase_actual
        clase_actual = "vista_admins_admin"
        tipo = "Administrador"
        usuarios = consultarMatriz('usuario')  
        usuario_admin = [usuario for usuario in usuarios if usuario[6] == tipo]
        return render_template('administrador/VistaAdministradoresAdmin.html', dataLogin = dataLoginSesion(),usuarios = usuario_admin)
    return redirect(url_for('vista_menu_inicio_admin'))
@app.route("/vista_sup_admin")
def vista_sup_admin():
    if 'conectado' in session:
        global clase_actual
        clase_actual = "vista_sup_admin"
        tipo = "Supervisor"
        usuarios = consultarMatriz('usuario')  
        usuario_super = [usuario for usuario in usuarios if usuario[6] == tipo]
        return render_template('administrador/VistaSupervisoresAdmin.html', dataLogin = dataLoginSesion(), usuarios = usuario_super)
    return redirect(url_for('vista_menu_inicio_admin'))
@app.route("/vista_rec_admin")
def vista_rec_admin():
    if 'conectado' in session:
        global clase_actual
        clase_actual = "vista_rec_admin"
        tipo = "Recepcionista"
        usuarios = consultarMatriz('usuario')  
        usuario_recep = [usuario for usuario in usuarios if usuario[6] == tipo]
        return render_template('administrador/VistaRecepcionistasAdmin.html', dataLogin = dataLoginSesion(), usuarios = usuario_recep)
    return redirect(url_for('vista_menu_inicio_admin'))
@app.route("/vista_ent_admin")
def vista_ent_admin():
    if 'conectado' in session:
        global clase_actual
        clase_actual = "vista_ent_admin"
        tipo = "Entrenador"
        usuarios = consultarMatriz('usuario')  
        usuario_entre = [usuario for usuario in usuarios if usuario[6] == tipo]
        return render_template('administrador/VistaEntrenadoresAdmin.html', dataLogin = dataLoginSesion(), usuarios = usuario_entre)
    return redirect(url_for('vista_menu_inicio_admin'))
@app.route("/vista_cli_admin")
def vista_cli_admin():
    if 'conectado' in session:
        global clase_actual
        clase_actual = "vista_cli_admin"
        tipo = "Cliente"
        usuarios = consultarMatriz('usuario')  
        usuario_cliente = [usuario for usuario in usuarios if usuario[6] == tipo]
        return render_template('administrador/VistaClientesAdmin.html', dataLogin = dataLoginSesion(), usuarios = usuario_cliente)
    return redirect(url_for('vista_menu_inicio_admin'))

@app.route("/control_menu_inicio", methods=["POST"])
def controlMenuInicio():
    email = request.form["email"]
    password = request.form["password"]
    #validar = validar_usuario(email, password)
    dataLogin = inicio_sesion_prueba(email, password)
    if dataLogin:
        return render_template('administrador/VistaMenuInicioAdmin.html', dataLogin = dataLoginSesion())
        #return redirect(url_for('vista_menu_inicio_admin'))
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
    telefono = request.form["telefono"]
    fecha = request.form["fecha_nacimiento"]
    password = request.form["password"]
    tipo_usuario = "Cliente"
    estado = "Inactivo"
    if password == request.form["confirmpassword"]:
        ControlmodalUsuarios.registro_usuario(cedula, nombre, apellido, telefono, fecha, email, tipo_usuario, estado, password)
    else:
        return register()
    return redirect(url_for('Inicio_secion'))
    
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
@app.route('/cerrar_sesion')
def cerrar_sesion():
    msgClose = ''
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('cedula_usuario', None)
    session.pop('email', None)
    msgClose ="La sesión fue cerrada correctamente"
    return render_template('VistaInicioSesion.html' , msjAlert = msgClose, typeAlert=1)

@app.route('/eliminar_Usuario', methods = ["POST"])
def eliminar_usuario():
    global clase_actual
    id_usuario = request.form["itemId"]
    ControlmodalUsuarios.desactivar_usuario(id_usuario)
    return redirect(url_for(clase_actual))

@app.route('/editarusuario', methods = ["POST"])
def editar_usuario():
    global clase_actual
    id_usuario = request.form["editItemId"]
    nombre = request.form["editItemName"]
    apellido = request.form["editItemApe"]
    telefono = request.form["editItemtelefono"]
    fecha = request.form["editItemFecha"]
    email = request.form["editItemEmail"]
    ControlmodalUsuarios.editar_usuario(id_usuario,nombre,apellido,telefono,fecha,email)
    return redirect(url_for(clase_actual))

@app.route('/registro_modal', methods = ["POST"])
def registrar_usuario():
    global clase_actual
    id_usuario = request.form["RegisItemCedula"]
    nombre = request.form["RegisItemName"]
    apellido = request.form["RegisItemApellido"]
    telefono = request.form["RegisItemTelefono"]
    fecha = request.form["RegisItemFecha"]
    email = request.form["RegisItemEmail"]
    tipoUsuario = request.form["RegisItemTipoUsuario"]
    estado = "Activo"
    contra = request.form["RegisItemContra"]
    ControlmodalUsuarios.registro_usuario(id_usuario,nombre,apellido,telefono,fecha,email, tipoUsuario, estado, contra)
    return redirect(url_for(clase_actual))

@app.route("/vista_membresia_g")
def vista_membresia_g():
    if 'conectado' in session:
        global clase_actual
        clase_actual = "vista_membresia_g"
        membresias = consultarMatriz('membresia_cliente')  
        membresia_cliente = [membresia for membresia in membresias]
        return render_template('administrador/Vistamembresias.html',dataLogin = dataLoginSesion(), membresias = membresia_cliente)
    return redirect(url_for('vista_menu_inicio_admin'))

@app.route('/registro_membresia', methods = ["POST"])
def registrar_membresia():
    global clase_actual
    fecha_inicio = request.form["RegisItemDate"]
    cedula_cliente = request.form["RegisItemCedulaC"]
    Tipo_membresia = request.form["RegisItemTipoUsuario"]
    controlRegistro.registro_membresia(fecha_inicio,Tipo_membresia,cedula_cliente)
    return redirect(url_for(clase_actual))

@app.route('/editarmembresia', methods = ["POST"])
def editarmembresia():
    global clase_actual
    id_membresia = request.form["editItemId"]
    fecha_inicio = request.form["editItemDate"]
    cedula_cliente = request.form["editItemCedula"]
    tipo_membresia = request.form["editItemTipomembresia"]
    controlRegistro.editar_membresia(id_membresia,fecha_inicio,tipo_membresia,cedula_cliente)
    return redirect(url_for(clase_actual))

@app.route('/eliminar_membresia', methods = ["POST"])
def eliminar_membresia():
    global clase_actual
    id_membresia = request.form["itemId"]
    controlRegistro.desactivar_membresia(id_membresia)
    return redirect(url_for(clase_actual))
app.run(host='0.0.0.0',port=81, debug=True)