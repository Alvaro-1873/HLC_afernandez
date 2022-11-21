#!/bin/bash
#Alvaro Fernandez Payo
#16-11-2022

import random
aleatorio=random.randint(1000,9999)

def numero_usuario():
        entrada=False #Establevemos una variable para el while. 
        # lpaneque: Este comentario no aporta nada, se ve en la siguiente línea. Quizás otro nombre para la variable sería más claro. terminar por ejemplo.

        while entrada==False: #El bucle no parara hasta que la variable no este a true. #lpaneque: Mejor while not entrada

            numero=(input("Introduce un numero de 4 digitos: ")) #El usuario introducira un numero y seguardara en una variable.
# lpaneque Comprovamos? Con v?
            if numero.isdigit(): #Comprovamos si el usuario a introducido solamente numeros. 

                numero=int(numero) #Transformamos el dato introducido a enteros, de esta forma podremos manejarlo mejor.
                # lpaneque: Esto no es correcto. El número no puede ser al mismo tiempo menor que 1000 y mayor que 9999, es imposible!! Debes utilizar or
                if numero<1000 and numero>9999: #Verificamos si el valo ingresado es una cifra de 4 digitos.

                    print("El valor introducido no es valido, por favor introduzca un valor de 4 digitos.")

                else:

                    entrada=True #Si el valor establecido es correcto cabiara la variable y cesara el while.

            else:

                print("Debes de introducir un número entero.")

        return numero #Devolvemos el valor aceptable.

intentos=0 #establecemos el numero de intentos en 0, luego le iremos sumando valores para indicar el numero de intentos.
# lpaneque: Comentario obvio
bucle=False#Establevemos una variable para el while.

while bucle==False:
    #Establecemos valores a cada digito para luego verificar si en nuemro coincide.
    digi1=False
    digi2=False
    digi3=False
    digi4=False

    num_user=numero_usuario() #Ingresamos el numero valido en una variable
    intentos=(intentos+1) #Sumamos 1 al numero de intentos.

    #Extraemos el primer digito de cada numero para compararlos.
    A=aleatorio//1000
    A2=num_user//1000
    
    # lpaneque: Veo cierta influcencia del código José Daniel en tu código. 
    #  Me da la sensación de que si te pregunto qué hace el código no lo vas a tener claro.
    # No es necesario que hagas todas estas operaciones matemáticas. Con ir comparando dígito a dígito es suficiente.
    if (A-A2)==0:

        print("-----------------------------------------")
        print(f"El primer digito es correcto: {A2}")
        
        digi1=True

    elif (A-A2)>0:

        print("----------------------------------------")
        print(f"Has fallado el primer digito por +/-: {(A-A2)}")
    
    elif (A-A2)<0:
        
        print("----------------------------------------")
        print(f"Has fallado el primer digito por +/-: {(A2-A)}")
    
    B=(aleatorio-(A*1000))//100
    B2=(num_user-(A2*1000))//100

    if (B-B2)==0:

        print(f"El segundo digito es correcto: {B2}")

        digi2=True

    elif (B-B2)>0:

        print(f"Has fallado el segundo digito por +/-: {(B-B2)}")
    
    elif (B-B2)<0:
        
        print(f"Has fallado el segundo digito por +/-: {(B2-B)}")
    
    C=(aleatorio-((A*1000)+(B*100)))//10
    C2=(num_user-((A2*1000)+(B2*100)))//10

    if (C-C2)==0:

        print(f"El tercero digito es correcto: {C2}")

        digi3=True

    elif (C-C2)>0:

        print(f"Has fallado el tercer digito por +/-: {(C-C2)}")
    
    elif (C-C2)<0:
        
        print(f"Has fallado el tercer digito por +/-: {(C2-C)}")
    
    D=(aleatorio-((A*1000)+(B*100)+(C*10)))
    D2=(num_user-((A2*1000)+(B2*100)+(C2*10)))

    if (D-D2)==0:

        print(f"El cuarto digito es correcto: {D2}")
        print("-----------------------------------------")

        digi4=True

    elif (D-D2)>0:

        print(f"Has fallado el cuarto digito por +/-: {(D-D2)}")
        print("----------------------------------------")
    
    elif (D-D2)<0:
        
        print(f"Has fallado el cuarto digito por +/-: {(D2-D)}")
        print("----------------------------------------")
    
    if digi1==True and digi2==True and digi3==True and digi4==True:
        
        print(f"Enhorabuena has hacertado el numero: {aleatorio}")
        print(f"Lo has intentado un numero de: {intentos} intentos")
        print("-----------------------------------------")
        bucle=True
