# API

API significa "Application Programming Interface" (Interfaz de Programación de Aplicaciones) y se refiere a un conjunto de reglas y protocolos que permiten a diferentes aplicaciones interactuar entre sí. En términos simples, una API es una manera en que diferentes programas o aplicaciones pueden comunicarse entre sí de manera estandarizada.

En el contexto de la web, una API suele referirse a un conjunto de endpoints (puntos finales) que se utilizan para permitir que las aplicaciones web interactúen entre sí. Las APIs web permiten a los desarrolladores integrar diferentes servicios y aplicaciones para crear aplicaciones más grandes y completas.

Por ejemplo, si una aplicación de noticias quisiera mostrar el clima actual en una ciudad en particular, podría utilizar una API del servicio meteorológico para obtener los datos en tiempo real y mostrarlos en la aplicación de noticias. De esta manera, las aplicaciones pueden compartir datos y funcionalidades sin necesidad de desarrollar todo desde cero.

---

# Testmariadb.py

El código es una aplicación Python que maneja una base de datos MariaDB para almacenar y manipular información de objetos. El código incluye la conexión a la base de datos, la definición de una clase ItemIsaac para manejar los objetos, y varias funciones para realizar operaciones de consulta, actualización y eliminación de objetos en la base de datos.

En la sección de conexión a la base de datos, se especifica el host, el puerto, el usuario, la contraseña y la base de datos a la que se conectará. Luego, se crea una conexión utilizando la biblioteca mariadb.

La clase ItemIsaac se utiliza para crear objetos que contienen información sobre un objeto en particular, incluyendo su nombre, tipo, rareza y un id opcional. También se incluye un método "insertar" que inserta el objeto en la base de datos.

Las funciones principales del código son:

- "consultar": consulta todos los objetos en la base de datos y los devuelve en una lista de objetos ItemIsaac.
- "consultar_rareza": consulta objetos en la base de datos que tengan una rareza específica y los devuelve en una lista de objetos ItemIsaac.
- "consultar_id": consulta un objeto en la base de datos por su id y lo devuelve como un objeto ItemIsaac.
- "tranformar": toma un diccionario de datos de objeto y devuelve un objeto ItemIsaac correspondiente.
- "actualizar": actualiza un objeto existente en la base de datos con nuevos datos de objeto.
- "borrar": elimina un objeto de la base de datos por su id.

En general, este código se utiliza para crear una aplicación de base de datos que puede almacenar y manipular información sobre objetos. La aplicación podría tener una interfaz de usuario que permita al usuario agregar, ver, actualizar y eliminar objetos en la base de datos.

---

# Main.py

Este código define una API web usando FastAPI que se conecta a una base de datos usando un módulo personalizado llamado "testmariadb".

La API tiene cinco endpoints:

1. `GET /objetos_isaac`: Consulta la base de datos para obtener una lista de objetos. Si se proporciona el parámetro `objeto_rare`, devuelve solo los objetos con la rareza especificada, de lo contrario devuelve todos los objetos.

2. `GET /objeto_id/{objeto_id}`: Consulta la base de datos para obtener un objeto por su ID.

3. `POST /insert_objeto`: Inserta un nuevo objeto en la base de datos. Los datos del objeto se pasan en el cuerpo de la solicitud.

4. `PUT /actu_objeto/{objeto_id}`: Actualiza un objeto existente en la base de datos por su ID. Los datos del objeto actualizado se pasan en el cuerpo de la solicitud.

5. `DELETE /borra_objeto/{objeto_id}`: Elimina un objeto existente en la base de datos por su ID.

Cada endpoint devuelve una respuesta en formato JSON. Además, se utilizan las excepciones de HTTP para devolver un código de estado y un mensaje de error apropiados si algo sale mal.

Finalmente, el archivo usa Uvicorn para ejecutar la aplicación en el puerto 8000.

---

# Base de datos y tablas

create database objetos;

use objetos;

CREATE TABLE isaac_objects (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  type VARCHAR(50) NOT NULL,
  rarity VARCHAR(20) NOT NULL
);

INSERT INTO isaac_objects (id, name, type, rarity) VALUES (1, 'The Bible', 'Active', 'Rare'),
 (2, 'The Halo', 'Passive', 'Rare'),
 (3, 'The Hourglass', 'Active', 'Uncommon'),
 (4, 'The Compass', 'Passive', 'Common'),
 (5, 'The Book of Belial', 'Active', 'Rare'),
 (6, 'The Halo of Flies', 'Passive', 'Uncommon'),
 (7, 'The Pentagram', 'Passive', 'Rare'),
 (8, 'The Book of Shadows', 'Active', 'Uncommon'),
 (9, 'The Nail', 'Passive', 'Rare'),
 (10, 'The Razor Blade', 'Active', 'Common');