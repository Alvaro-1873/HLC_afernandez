from Pagos import Tarjeta_debito, Bizum, Tarjeta_credito, PayPal
from Productos import producto, libros, muebles, ropa, videojuegos
from cesta import ShoppingCart

#---------------------------------------------------------------------
#--------------------------- Metodos de pago -------------------------
#---------------------------------------------------------------------

#-------------------------- Targeta de debito-------------------------
tarjetadebi_1=Tarjeta_debito("Paco",1234567890,"10/26",123,10000)
tarjetadebi_2=Tarjeta_debito("Juan",1234567890,"10/26",123,10000)
tarjetadebi_3=Tarjeta_debito("Manolo",1234567890,"10/26",123,10000)
tarjetadebi_4=Tarjeta_debito("Raul",1234567890,"10/26",123,10000)

#-------------------------- Targeta de credito------------------------
targetacredito_1=Tarjeta_credito("Paco",1234567890,"10/26",123,10000,1000)
targetacredito_2=Tarjeta_credito("Juan",1234567890,"10/26",123,10000,1000)
targetacredito_3=Tarjeta_credito("Manolo",1234567890,"10/26",123,10000,1000)
targetacredito_4=Tarjeta_credito("Raul",1234567890,"10/26",123,10000,1000)

#-------------------------------- Bizum ------------------------------
bizum_1=Bizum("Rosa",652897898,1000)
bizum_2=Bizum("Antonio",111111111,1000)
bizum_3=Bizum("Pepe",222222222,1000)
bizum_4=Bizum("Javi",333333333,1000)

#-------------------------------- Paypal -----------------------------
paypal_1=PayPal("Rosa","rosa@gmail.com","111111",1000)
paypal_2 = PayPal("Antonio","antonio@gmail.com","222222",1000)
paypal_3 = PayPal("Pepe","pepe@gmail.com","333333",1000)
paypal_4 = PayPal("Javi","javi@gmail.com","444444",1000)

#----------------------------------------------------------------------
#------------------------------- Productos ----------------------------
#----------------------------------------------------------------------

#--------------------------------- Libros -----------------------------
libro1 = libros("El Gran Gatsby", "978-84-17929-24-5", 12.99, "Novela ambientada en los años 20 en Estados Unidos", "Novela", "F. Scott Fitzgerald", "ISBN-1234")
libro2 = libros("Cien años de soledad", "978-84-204-6744-4", 15.99, "Obra maestra del realismo mágico latinoamericano", "Realismo mágico", "Gabriel García Márquez", "ISBN-5678")
libro3 = libros("Orgullo y prejuicio", "978-84-376-0494-7", 9.99, "Una de las novelas más famosas de Jane Austen", "Novela romántica", "Jane Austen", "ISBN-9101")

#-------------------------------- Muebles -----------------------------
mueble_1 = muebles("Armario de roble","AR-001",200,"Armario de madera maciza de roble con cuatro puertas y dos cajones","180x120x60","Roble macizo")
mueble_2 = muebles("Sofá seccional de cuero","SC-002",400,"Sofá seccional moderno de 3 piezas en forma de L, tapizado en cuero","230x165x80","Cuero de alta calidad")
mueble_3 = muebles("Mesa de comedor de madera maciza","MC-003",250,"Mesa de comedor de estilo rústico con tablero de madera maciza de pino","180x90x76","Madera maciza de pino envejecido")

#---------------------------------- Ropa ------------------------------
ropa_1 = ropa("Chaqueta de invierno con capucha","CJ-001",120,"Chaqueta de invierno resistente al agua con capucha y forro térmico","L","Unisex","Invierno")
ropa_2 = ropa("Vestido de verano estampado","VS-002",50,"Vestido de verano ligero y cómodo con estampado floral en tonos rosados y verdes","M","Femenino","Verano")
ropa_3 = ropa("Camiseta de algodón básica","CM-003",15,"Camiseta de algodón 100% de color blanco con cuello redondo y mangas cortas","S","Unisex","Todas las estaciones")

#------------------------------- Videojuegos --------------------------
videojuegos_1 = videojuegos("The Elder Scrolls V: Skyrim","ESV-001",50,"Videojuego de rol en mundo abierto en el que el jugador puede explorar un vasto mundo de fantasía medieval lleno de peligros, misiones y aventuras","Bethesda Game Studios","RPG","PC, PlayStation 3, Xbox 360, PlayStation 4, Xbox One, Nintendo Switch","+17")
videojuegos_2 = videojuegos("FIFA 22","F22-002",60,"Videojuego de simulación de fútbol que permite al jugador controlar a su equipo favorito o a una selección nacional y competir contra otros equipos en distintos modos de juego","EA Sports","Deportes"," PC, PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Nintendo Switch, Google Stadia","+3")
videojuegos_3 = videojuegos("Resident Evil Village","REV-003",60,"Videojuego de terror en el que el jugador controla al personaje Ethan Winters, quien debe investigar una misteriosa aldea y enfrentarse a peligrosos enemigos para encontrar a su hija secuestrada","Capcom","Survival horror","PC, PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S","+18")

#----------------------------------------------------------------------
#-------------------------------- Listas ------------------------------
#----------------------------------------------------------------------

metodos_pagos = ["Tarjeta de debito","Tarjeta de credito","Bizum","Paypal"]
opciones_targetadebi = ["tarjetadebi_1","tarjetadebi_2","tarjetadebi_3","tarjetadebi_4"]
opciones_targetacredi = ["targetacredito_1","targetacredito_2","targetacredito_3","targetacredito_4"]
opciones_bizum = ["bizum_1","bizum_2","bizum_3","bizum_4"]
opciones_paypal = ["paypal_1","paypal_2","paypal_3","paypal_4"]
Productos= ["Libros","Muebles","Ropa","Videojuegos"]
productos_libros = ["libro1","libro2","libro3"]
productos_muebles = ["mueble_1","mueble_2","mueble_3"]
productos_ropa = ["ropa_1","ropa_2","ropa_3"]
productos_videojuegos = ["videojuegos_1","videojuegos_2","videojuegos_3"]

#----------------------------------------------------------------------
#------------------------------- Carrito ------------------------------
#----------------------------------------------------------------------

mi_carrito=ShoppingCart()
mi_carrito.add_objeto(videojuegos_1)
mi_carrito.add_objeto(videojuegos_2)
mi_carrito.add_objeto(videojuegos_3)
total=mi_carrito.get_total()

print(total)


"""
#----------------------------------------------------------------------
#--------------------------------- Menus ------------------------------
#----------------------------------------------------------------------

#---------------------------- menu_targetadebi -----------------------
def menu_targetacredi():
    salir=False
    while salir == False:
        print("\n----------------------")
        print("| Tarjetas guardadas |")
        print("----------------------")
        for i in range(len(opciones_targetacredi)):
            print(f"{i+1}. {opciones_targetacredi[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            targetacredito_1.activar()
            targetacredito_1.pagar(50)
            print("Has pagado con la targeta de: ", targetacredito_1.nombre ,"tu saldo ahora es de:", targetacredito_1.saldo,"€")
            salir=True
        elif eleccion == 2:
            targetacredito_2.activar()
            targetacredito_2.pagar(50)
            print("Has pagado con la targeta de: ", targetacredito_2.nombre ,"tu saldo ahora es de:", targetacredito_2.saldo,"€")
            salir=True
        elif eleccion == 3:
            targetacredito_3.activar()
            targetacredito_3.pagar(50)
            print("Has pagado con la targeta de: ", targetacredito_3.nombre ,"tu saldo ahora es de:", targetacredito_3.saldo,"€")
            salir=True
        elif eleccion == 4:
            targetacredito_4.activar()
            targetacredito_4.pagar(50)
            print("Has pagado con la targeta de: ", targetacredito_4.nombre ,"tu saldo ahora es de:", targetacredito_4.saldo,"€")
            salir=True
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#---------------------------- menu_targetadebi -----------------------
def menu_targetadebi():
    salir=False
    while salir == False:
        print("\n----------------------")
        print("| Tarjetas guardadas |")
        print("----------------------")
        for i in range(len(opciones_targetadebi)):
            print(f"{i+1}. {opciones_targetadebi[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            tarjetadebi_1.activar()
            tarjetadebi_1.pagar(50)
            print("Has pagado con la targeta de: ", tarjetadebi_1.nombre ,"tu saldo ahora es de:", tarjetadebi_1.saldo,"€")
            salir=True
        elif eleccion == 2:
            tarjetadebi_2.activar()
            tarjetadebi_2.pagar(50)
            print("Has pagado con la targeta de: ", tarjetadebi_2.nombre ,"tu saldo ahora es de:", tarjetadebi_2.saldo,"€")
            salir=True
        elif eleccion == 3:
            tarjetadebi_3.activar()
            tarjetadebi_3.pagar(50)
            print("Has pagado con la targeta de: ", tarjetadebi_3.nombre ,"tu saldo ahora es de:", tarjetadebi_3.saldo,"€")
            salir=True
        elif eleccion == 4:
            tarjetadebi_4.activar()
            tarjetadebi_4.pagar(50)
            print("Has pagado con la targeta de: ", tarjetadebi_4.nombre ,"tu saldo ahora es de:", tarjetadebi_4.saldo,"€")
            salir=True
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#-------------------------------- menu_Bizum ---------------------------
def menu_bizum():
    salir=False
    while salir == False:
        print("\n-------------------------------")
        print("| Numero de telefonos guardados |")
        print("---------------------------------")
        for i in range(len(opciones_bizum)):
            print(f"{i+1}. {opciones_bizum[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            print("Has pagado con numero:",bizum_1.numero_telefono,"ha nombre de:",bizum_1.nombre,"tu saldo ahora es de:",bizum_1.saldo,"€")
            salir=True
        elif eleccion == 2:
            print("Has pagado con numero:",bizum_2.numero_telefono,"ha nombre de:",bizum_2.nombre,"tu saldo ahora es de:",bizum_2.saldo,"€")
            salir=True
        elif eleccion == 3:
            print("Has pagado con numero:",bizum_3.numero_telefono,"ha nombre de:",bizum_3.nombre,"tu saldo ahora es de:",bizum_3.saldo,"€")
            salir=True
        elif eleccion == 4:
            print("Has pagado con numero:",bizum_4.numero_telefono,"ha nombre de:",bizum_4.nombre,"tu saldo ahora es de:",bizum_4.saldo,"€")
            salir=True
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#------------------------------- menu_Paypal ---------------------------
def menu_paypal():
    salir=False
    while salir == False:
        print("\n-----------------------------")
        print("| Cuentas de paypal guardadas |")
        print("-------------------------------")
        for i in range(len(opciones_paypal)):
            print(f"{i+1}. {opciones_paypal[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            print("Has pagado con numero:",bizum_1.numero_telefono,"ha nombre de:",bizum_1.nombre,"tu saldo ahora es de:",bizum_1.saldo,"€")
            salir=True
        elif eleccion == 2:
            print("Has pagado con numero:",bizum_2.numero_telefono,"ha nombre de:",bizum_2.nombre,"tu saldo ahora es de:",bizum_2.saldo,"€")
            salir=True
        elif eleccion == 3:
            print("Has pagado con numero:",bizum_3.numero_telefono,"ha nombre de:",bizum_3.nombre,"tu saldo ahora es de:",bizum_3.saldo,"€")
            salir=True
        elif eleccion == 4:
            print("Has pagado con numero:",bizum_4.numero_telefono,"ha nombre de:",bizum_4.nombre,"tu saldo ahora es de:",bizum_4.saldo,"€")
            salir=True
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#----------------------------- Metodos de pago -------------------------
def menu_metodos_pagos():
    salir=False
    while salir == False:
        print("--------------------")
        print("| Metodos de pagos |")
        print("--------------------")
        for i in range(len(metodos_pagos)):
            print(f"{i+1}. {metodos_pagos[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            menu_targetadebi()
        elif eleccion == 2:
            salir=True
            menu_targetacredi()
        elif eleccion == 3:
            salir=True
            menu_bizum()
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#------------------------------- menu_Libros ---------------------------
def menu_productos_libros():
    salir=False
    while salir == False:
        print("--------------------")
        print("| Metodos de pagos |")
        print("--------------------")
        for i in range(len(productos_libros)):
            print(f"{i+1}. {productos_libros[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            
        elif eleccion == 2:
            salir=True
            
        elif eleccion == 3:
            salir=True
            
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#------------------------------ menu_Muebles ---------------------------
def menu_productos_muebles():
    salir=False
    while salir == False:
        print("--------------------")
        print("| Metodos de pagos |")
        print("--------------------")
        for i in range(len(productos_muebles)):
            print(f"{i+1}. {productos_muebles[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            
        elif eleccion == 2:
            salir=True
            
        elif eleccion == 3:
            salir=True
            
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#-------------------------------- menu_Ropa ----------------------------
def menu_productos_ropa():
    salir=False
    while salir == False:
        print("--------------------")
        print("| Metodos de pagos |")
        print("--------------------")
        for i in range(len(productos_ropa)):
            print(f"{i+1}. {productos_ropa[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            
        elif eleccion == 2:
            salir=True
            
        elif eleccion == 3:
            salir=True
            
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#---------------------------- menu_Videojuegos -------------------------
def menu_productos_videojuegos():
    salir=False
    while salir == False:
        print("--------------------")
        print("| Metodos de pagos |")
        print("--------------------")
        for i in range(len(productos_videojuegos)):
            print(f"{i+1}. {productos_libros[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            
        elif eleccion == 2:
            salir=True
            
        elif eleccion == 3:
            salir=True
            
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#----------------------------- Metodos de Compra -----------------------

def menu_productos():
    salir=False
    while salir == False:
        print("--------------------")
        print("| Metodos de pagos |")
        print("--------------------")
        for i in range(len(Productos)):
            print(f"{i+1}. {Productos[i]}")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            
        elif eleccion == 2:
            salir=True
            
        elif eleccion == 3:
            salir=True
            
        elif eleccion == 4:
            salir=True
            return PayPal
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

"""