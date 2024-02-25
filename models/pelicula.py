import pymysql

from db.database import get_db_connection
from datetime import datetime, timedelta


def insert_pelicula(nombre, idGenero, duracion, cantidadDisponible):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            print(f"Insertando película: {nombre}, Género: {idGenero}, Duración: {duracion}, Disponibles: {cantidadDisponible}")
            sql = "INSERT INTO `peliculas` (`nombre`, `idGenero`, `duracion`, `cantidadDisponible`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, idGenero, duracion, cantidadDisponible))
            id_pelicula = cursor.lastrowid
            connection.commit()
            print(f"Película insertada con ID: {id_pelicula}")
            return id_pelicula
    except pymysql.err.IntegrityError as e:
        print(f"Error al insertar película: {e}")
    except Exception as e:
        print(f"Error al insertar película: {e}")
    finally:
        connection.close()


def insert_rentar(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus))
            connection.commit()
            print("Renta insertada correctamente.")
    except pymysql.err.IntegrityError as e:
        # Este bloque captura errores de integridad, como violaciones de clave foránea.
        print(f"No se pudo insertar la renta debido a un error de integridad: {e}")
    except pymysql.err.MySQLError as e:
        # Este bloque captura errores generales relacionados con MySQL.
        print(f"Error de MySQL: {e}")
    except Exception as e:
        # Este bloque captura cualquier otro tipo de error no capturado por los bloques anteriores.
        print(f"Ocurrió un error al insertar la renta: {e}")
    finally:
        connection.close()


def poblar_generos():
    generos_default = [
        'Acción', 'Comedia', 'Drama', 'Fantasía', 'Horror',
        'Romance', 'Ciencia Ficción', 'Thriller', 'Documental', 'Animación', 'Aventura'
    ]
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            for genero in generos_default:
                sql = "INSERT INTO `generos` (`nombre`) VALUES (%s)"
                cursor.execute(sql, (genero,))
        connection.commit()
        print("Géneros poblados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al poblar los géneros: {e}")
    finally:
        connection.close()

def mostrar_generos_y_seleccionar():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Verificar si hay géneros disponibles
            sql = "SELECT COUNT(*) AS count FROM `generos`"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            if resultado['count'] == 0:
                # Si no hay géneros, poblar la tabla
                poblar_generos()

            # Ahora, seleccionar y mostrar los géneros
            sql = "SELECT `idGenero`, `nombre` FROM `generos`"
            cursor.execute(sql)
            generos = cursor.fetchall()
            print("Seleccione el número del nuevo género para la película:")
            for genero in generos:
                print(f"{genero['idGenero']}. {genero['nombre']}")
            seleccion = int(input())
            return seleccion
    except Exception as e:
        print(f"Ocurrió un error al obtener los géneros: {e}")
        return None
    finally:
        connection.close()


def cambiar_genero_pelicula(nombre_pelicula):
    id_genero = mostrar_generos_y_seleccionar()
    if id_genero is None:
        print("Operación cancelada o género inválido.")
        return

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `peliculas` SET `idGenero` = %s WHERE `nombre` = %s"
            cursor.execute(sql, (id_genero, nombre_pelicula))
            if cursor.rowcount > 0:
                connection.commit()
                print(f"Género de la película '{nombre_pelicula}' cambiado exitosamente.")
            else:
                print(f"No se encontró la película '{nombre_pelicula}' para actualizar.")
    except Exception as e:
        print(f"Ocurrió un error al cambiar el género de la película: {e}")
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
