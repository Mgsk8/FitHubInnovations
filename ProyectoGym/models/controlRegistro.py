from flask import redirect
from models.consultas import registro 


    

def registro_usuario(cedula, nombre, apellido, email, password):
    registro(cedula, nombre, apellido, email, password)
    