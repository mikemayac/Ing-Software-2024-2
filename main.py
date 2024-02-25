from db.database import get_db_connection
from models.usuario import insert_usuario
from models.detalle_usuario import insert_detalle_usuario, filtrar_usuarios_por_apellido
from models.genero import insertar_genero
from models.pelicula import insert_pelicula, cambiar_genero_pelicula, insert_rentar, eliminar_rentas_antiguas
import datetime

def main():
    try:
        # 1. Insertar al menos 1 registro en cada tabla.
        id_usuario = insert_usuario('mario1@test.com', 'passexample', 0)
        print(f"ID de usuario insertado: {id_usuario}")
        print("Usuario insertado correctamente.")
        insert_detalle_usuario(id_usuario, 'Mario1', 'Zampano1', 'Hernandez1', 'url/a/imagen.jpg')
        print("Detalle de usuario insertado correctamente.")
        id_genero = insertar_genero('Thriller')
        print("Género insertado correctamente.")
        id_pelicula = insert_pelicula('Buscando a memo 2', id_genero, 120, 10)
        print("Película insertada correctamente.")
        insert_rentar(id_usuario, id_pelicula, datetime.datetime.now(), 5, 'activo')
        print("Renta insertada correctamente.")
    # else:
    #     print("No se pudo insertar el usuario. Verifique que el email no esté duplicado.")

        # 2. Filtrar a la tabla Usuario por apellido.
        apellido_a_buscar = input("Ingrese el final del apellido a buscar: ")
        usuarios = filtrar_usuarios_por_apellido(apellido_a_buscar)
        if usuarios:
            print(f"Usuarios filtrados por apellido '{apellido_a_buscar}': {usuarios}")
        else:
            print(f"No se encontraron usuarios con el apellido terminando en '{apellido_a_buscar}'.")

        # 3. Cambiar el género de una película existente.
        nombre_pelicula = input("Ingrese el nombre de la película a cambiar de género: ")
        genero_modificado = cambiar_genero_pelicula(nombre_pelicula)
        print(f"Género de la película {nombre_pelicula}, cambiado a '{genero_modificado}' exitosamente.")

        # 4. Eliminar todas las rentas anteriores a 3 días a la fecha actual.
        # if eliminar_rentas_antiguas():
        #     print("Rentas antiguas eliminadas correctamente.")

    except Exception as e:
        print(f"Ocurrió un error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
    # insert_pelicula('Rapidos y Furiosos',1,120,30)
    # insert_rentar(1,1,datetime.datetime.now(),20,'activo')
