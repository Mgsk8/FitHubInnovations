import database as database
def inicio_sesion(email, password):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT * FROM usuario WHERE email = %s AND password = %s;"
            cursor.execute(sql, (email, password))
            usuario = cursor.fetchone()
            print(usuario[0], usuario[1], usuario[2])
            print("Hola")
            return usuario
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            # Registrar el error en un archivo o sistema de monitoreo
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def consultarCorreo(email):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = f"SELECT email FROM usuario WHERE email = %s;"
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()
            if usuario is not None:
                return True
            else:
                return False
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def actualizarContraseña(password, email):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = f"UPDATE usuario SET password = %s WHERE email = %s;"
            cursor.execute(sql, (password,email))
            conexion.commit()
            print("contraseña actualizada correctamente.")
        except Exception as ex:
            print(f"Error al ejecutar update: {ex}")
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def verificarContraseña(password, email):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = f"SELECT password FROM usuario WHERE email = %s and password = %s;"
            cursor.execute(sql, (email, password))
            usuario = cursor.fetchone()
            if usuario is not None:
                return True
            else:
                return False
            
        except Exception as ex:
            print(f"Error al ejecutar update: {ex}")
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

def consultarFila(tabla, campo, valor ):
    conexion = database.conectar()
    fila = []
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT * FROM {} WHERE {} = %s;".format(tabla,campo)
            cursor.execute(sql, (valor,))
            resultados = cursor.fetchone()
            if resultados:
                fila = list(resultados)
                print("Datos de la fila: ", fila)
                return fila
            else:
                print("no se encontraron resultados a la consulta.")
                return False
        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def actualizarFila(tabla, datos, condicion):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = f"UPDATE {tabla} SET "
            for dato in range(0,len(datos)):
                sql += f"{datos[dato]}"
                if dato < len(datos) - 1:
                    sql += ", "
            sql += f" WHERE {condicion}"
            cursor.execute(sql)
            conexion.commit()
            if cursor.rowcount > 0:
                print("datos actualizados correctamente")
            else:
                print("datos no actualizados")
        except Exception as ex:
            print(f"Error al actualizar: {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def consultarMatriz(tabla):
    conexion = database.conectar()
   
    matriz = []
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT * FROM {} ;"
            cursor.execute(sql.format(tabla))
            resultados = cursor.fetchall()
            if resultados is not None:
                for fila in resultados:
                    matriz.append(fila)
                return matriz
            else:
                print("no se encontraron resultados a la consulta.")
                False

        except Exception as ex:
            print(f"Error al ejecutar la consulta: {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

def delete(tabla, campo, dato):
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM {} WHERE {} = %s;".format(tabla, campo)
            cursor.execute(sql,(dato,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            if filas_afectadas > 0:
                print("datos de la fila eliminados. ")
                return True
            else:
                print("no se eliminaron los datos de la consulta.")
                return False
        except Exception as ex:
            print(f"Error al ejecutar el delete: {ex}")
            return False
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)