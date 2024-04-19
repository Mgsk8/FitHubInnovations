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