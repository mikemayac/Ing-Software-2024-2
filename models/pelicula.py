from db.database import get_db_connection
from datetime import datetime, timedelta


def insert_pelicula(nombre, idGenero, duracion, cantidadDisponible):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `peliculas` (`nombre`, `idGenero`, `duracion`, `cantidadDisponible`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, idGenero, duracion, cantidadDisponible))
        connection.commit()
    finally:
        connection.close()


def insert_rentar(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus))
        connection.commit()
    finally:
        connection.close()


def cambiar_genero_pelicula(nombre_pelicula, nuevo_id_genero):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `peliculas` SET `idGenero`=%s WHERE `nombre`=%s"
            cursor.execute(sql, (nuevo_id_genero, nombre_pelicula))
        connection.commit()
    finally:
        connection.close()


def eliminar_rentas_antiguas():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            fecha_limite = datetime.now() - timedelta(days=3)
            sql = "DELETE FROM `rentar` WHERE `fecha_renta` <= %s"
            cursor.execute(sql, (fecha_limite,))
        connection.commit()
    finally:
        connection.close()
