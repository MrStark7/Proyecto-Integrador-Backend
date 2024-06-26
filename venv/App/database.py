
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        dbname="nombre_de_tu_bd", #acá pon el nombre de la base de datos para que conecte
        user="tu_usuario",
        password="tu_contraseña",
        host="localhost",
        port="5432"
    )
    return conn

def get_cursor(conn):
    return conn.cursor(cursor_factory=RealDictCursor)
