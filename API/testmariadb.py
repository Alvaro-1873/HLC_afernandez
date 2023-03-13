import sys
from  mariadb import connect, Error

#-------------------------------
#- Conexion a la base de datos -
#-------------------------------

host="172.26.0.11"
port=3306
user="isaac"
database="objetos"
password="1234"

conn = connect(host=host, port=port, user=user, database=database, password=password) #Conexion a la base de datos

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

#-------------------------------------
#---- Consultar todos los objetos ----
#-------------------------------------
def consultar():
    objetos = [] #Creamos una tupla que contendra los datos del objeto
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("SELECT * FROM isaac_objects") #Creamos la sentecia select, en este caso devolvera todo lo que contenga la tabla
    for id, name, type, rarity in cur.fetchall(): #Creamos un bucle el cual nos soltara sobre cada variable el daco correspondiente de cada columna
        objetos.append(ItemIsaac(name, type, rarity, id)) #Añadimos a una tupla un objeto
    return objetos

#--------------------------------------------------
#---- Consultar los objetos mediante la rareza ----
#--------------------------------------------------
def consultar_rareza(rareza_input):
    objetos = [] #Creamos una tupla que contendra los datos del objeto
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("SELECT * FROM isaac_objects where rarity = ?", (rareza_input,)) #Crearemos una consulta a la cual le pasaremos una variable con un dato, en este caso sera la rareza del objeto.
    for id, name, type, rarity in cur.fetchall(): #Creamos un bucle el cual nos soltara sobre cada variable el dato correspondiente de cada columna
        objetos.append(ItemIsaac(name, type, rarity, id)) #Añadimos a una tupla un objeto
    return objetos

#----------------------------------------------
#---- Consultar los objetos mediante la ID ----
#----------------------------------------------
def consultar_id(id):
    objeto = [] #Creamos una tupla que contendra los datos del objeto
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("Select * from isaac_objects where id = ?",(id,)) #Crearemos una consulta a la cual le pasaremos una variable con un dato, en este caso sera la id del objeto.
    for id, name, type, rarity in cur: #Creamos un bucle el cual nos soltara sobre cada variable el dato correspondiente de cada columna
        objeto.append(ItemIsaac(name, type, rarity, id)) #Añadimos a una tupla un objeto
    return objeto

#---------------------------------------
#---- Tranforma un JSON a un objeto ----
#---------------------------------------
def tranformar(objeto_datos):  #Ingresamos los datos de un JSON a un objeto
    objeto=ItemIsaac(
        id=objeto_datos["id"],
        name=objeto_datos["name"],
        type=objeto_datos["type"],
        rarity=objeto_datos["rarity"]
    )
    return objeto

#------------------------------------------------
#---- Actualiza una linea mediante un objeto ----
#------------------------------------------------
def actualizar(objeto_id, objeto_datos):
    nuevo=tranformar(objeto_datos) #Usa la funcion transformar para pasar de JSON a objeto, luego añadimos cada campo a una variable
    id_old=objeto_id
    id_new=nuevo.id
    name=nuevo.name
    type=nuevo.type
    rarity=nuevo.rarity

    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("UPDATE isaac_objects SET id = ?, name = ?, type= ?, rarity = ? WHERE id = ?", (id_new, name, type, rarity, id_old,)) #Creamos el update y añadimos las variables necesarias
    conn.commit()

#----------------------------------
#---- Borra objeto de la tabla ----
#----------------------------------
def borrar(id):
    cur = conn.cursor() #Iniciamos la conexion a la base de datos
    cur.execute("DELETE FROM isaac_objects WHERE id=?", (id,)) #Recive la id del objeto y la borra
    conn.commit()

    if cur.rowcount == 0:
        return 1
    else:
        return 0