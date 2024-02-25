import pymysql

from db.database import get_db_connection


def insert_usuario(email, password, superUser=0):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `usuarios` (`email`, `password`, `superUser`) VALUES (%s, %s, %s)"
            try:
                cursor.execute(sql, (email, password, superUser))
                id_usuario = cursor.lastrowid
                connection.commit()
                return id_usuario
            except pymysql.err.IntegrityError as e:
                print(f"Error al insertar usuario: {e}")
                # Opcional: retornar None o manejar de otra manera
    finally:
        connection.close()
