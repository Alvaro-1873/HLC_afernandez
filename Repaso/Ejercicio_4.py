#Alvaro Fernandez Payo
#08-12-2022
import sys

def verificacion(dni):
    if len(dni) == 9:
      return True
    else:
        print("Se ha introducido un numero erroneo de caracteres")
        sys.exit(1)

def prohibidos(dni):
    dni_proibidos=["00000000T","00000001R","99999999R"]
    if dni in dni_proibidos:
        print("Ha introducido un DNI prohibido por la institucion ¡¡¡¡¡ESPAÑOLA!!!!!")
        sys.exit(1)
    else:
      return True

def separacion(dni):
    dni_completo = list(dni)
    numero = "".join(dni_completo[0:8])
    letra = "".join(dni_completo[8])
    return numero, letra

def validar_numero(numero):
    correcto=True
    lista_numeros=["0","1","2","3","4","5","6","7","8","9"]
    for i in range(0,8):
        if numero[i] not in lista_numeros:
            correcto=False
        
    if correcto == False:
        print("Ha introducido mal el DNI")
        sys.exit(1)
    return True

def DNI(numero, letra):
    intnumero = int(numero)
    diccionario = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",
               11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",
               20:"C",21:"K",22:"E"}
    resto = intnumero%23
    letra_calculada = diccionario[resto]

    if letra_calculada == letra:
        print("El DNI es Valido")
    else:
        print("El DNI no es valido")
    
dni = input("Introduzca su DNI: ")


if verificacion(dni):
    if prohibidos(dni):
        numero, letra = separacion(dni)
        if validar_numero(numero):
            DNI(numero, letra)
        else:
            print("Sea producido un error en validar_numero")
    else:
        print("Sea producido un error en prohibidos")
else:
    print("Sea producido un error en verificacion")