from flask import redirect, url_for
from controllers import consultas

def desactivar_usuario(id_usuario):
    datos = []
    estado = "estado = 'Inactivo'"
    datos.append(estado)
    condicion = f"cedula_usuario = {id_usuario}" 
    consultas.actualizarFila('usuario',datos,condicion)

def editar_usuario(editItemId,editItemName,editItemApe,editItemtelefono,editItemFecha,editItemEmail):
    datos = []
    condicion = f"cedula_usuario = {editItemId}"
    nombre = f"nombre = '{editItemName}'"
    apellido = f"apellido = '{editItemApe}'"
    telefono = f"telefono = {editItemtelefono}"
    fecha = f"fecha_nacimiento = '{editItemFecha}'"
    email = f"email = '{editItemEmail}'"
    datos.append(nombre)
    datos.append(apellido)
    datos.append(telefono)
    datos.append(fecha)
    datos.append(email)
    consultas.actualizarFila('usuario',datos,condicion)

def registro_usuario(cedula, nombre, apellido,telefono, fecha_nacimiento, email, tipo_usuario, estado, password):
    consultas.registro(cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password)