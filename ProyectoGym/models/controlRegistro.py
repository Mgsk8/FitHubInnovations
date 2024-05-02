from flask import redirect
from models.consultas import registro 


    

def registro_usuario(cedula, nombre, apellido,telefono, fecha_nacimiento, email, tipo_usuario, estado, password):
    registro(cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password)
    