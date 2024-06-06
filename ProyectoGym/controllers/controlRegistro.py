from datetime import datetime, timedelta
from flask import redirect
from controllers.consultas import registro_membresiag, actualizarFila


    
def registro_membresia(fecha_inicio, tipo_membresia, id_cliente):
    fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin_dt = fecha_inicio_dt + timedelta(days=30)
    fecha_fin = fecha_fin_dt.strftime('%Y-%m-%d')
    registro_membresiag(fecha_inicio,fecha_fin,tipo_membresia,id_cliente)

def editar_membresia(id_membresia,fecha_inicio,tipo_membresia,cedula_cliente):
    datos = []
    condicion = f"id_membresia = {id_membresia}"
    fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin_dt = fecha_inicio_dt + timedelta(days=30)
    fecha_inicio_sql = f"fecha_inicio = '{fecha_inicio_dt.strftime('%Y-%m-%d')}'"
    fecha_fin_sql = f"fecha_fin = '{fecha_fin_dt.strftime('%Y-%m-%d')}'"
    tipo_membresia = f"tipo_membresia = {tipo_membresia}"
    id_cliente = f"id_cliente = '{cedula_cliente}'"
    datos.append(fecha_inicio_sql)
    datos.append(fecha_fin_sql)
    datos.append(tipo_membresia)
    datos.append(id_cliente)
    actualizarFila('membresia_cliente',datos,condicion)

def desactivar_membresia(id_membresia):
    datos = []
    estado = "estado = 'Inactivo'"
    datos.append(estado)
    condicion = f"id_membresia = {id_membresia}" 
    actualizarFila('membresia_cliente',datos,condicion)