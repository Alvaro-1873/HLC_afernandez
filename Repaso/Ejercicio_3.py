#Alvaro Fernandez Payo
#08-12-2022

def encriptar(palabra):
  salida=''
  for i in palabra:
    if i in clave:
      salida+=str(codigo.index(i))
    else:
      salida+=i
  return(salida)

def desencriptar(palabra):
  texto=''
  for i in palabra:
    if i.isdigit():
      texto+=codigo[int(i)]
    else:
      texto+=i
  return(texto)

clave='MURCIELAGO'
codigo=list(clave)
palabra=input("Ingrese la palabra a cifrar: ").upper()

palabra_encript=encriptar(palabra)
palabra_desencript=desencriptar(palabra_encript)
print(f"Palabra encriptada ({palabra_encript})")
print(f"Plabra Desencriptada ({palabra_desencript})")