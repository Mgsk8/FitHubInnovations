from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def Inicio_secion():
    return render_template('VistaInicioSesion.html')
@app.route("/register")
def register():
    return render_template('Registrarse.html')
app.run(port=81, debug=True)