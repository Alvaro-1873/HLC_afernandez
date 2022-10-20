
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

