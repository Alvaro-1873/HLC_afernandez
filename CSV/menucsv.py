#Alvaro Fernandez Payo
#14-12-2022

import csv
from csv import DictWriter, DictReader

archivo = "productos.csv"
lista_productos=[]

with open(archivo, newline='') as fichero:
  Productos = csv.DictReader(fichero)
  for row in Productos:
    lista_productos.append(row)

def busqueda(clave):
    for registro in lista_productos:
        if registro["ID"] == clave:
            print(registro)

def añadir():
    Clave=input("Introduzca el ID deseado:")
    Producto=input("Introduzca el nombre del producto: ")
    Precio=input("Introduce el precio del producto y su moneda: ")
    lista_productos.append({"ID":Clave,"Producto":Producto,"Precio":Precio})

def borra(clave):
    for registro in lista_productos:
        if registro["ID"] == clave:
            lista_productos.remove(registro)

def editar(clave, valor, opcion):
    for registro in lista_productos:
        if registro["ID"] == clave:
            registro[opcion]=valor

def sobreescribirCSV():
    header=["ID","Producto","Precio"]
    with open(archivo, 'w', newline='') as File:
        writer= csv.DictWriter(File,header)
        writer.writeheader()
        writer.writerows(lista_productos)

salir = False
while salir == False:
    print(""" 
    1.Buscar producto
    2.Añadir producto
    3.Borra producto
    4.Editar producto
    5.Salir
    """)
    opcion=int(input("Elige una opcion: "))

    if opcion == 1:
        clave=input("Ingrese la ID del producto que desee buscar: ")
        busqueda(clave)
    elif opcion == 2:
        añadir()
    elif opcion == 3:
        clave=input("Ingrese la ID del producto que desee borrar: ")
        borra(clave)
    elif opcion == 4:
        clave=input("Ingrese la ID del producto que desee editar: ")
        opcion=input("Indique el campo que de see cambiar(ID/Producto/Precio): ")
        valor=input("Ingrese el valor a insertar en el campo: ")
        editar(clave, valor, opcion)
    elif opcion == 5:
        guardar=input("¿Desea guardar los cambios (si/no)?")
        if guardar == "si":
            sobreescribirCSV()
            salir=True
        elif guardar == "no":
            salir=True
    else:
        print("Se ha insertado un caracter no valido")