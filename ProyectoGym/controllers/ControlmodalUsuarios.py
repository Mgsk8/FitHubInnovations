from flask import redirect, url_for
from controllers import consultas

def desactivar_usuario(id_usuario):
    datos = []
    estado = "estado = 'Inactivo'"
    datos.append(estado)
    condicion = f"cedula_usuario = {id_usuario}" 
    consultas.actualizarFila('usuario',datos,condicion)

def activar_usuario(id_usuario):
    datos = []
    estado = "estado = 'Activo'"
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
    if tipo_usuario == 1 or tipo_usuario == "Administrador" or tipo_usuario == "1":
        print("")
    if tipo_usuario == 5 or tipo_usuario == "Cliente" or tipo_usuario == "5":
        registro_cli(cedula)
def registro_admin():
    return 0

def registro_sup():
    return 0

def registro_rec():
    return 0

def registro_ent():
    return 0

def registro_cli(cedula):
    consultas.registro_cliente(cedula, "", "no", "")