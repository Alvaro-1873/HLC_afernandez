from Pagos import Tarjeta_debito, Bizum, Tarjeta_credito, PayPal

tarjetadebi_1=Tarjeta_debito("Paco",1234567890,"10/26",123,10000)
tarjetadebi_2=Tarjeta_debito("Juan",1234567890,"10/26",123,10000)
tarjetadebi_3=Tarjeta_debito("Manolo",1234567890,"10/26",123,10000)
tarjetadebi_4=Tarjeta_debito("Raul",1234567890,"10/26",123,10000)

metodos_pagos = ["Tarjeta de debito","Tarjeta de credito","Bizum","Paypal"]
opciones_targetadebi = ["tarjetadebi_1","tarjetadebi_2","tarjetadebi_3","tarjetadebi_4"]

def menu_targetadebi():
    salir=False
    while salir == False:
        print("Tarjetas guardadas:")
        for i in range(len(opciones_targetadebi)):
            print(f"{i+1}. {opciones_targetadebi[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            return opciones_targetadebi[0]
        elif eleccion == 2:
            salir=True
            return opciones_targetadebi[1]
        elif eleccion == 3:
            salir=True
            return opciones_targetadebi[2]
        elif eleccion == 4:
            salir=True
            return opciones_targetadebi[3]
        else:
            print("Opcion incorrecta")

def menu_metodos_pagos():
    salir=False
    while salir == False:
        print("Metodos de pagos:")
        for i in range(len(metodos_pagos)):
            print(f"{i+1}. {metodos_pagos[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            menu_targetadebi()
        elif eleccion == 2:
            salir=True
            return Tarjeta_credito
        elif eleccion == 3:
            salir=True
            return Bizum
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("Opcion incorrecta")

#print(menu_metodos_pagos())
#print(tarjetadebi_1)
tarjetadebi_1.activar()
tarjetadebi_1.pagar(50)