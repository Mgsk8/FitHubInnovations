from flask import redirect
from models.consultas import inicio_sesion
def validar_usuario(email, password):
    # En este ejemplo, se simula la validación con un diccionario    
    # Busca el usuario en la base de datos
    existeUsuario = inicio_sesion(email, password)
    if existeUsuario:
        return True
    else:
        return False
    #return existeUsuario

def iniciar_sesion(email, password):
    #email = request.form["email"]
    #password = request.form["password"]
    if validar_usuario(email, password):
        return redirect("/vista_menu_inicio")
    else:
        return redirect("/")

# Se exporta la función para ser utilizada en la vista
#iniciar_sesion = iniciar_sesion()
