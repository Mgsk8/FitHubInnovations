from flask import Flask,render_template, request
from models.ControlInicioSesion import validar_usuario

app = Flask(__name__)

@app.route("/")
def Inicio_secion():
    return render_template('VistaInicioSesion.html')
@app.route("/register")
def register():
    return render_template('Registrarse.html')

@app.route("/vista_menu_inicio")
def vista_menu_inicio():
    return render_template('VistaMenuInicio.html')
@app.route("/vista_menu_inicio_admin")
def vista_menu_inicio_admin():
    return render_template('administrador/VistaMenuInicioAdmin.html')

@app.route("/vista_admins_admin")
def vista_admins_admin():
    return render_template('administrador/VistaAdministradoresAdmin.html')
@app.route("/vista_sup_admin")
def vista_sup_admin():
    return render_template('administrador/VistaSupervisoresAdmin.html')
@app.route("/vista_rec_admin")
def vista_rec_admin():
    return render_template('administrador/VistaRecepcionistasAdmin.html')
@app.route("/vista_ent_admin")
def vista_ent_admin():
    return render_template('administrador/VistaEntrenadoresAdmin.html')
@app.route("/vista_cli_admin")
def vista_cli_admin():
    return render_template('administrador/VistaClientesAdmin.html')
@app.route("/control_menu_inicio", methods=["POST"])
def controlMenuInicio():
    email = request.form["email"]
    password = request.form["password"]
    validar = validar_usuario(email, password)
    if validar:
        return vista_menu_inicio_admin()
    else:
        return Inicio_secion()
app.run(host='0.0.0.0',port=81, debug=True)