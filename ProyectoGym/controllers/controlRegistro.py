from flask import redirect
from controllers.consultas import registro 
from controllers.consultas import registro_cliente


    

def registro_usuario(cedula, nombre, apellido,telefono, fecha_nacimiento, email, tipo_usuario, estado, password):
    registro(cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password)
    registro_cli(cedula)
def registro_cli(cedula):
    registro_cliente(cedula, "", "no", "")