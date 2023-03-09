import sys
from  mariadb import connect, Error

class DC:

    def __init__(self, host, port, user, database, password):
        self.host = "172.26.0.11"
        self.port = 3306
        self.user = "isaac"
        self.database = "objetos"
        self.password = "1234"
        self.conn = None

    def connect(self):

        try:
            self.conn=connect(
                user=self.user,#hlc",
                password=self.password,#"1234",
                host=self.host,#"localhost",
                port=self.port,#3306,
                database=self.database#"prueba"
            )
        except Error as e:
            print(f"Error connecting to database {e}")
            sys.exit(1)
        else:
            print("Conexión realizada a la base de datos.")

    def close(self):
        self.conn.close()

    def execute_query(self,query):
        self.conn.cursor().execute(query)

    def get_cursor(self):
        return self.conn.cursor()

class User:
    def __init__(self, id, nombre, descripcion, tipo, rareza, efecto, imagen_url):
        self.id = id
        self.nombre=nombre
        self.descripcion=descripcion
        self.tipo=tipo
        self.rareza=rareza
        self.efecto=efecto
        self.imagen_url=imagen_url

    def __str__(self):
        return f"Usuario con id {self.id} y nombre {self.name}"
    
class UC(DC):
    def __init__(self, host, port, user, database, password):
        super().__init__(host, port, user, database, password)

    def insertar(self, nombre, descripcion, tipo, rareza, efecto, imagen_url):
        cur = self.get_cursor()
        cur.execute("INSERT INTO binding_of_isaac_objetos (nombre,descripcion,tipo,rareza,efecto,imagen_url) VALUES (?, ?, ?, ?, ?, ?)", (nombre,descripcion,tipo,rareza,efecto,imagen_url))
        self.conn.commit()

    def consultar(self):
        # objetos = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM binding_of_isaac_objetos")
        for id, nombre, descripcion, tipo, rareza, efecto, imagen_url in cur.fetchall():
            print(f"id: {id}, nombre: {nombre}, descripcion: {descripcion}, tipo: {tipo}, rareza: {rareza}, efecto: {efecto}, imagen_url: {imagen_url}")
        cur.close()
    
    def consultar_id(self, id):
        cur = self.get_cursor()
        cur.execute("Select * from binding_of_isaac_objetos where id = ?",(id,))
        for id, nombre, descripcion, tipo, rareza, efecto, imagen_url in cur:
            print(f"id: {id}, nombre: {nombre}, descripcion: {descripcion}, tipo: {tipo}, rareza: {rareza}, efecto: {efecto}, imagen_url: {imagen_url}")

    def actualizar(self, nombre,descripcion,tipo,rareza,efecto,imagen_url,id):
        cur = self.get_cursor()
        cur.execute("UPDATE binding_of_isaac_objetos SET id = ?, nombre = ?, descripcion = ?, tipo = ?, rareza = ?, efecto = ?, imagen_url = ? WHERE id = ?", (id, nombre, descripcion, tipo, rareza, efecto, imagen_url, id))
        self.conn.commit()
    
    def borrar(self, id):
        cur = self.get_cursor()
        cur.execute("DELETE FROM binding_of_isaac_objetos WHERE id=?", (id,))
        self.conn.commit()


if __name__ == "__main__":
    # Creando la conexión a la base de datos
    objet_conn = UC("172.26.0.11",3306,"isaac","objetos","1234")
    objet_conn.connect()

    print("1. Consultar tabla")
    print("2. Consultar tabla mediante ID")
    print("3. Añadir un objeto")
    print("4. Actualiza una fila de la tabla")
    print("5. Borrar una fila de la tabla")
    print("6. Salir")
    eleccion = int(input("Elige una opcion: "))

    salir=False
    while salir == False:
        if eleccion == 1:
            objet_conn.consultar()
            salir=True
        elif eleccion == 2:
            id=input("Indica la id del objeto que deseas consultar: ")
            objet_conn.consultar_id(id)
            salir=True
        elif eleccion == 3:
            nombre=input("Indique el nombre del objeto: ")
            descripcion=input("Indique la descripcion del objeto: ")
            tipo=input("Indique el tipo del ojeto: ")
            rareza=input("Indica la rareza del objeto: ")
            efecto=input("Describe el efecto del objeto: ")
            imagen_url=input("Indica la url de la imagen del objeto a añadir: ")

            objet_conn.insertar(nombre,descripcion,tipo,rareza,efecto,imagen_url)
            salir=True
        elif eleccion == 4:
            id=input("Indica la id del objeto que deseas actualizar: ")
            nombre=input("Indique el nombre del objeto: ")
            descripcion=input("Indique la descripcion del objeto: ")
            tipo=input("Indique el tipo del ojeto: ")
            rareza=input("Indica la rareza del objeto: ")
            efecto=input("Describe el efecto del objeto: ")
            imagen_url=input("Indica la url de la imagen del objeto a añadir: ")

            objet_conn.actualizar(nombre,descripcion,tipo,rareza,efecto,imagen_url,id)
            salir=True
        elif eleccion == 5:
            id=input("Indica la id del objeto que deseas borrar: ")
            objet_conn.borrar(id)
            salir=True
        elif eleccion == 6:
            salir=True
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

    # Cerrando la conexión 
    objet_conn.close()
