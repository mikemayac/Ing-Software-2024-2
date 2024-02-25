from db.database import get_db_connection


def insertar_genero(nombre):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `generos` (`nombre`) VALUES (%s)"
            cursor.execute(sql, (nombre,))
        connection.commit()
    finally:
        connection.close()