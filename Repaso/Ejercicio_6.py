#Alvaro Fernandez Payo
#13-12-2022
cadenaPalabras=input("Ingrese un texto en el que se repita palabras:")
listaPalabras=cadenaPalabras.split()
frecuenciaPalab=[]
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))
print("Texto\n" + cadenaPalabras +"\n")
print("Repeticiones\n" + str(list(zip(listaPalabras, frecuenciaPalab))))