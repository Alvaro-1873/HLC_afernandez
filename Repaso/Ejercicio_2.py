#!/bin/bash
#Alvaro Fernandez Payo
#08-12-2022

def combersion(segundos):
    horas = int(segundos/60/60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas} horas, {minutos} minuto, {segundos} segundos = {horas}:{minutos}:{segundos}"

numero = int(input("Ingrese los segundos que desee combertir: "))

segundos = [numero]

for cantidad_segundos in segundos:
    convertido = combersion(cantidad_segundos)
    print(f"{cantidad_segundos} segundos son {convertido}")
