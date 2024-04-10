import database
def select():
    conexion = database.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "SELECT * FROM administrador;"
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