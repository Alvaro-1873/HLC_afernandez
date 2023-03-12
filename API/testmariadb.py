import sys
from  mariadb import connect, Error

#-------------------------------
#- Conexion a la base de datos -
#-------------------------------

host="localhost"
port=13307
user="isaac"
database="objetos"
password="1234"

conn = connect(host=host, port=port, user=user, database=database, password=password)

#--------------------
#- Clases principal -
#--------------------

class ItemIsaac:
    def __init__(self, name, type, rarity, id = None):
        self.id = id
        self.name=name
        self.type=type
        self.rarity=rarity

    def insertar(self):
        cur = conn.cursor()
        id=self.id
        name=self.name
        type=self.type
        rarity=self.rarity
        cur.execute("INSERT INTO isaac_objects (id, name, type, rarity) VALUES (?, ?, ?, ?)", (id,name,type,rarity,))
        conn.commit()

#-------------------------
#- Funciones principales -
#-------------------------

def consultar():
    objetos = [] #Creamos una lista que contendra los datos del objeto
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("SELECT * FROM isaac_objects")
    for id, name, type, rarity in cur.fetchall():
        objetos.append(ItemIsaac(name, type, rarity, id))
    return objetos

def consultar_rareza(rareza_input):
    objetos = []
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("SELECT * FROM isaac_objects where rarity = ?", (rareza_input,))
    for id, name, type, rarity in cur.fetchall():
        objetos.append(ItemIsaac(name, type, rarity, id))
    return objetos

def consultar_id(id):
    objeto = []
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("Select * from isaac_objects where id = ?",(id,))
    for id, name, type, rarity in cur:
        objeto.append(ItemIsaac(name, type, rarity, id))
    return objeto

def tranformar(objeto_datos):
    objeto=ItemIsaac(
        id=objeto_datos["id"],
        name=objeto_datos["name"],
        type=objeto_datos["type"],
        rarity=objeto_datos["rarity"]
    )
    return objeto

def actualizar(objeto_id, objeto_datos):
    nuevo=tranformar(objeto_datos)
    id_old=objeto_id
    id_new=nuevo.id
    name=nuevo.name
    type=nuevo.type
    rarity=nuevo.rarity

    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("UPDATE isaac_objects SET id = ?, name = ?, type= ?, rarity = ? WHERE id = ?", (id_new, name, type, rarity, id_old,))
    conn.commit()

def borrar(id):
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("DELETE FROM isaac_objects WHERE id=?", (id,))
    conn.commit()

    if cur.rowcount == 0:
        return 1
    else:
        return 0