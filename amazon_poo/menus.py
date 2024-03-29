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
targetacredito_1=Tarjeta_credito("Pepe",1234567890,"10/26",123,10000,1000)
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
productos_libros = ["libro_1","libro_2","libro_3"]
productos_muebles = ["mueble_1","mueble_2","mueble_3"]
productos_ropa = ["ropa_1","ropa_2","ropa_3"]
productos_videojuegos = ["videojuegos_1","videojuegos_2","videojuegos_3"]

#----------------------------------------------------------------------
#------------------------- Menus metodos de pago ----------------------
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
            mi_carrito.pagotarjeta(targetacredito_1)
            salir=True
        elif eleccion == 2:
            mi_carrito.pagotarjeta(targetacredito_2)
            salir=True
        elif eleccion == 3:
            mi_carrito.pagotarjeta(targetacredito_3)
            salir=True
        elif eleccion == 4:
            mi_carrito.pagotarjeta(targetacredito_4)
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
            mi_carrito.pagotarjeta(tarjetadebi_1)
            salir=True
        elif eleccion == 2:
            mi_carrito.pagotarjeta(tarjetadebi_2)
            salir=True
        elif eleccion == 3:
            mi_carrito.pagotarjeta(tarjetadebi_3)
            salir=True
        elif eleccion == 4:
            mi_carrito.pagotarjeta(tarjetadebi_4)
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
            mi_carrito.pagobizum(bizum_1)
            salir=True
        elif eleccion == 2:
            mi_carrito.pagobizum(bizum_2)
            salir=True
        elif eleccion == 3:
            mi_carrito.pagobizum(bizum_3)
            salir=True
        elif eleccion == 4:
            mi_carrito.pagobizum(bizum_4)
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
            mi_carrito.pagopaypal(paypal_1)
            salir=True
        elif eleccion == 2:
            mi_carrito.pagopaypal(paypal_2)
            salir=True
        elif eleccion == 3:
            mi_carrito.pagopaypal(paypal_3)
            salir=True
        elif eleccion == 4:
            mi_carrito.pagopaypal(paypal_4)
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
            menu_paypal()
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#----------------------------------------------------------------------
#----------------------------- Menus Productos ------------------------
#----------------------------------------------------------------------

#------------------------------- menu_Libros --------------------------
def menu_productos_libros():
    salir=False
    while salir == False:
        print("----------")
        print("| Libros |")
        print("----------")
        for i in range(len(productos_libros)):
            print(f"{i+1}. {productos_libros[i]}")
        print("4. Salir")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            mi_carrito.add_objeto(libro1)
            print("Añadido libro 1")
        elif eleccion == 2:
            mi_carrito.add_objeto(libro2)
            print("Añadido libro 2")
        elif eleccion == 3:
            mi_carrito.add_objeto(libro3)
            print("Añadido libro 3")
        elif eleccion == 4:
            salir=True
            menu_productos()
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#------------------------------ menu_Muebles ---------------------------
def menu_productos_muebles():
    salir=False
    while salir == False:
        print("-----------")
        print("| Muebles |")
        print("-----------")
        for i in range(len(productos_muebles)):
            print(f"{i+1}. {productos_muebles[i]}")
        print("4. Salir")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            mi_carrito.add_objeto(mueble_1)
            print("Añadido mueble 1")
        elif eleccion == 2:
            mi_carrito.add_objeto(mueble_2)
            print("Añadido mueble 2")
        elif eleccion == 3:
            mi_carrito.add_objeto(mueble_3)
            print("Añadido mueble 3")
        elif eleccion == 4:
            salir=True
            menu_productos()
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#-------------------------------- menu_Ropa ----------------------------
def menu_productos_ropa():
    salir=False
    while salir == False:
        print("--------")
        print("| Ropa |")
        print("--------")
        for i in range(len(productos_ropa)):
            print(f"{i+1}. {productos_ropa[i]}")
        print("4. Salir")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            mi_carrito.add_objeto(ropa_1)
            print("Añadido ropa 1")
        elif eleccion == 2:
            mi_carrito.add_objeto(ropa_2)
            print("Añadido ropa 2")
        elif eleccion == 3:
            mi_carrito.add_objeto(ropa_3)
            print("Añadido ropa 3")
        elif eleccion == 4:
            salir=True
            menu_productos()
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

#---------------------------- menu_Videojuegos -------------------------
def menu_productos_videojuegos():
    salir=False
    while salir == False:
        print("---------------")
        print("| Videojuegos |")
        print("---------------")
        for i in range(len(productos_videojuegos)):
            print(f"{i+1}. {productos_libros[i]}")
        print("4. Salir")
        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            mi_carrito.add_objeto(videojuegos_1)
            print("Añadido videojuegos 1")
        elif eleccion == 2:
            mi_carrito.add_objeto(videojuegos_2)
            print("Añadido videojuegos 2")
        elif eleccion == 3:
            mi_carrito.add_objeto(videojuegos_3)
            print("Añadido videojuegos 3")
        elif eleccion == 4:
            salir=True
            menu_productos()
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
        print("5. Tramitar")
        print("6. Salir")

        eleccion = int(input("Selecciona una opcion: "))
        if eleccion == 1:
            salir=True
            menu_productos_libros()
        elif eleccion == 2:
            salir=True
            menu_productos_muebles()
        elif eleccion == 3:
            salir=True
            menu_productos_ropa()
        elif eleccion == 4:
            salir=True
            menu_productos_videojuegos()
        elif eleccion == 5:
            salir=True
            menu_metodos_pagos()
        elif eleccion == 6:
            salir=True
        else:
            print("---------------------")
            print("| Opcion incorrecta |")
            print("---------------------")

mi_carrito=ShoppingCart("alvaro")
menu_productos()