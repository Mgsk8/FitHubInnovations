from consultas import consultarFila

# Supongamos que tienes una tabla llamada "usuarios" con campos "id", "nombre" y "edad"
# y quieres consultar la fila donde el campo "id" sea igual a 1.

# Llamada a la función consultarFila
resultado = consultarFila("usuario", "cedula_usuario", "1")

# Verificar el resultado
if resultado:
    print("Fila encontrada:", resultado)
    # Dividir cada dato de la fila
    print("ID:", resultado[0])
    
    
else:
    print("No se encontró ninguna fila.")
