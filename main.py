from db.database import get_db_connection
from models.usuario import insert_usuario
from models.detalle_usuario import filtrar_usuarios_por_apellido
from models.genero import insertar_genero
from models.pelicula import insert_pelicula, cambiar_genero_pelicula, insert_rentar, eliminar_rentas_antiguas
import datetime

def main():
    # 1. Insertar al menos 1 registro en cada tabla.
    # Asegúrate de que estos métodos retornen el ID del registro insertado si es necesario para las claves foráneas.
    id_usuario = insert_usuario('test@example.com', 'securepassword', 0)
    id_genero = insertar_genero('Comedia')
    id_pelicula = insert_pelicula('Mi Película', id_genero, 120, 10)
    insert_rentar(id_usuario, id_pelicula, datetime.datetime.now(), 5, 'activo')

    # 2. Filtrar a la tabla Usuario por apellido.
    apellido_a_buscar = input("Ingrese el final del apellido a buscar: ")
    filtrar_usuarios_por_apellido(apellido_a_buscar)

    # 3. Cambiar el género de una película existente.
    nombre_pelicula = input("Ingrese el nombre de la película a cambiar de género: ")
    nuevo_genero = input("Ingrese el nuevo género para la película: ")
    cambiar_genero_pelicula(nombre_pelicula, nuevo_genero)

    # 4. Eliminar todas las rentas anteriores a 3 días a la fecha actual.
    eliminar_rentas_antiguas()

if __name__ == "__main__":
    main()
