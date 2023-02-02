import mysql.connector

conn = mysql.connector.connect(
    host="host_de_la_bd",
    user="nombre_de_usuario",
    password="contraseña",
    database="nombre_de_la_bd"
)

