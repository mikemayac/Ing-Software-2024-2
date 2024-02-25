# Conexión a la base de datos y operaciones básicas
import pymysql.cursors
from .config import DATABASE_CONFIG

def get_db_connection():
    return pymysql.connect(**DATABASE_CONFIG, cursorclass=pymysql.cursors.DictCursor)
