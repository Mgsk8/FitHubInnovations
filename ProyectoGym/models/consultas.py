import database as database
def select():
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT * FROM usuario;"
            cursor.execute(sql)
            
            registros = cursor.fetchall()
 
            for registro in registros:
                print(registro)
        except Exception as ex:
            print("Error al ejecutar la consulta:", ex)
        finally:
            if cursor:
                cursor.close()
            database.desconectar(conexion)

select()

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