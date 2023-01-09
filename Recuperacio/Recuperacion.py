#!/bin/bash
#Alvaro Fernandez Payo
#09-12-2022


#-----------#
#Ejercicio 1#
#-----------#

def reverse(palabra):
  lista=list(palabra)
  longitud=len(palabra)-1
  lista_palabra_ordenada=[]

  for i in lista:
    lista_palabra_ordenada.append(lista[longitud])
    longitud-=1
    #print(lista_palabra_ordenada) este print es para comprobar que el bucle funciona
  
  palabra_ordenada = "".join(lista_palabra_ordenada)
  return palabra_ordenada

def comprobar(palabra, palabra_ordenada):
  if palabra == palabra_ordenada:
    print(f"({palabra}) --> Resultado: True")
  else:
    print(f"({palabra}) --> Resultado: False")


palabra = input("Introduzca una palabra: ")
print(comprobar(palabra, reverse(palabra)))

#-----------#
#Ejercicio 2#
#-----------#

import csv
from csv import DictReader

archivo = "/content/sample_data/distanciasAndalucia.csv"

def create_diccionario(archivo):
  distanciasAndalucia={}
  with open(archivo, newline='') as fichero:
    distanciasAndalucia = csv.DictReader(fichero)
    for row in distanciasAndalucia:
      origen=row["origen"]
      destino=row["destino"]
      km=row["km"]
      print(f"Origen:{origen} - Destino:{destino} - Km:{km}")

print(create_diccionario(archivo))


#-----------#
#Ejercicio 3#
#-----------#

import csv
from csv import DictReader

archivo = "/content/sample_data/distanciasAndalucia.csv"

precios_pro_litro={"disel":1.74, "diesel+":1.82, "gasolina95":1.64, "gasolina98":1.69,"biodiesel":1.71}

def create_diccionario(archivo):
  distanciasAndalucia={}
  with open(archivo, newline='') as fichero:
    distanciasAndalucia = csv.DictReader(fichero)
  return distanciasAndalucia



origen_usuario = input("Ciudad de origen:")
destino_usuario = input("Ciudad de destino:")
combustible_usuario = input("¿Que combustible usa?: ")
km_usuario = input("¿Cuanto consume su vehiculo a los 100km?: ")