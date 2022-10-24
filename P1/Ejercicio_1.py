
import random
entrada = input("Elige piedra, papel o tijeras:")

aleatorio = random.randint(1,3)

if entrada.lower() == "piedra":
    eleccion = 1
elif entrada.lower() == "papel":
    eleccion = 2
elif entrada.lower() == "tijeras":
    eleccion = 3
else:
    print ("El valor introducido no es correcto.")



if (eleccion == 1) and (aleatorio == 2):
    print ('Has perdido')
if (eleccion == 1) and (aleatorio == 3):
    print ('Has Ganado')
elif (eleccion == 2) and (aleatorio == 1):
    print ('Has Ganado')
elif (eleccion == 2) and (aleatorio == 3):
    print ('Has perdido')
elif (eleccion == 3) and (aleatorio == 1):
    print ('Has perdido')
elif (eleccion == 3) and (aleatorio == 2):
    print ('Has Ganado')
elif (eleccion == aleatorio):
    print ('Habeis empatado')
