#Alvaro Fernandez Payo
#13-12-2022
año=int(input("Introduzca el año que quiera saber si es bisiesto: "))

if año % 4 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0:
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
	print("Es bisiesto")