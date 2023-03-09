import mariadb
import sys

try:
    conn = mariadb.connect(
        user="isaac",
        password="1234",
        host="172.26.0.11",
        port=3306,
        database="objetos"
    )
except mariadb.Error as e:
    print(f"Error en la conexion a la base de datos de mariadb: {e}")
    sys.exit(1)

def consulta():
    cur = conn.cursor()
    nombre = "Tech X"
    cur.execute("select id, nombre, descripcion, tipo, rareza, efecto from binding_of_isaac_objetos where nombre=?", (nombre,))
    for id, nombre, descripcion, tipo, rareza, efecto in cur:
        print(f"Id: {id}, Nombre: {nombre}, Descripcion: {descripcion}, Tipo: {tipo}, Rareza: {rareza}, Efecto: {efecto}")
    conn.close()

def insertar():
    try:
        cur = conn.cursor()
        nombre="Magic Mushroom"
        descripcion="Aumenta la salud, la lágrima, la velocidad y el daño del jugador"
        tipo="Objeto pasivo"
        rareza="Objeto especial"
        efecto="El jugador aumenta la salud, la lágrima, la velocidad y el daño, lo que mejora su capacidad para sobrevivir y luchar"
        imagen_url="https://bindingofisaacrebirth.fandom.com/wiki/Magic_Mushroom"
        cur.execute("INSERT INTO binding_of_isaac_objetos (nombre,descripcion,tipo,rareza,efecto,imagen_url) VALUES (?, ?, ?, ?, ?, ?)", (nombre,descripcion,tipo,rareza,efecto,imagen_url))
        conn.commit()
        conn.close()
    except mariadb.Error as e:
        print(f"Error al insertar los datos: {e}")
        sys.exit(1)
    
