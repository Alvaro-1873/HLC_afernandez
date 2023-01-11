#!/bin/bash
#Alvaro Fernandez Payo
#03-01-2023

import random

def ahorcado():
    palabra = random.choice(["python", "java", "javascript", "html", "css"])
    letras_validas = 'abcdefghijklmnñopqrstuvwxyz'
    turnos = 5
    fallos = 0
    letra_introducida = ''
    letras_usadas = []
    stado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    while len(palabra) > 0:
        principal = ""
        omitido = 0

        for letras in palabra:
            if letras in letra_introducida:
                principal = principal + letras
            else:
                principal = principal + "_" + " "
        if principal == palabra:
            print(principal)
            print("¡Felicidades! Has ganado.")
            break

        print("Adivina la palabra:", principal)
        print("Letras usadas: ",letras_usadas)
        adivinar = input("Introduce una letra: ").lower()
        print("=================================")
        if not adivinar.isalpha() or len(adivinar)>1 or adivinar==' ':
            print("Entrada no válida. Intenta de nuevo con una sola letra sin espacios en blanco.")
            adivinar = input().lower()

        if adivinar in letras_validas:
            letra_introducida = letra_introducida + adivinar
            letras_usadas.append(adivinar)
        else:
            print("Entrada no válida. Intenta de nuevo.")
            adivinar = input().lower()

        if adivinar not in palabra:
            turnos = turnos - 1
            fallos +=1
            if turnos == 0:
              print(stado[-1])
              print(f"Has fallado la palabra era {palabra}")
              break
            else:
              print(stado[fallos])
              print(f"Te quedan {turnos} restantes")

ahorcado()