import database as database

def inicio_sesion(email, password):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = f"SELECT * FROM usuario WHERE email = %s AND password = %s;"
            cursor.execute(sql, (email, password))
            usuario = cursor.fetchone()
            if usuario is not None:
                return True
            return False
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            # Registrar el error en un archivo o sistema de monitoreo
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def registro(cedula, nombre, apellido, email, password):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuario (cedula_usuario, nombre, apellido, email, password) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(sql, (cedula, nombre, apellido, email, password))
            conexion.commit()  # Agregamos el commit para confirmar los cambios
            print("Usuario registrado exitosamente.")
            return True
        except Exception as ex:
            print(f"Error al crear usuario: {ex}")
            # NO SE PUDO REGISTRAR USUARIO
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)
    else:
        print("Error de conexión a la base de datos.")