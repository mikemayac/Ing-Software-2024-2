# En usuario.py o detalle_usuario.py dependiendo de tu estructura
from db.database import get_db_connection


def insert_detalle_usuario(idUsuario, nombre, apPat, apMat, profilePicture):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `detalles_usuario` (`idUsuario`, `nombre`, `apPat`, `apMat`, `profilePicture`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (idUsuario, nombre, apPat, apMat, profilePicture))
        connection.commit()
    finally:
        connection.close()


def filtrar_usuarios_por_apellido(apellido):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Asume que el apellido está en la columna `apPat`
            sql = "SELECT * FROM `detalle_usuario` WHERE `apPat` LIKE %s"
            cursor.execute(sql, ('%' + apellido,))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()
