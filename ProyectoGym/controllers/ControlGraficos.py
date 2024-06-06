from controllers import consultas

def conteo_tipo_usuario(tabla, condicional):
    condicion = f"tipo_usuario = '{condicional}'"
    print(condicion)
    conteo = consultas.consultarConteo(tabla, condicion)
    print(condicional, " = ", conteo)
    return conteo

def conteo_usuario_activos(tabla, condicional):
    condicion = f"estado = '{condicional}'"
    print(condicion)
    conteo = consultas.consultarConteo(tabla, condicion)
    print(condicional, " = ", conteo)
    return conteo

def conteo_tipo_membresias(tabla, condicional):
    condicion = f"tipo_membresia = '{condicional}'"
    print(condicion)
    conteo = consultas.consultarConteo(tabla, condicion)
    print(condicional, " = ", conteo)
    return conteo

def conteo_membresias_activas(tabla, condicional):
    condicion = f"estado = '{condicional}'"
    print(condicion)
    conteo = consultas.consultarConteo(tabla, condicion)
    print(condicional, " = ", conteo)
    return conteo