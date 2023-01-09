#Alvaro Fernandez Payo
#fecha: 24/11/2022
#Examen de Python

#-----------#
#Ejercicio 1#
#-----------#








#-----------#
#Ejercicio 2#
#-----------#

from csv import DictReader

Datos = "/content/peliculas.csv"

def create_list(archivo):
    lista=[]
    with open(archivo, 'r') as file:
        reader = DictReader(file)
        for linea in reader:
            lista.append(linea)
    return lista

definido = create_list(Datos)

for registros in definido:
  print(f"Titulo:{registros['titulo']} - Director:{registros['director']} - Año:{registros['anyo']} - Genero:{registros['genero']}")


#-----------#
#Ejercicio 3#
#-----------#


from csv import DictWriter

Datos = "/content/peliculas.csv"

def create_list(archivo):
    lista=[]
    with open(archivo, 'r') as file:
        reader = DictReader(file)
        for linea in reader:
            lista.append(linea)
    return lista

def nueva_pelicula():
  nuevos_datos=[]

  titulo = input("Añade un titulo de la pelicula: ")
  director = input("Indica el director: ")
  año = input("El año que salio la pelicula: ")
  genero = input("El genero de la pelicula: ")
  nuevos_datos.append({"titulo": titulo, "anyo": año, "genero": genero, "director": director})
  return nuevos_datos

def lista_nueva(lista1, lista2):
  nueva_lista=[]
  nueva_lista.append(lista1)
  nueva_lista.extend(lista2)
  return lista1

lista1=create_list(Datos)
lista2=nueva_pelicula()
definido=lista_nueva(lista1, lista2)

#print(lista1)
#print(lista2)
#print(definido)
for registros in definido:
  print(f"Titulo:{registros['titulo']} - Director:{registros['director']} - Año:{registros['anyo']} - Genero:{registros['genero']}")