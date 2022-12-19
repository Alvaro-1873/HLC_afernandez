#Alvaro Fernandez Payo
#08-12-2022

def anagrama(palabra1, palabra2):

    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    #print(palabra1)
    #print(palabra2)

    lista1 = list(palabra1)
    lista2 = list(palabra2)

    #print(lista1)
    #print(lista2)

    lista1.sort()
    lista2.sort()

    #print(lista1)
    #print(lista2)

    palabra1_ordenada = "".join(lista1) # lpaneque: Pero esto para qué? si puedes convertir una lista a string str(lista)
    palabra2_ordenada = "".join(lista2)

    #print(palabra1_ordenada)
    #print(palabra2_ordenada)

    if palabra1_ordenada == palabra2_ordenada:
        return True
    else:
        return False


palabra1 = input("Ingresa una palabra: ")
palabra2 = input("Ingresa otra palabra: ")

es_anagrama = anagrama(palabra1, palabra2)

if es_anagrama == True:
    print(f"{palabra1} es anagrama de {palabra2}")
else:
    print(f"{palabra1} NO es anagrama de {palabra2}")
