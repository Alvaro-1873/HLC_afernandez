
import random
terminar = "False"

# lpaneque: Mejor hacerlo al revés
#continuar=True
# while continuar:
# Por cierto, terminar debería ser Boolean no texto. Los booleanos son True y False y NO van entre comillas.
while terminar == "False":

    entrada = input("Elige piedra, papel o tijeras:")

    aleatorio = random.randint(1,3)

    if entrada.lower() == "piedra":
        eleccion = 1
    elif entrada.lower() == "papel":
        eleccion = 2
    elif entrada.lower() == "tijeras":
        eleccion = 3
    else:
        print (f"El valor introducido no es correcto.")

    if (eleccion == 1) and (aleatorio == 2):
        print (f"Jugador <------ VS ------>  IA")
        print (f"Piedra  <------ VS ------> Papel")
        # lpaneque: Te puedes ahorar un monton de líneas de código si utilizas variables o lo incluyes en una función.:
        # print (f"{jugador}  <------ VS ------> {maquina}")
        print (f'---------- Has perdido ---------')
    if (eleccion == 1) and (aleatorio == 3):
        print (f"Jugador <------ VS ------>   IA")
        print (f"Piedra  <------ VS ------> Tijeras")
        print (f'---------- Has Ganado ------------')
    elif (eleccion == 2) and (aleatorio == 1):
        print (f"Jugador <------ VS ------>   IA")
        print (f" Papel  <------ VS ------> Piedra")
        print (f'---------- Has Ganado -----------')
    elif (eleccion == 2) and (aleatorio == 3):
        print (f"Jugador <------ VS ------>   IA")
        print (f" Papel  <------ VS ------> Tijeras")
        print (f'---------- Has perdido -----------')
    elif (eleccion == 3) and (aleatorio == 1):
        print (f"Jugador <------ VS ------>   IA")
        print (f"Tijeras <------ VS ------> Piedra")
        print (f'---------- Has perdido ----------')
    elif (eleccion == 3) and (aleatorio == 2):
        print (f"Jugador <------ VS ------>  IA")
        print (f"Tijeras <------ VS ------> Papel")
        print (f'---------- Has Ganado ----------')
    elif (eleccion == aleatorio):
        print (f"---------------------------------")
        print (f'-------- Habeis empatado --------')
        print (f"---------------------------------")
    
    volver = input("¿Quieres volver a jugar? [Y/N]:")

    if volver.lower() == "y":
        terminar = "False"
    elif volver.lower() == "n":
        terminar = "True"
        
  # lpaneque: Faltan las funciones para estrucutrar tu código.
