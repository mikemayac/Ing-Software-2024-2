from db.database import get_db_connection


def insert_usuario(email, password, superUser=0):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `usuarios` (`email`, `password`, `superUser`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (email, password, superUser))
        connection.commit()
    finally:
        connection.close()
