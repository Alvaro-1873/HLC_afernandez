#Alvaro Fernandez Payo
#19-01-2023

class Tarjeta_debito:
    def __init__(self, nombre, numero_tarjeta, fecha_de_caducidad, cvv, saldo=0):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta
        self.fecha_de_caducidad = fecha_de_caducidad
        self.cvv = cvv
        self.activa = False
        self.saldo = saldo

    def activar(self):
        if not self.activa:
            self.activa = True
            print(f"Activando la tarjeta")
        else:
            print(f"La tarjeta con con número {self.numero} ya estaba activada")

    def pagar(self, cantidad):
        if self.activa:
            print(f"Pagando {cantidad}")
            self.saldo-=cantidad
            print(f"Su saldo es de {self.saldo}")
        else:
            print(f"ERROR al pagar con la tarjeta {self.numero}. TARJETA INACTIVA")

    def anular(self):
        if self.activa:
            print(f"Anulando la tarjeta {self.numero}")
            self.activa = False
        else:
            print(f"La tarjeta {self.numero} ya estaba desactivada.")

class Tarjeta_credito(Tarjeta_debito):
    def __init__(self, nombre, numero_tarjeta, fecha_de_caducidad, cvv, saldo, credito):
        super().__init__(nombre, numero_tarjeta, fecha_de_caducidad, cvv, saldo)
        self.credito = 0

class Bizum:
    def __init__(self, nombre, numero_telefono, saldo=0):
        self.nombre = nombre
        self.numero_telefono = numero_telefono
        self.saldo = saldo

    def pagar(self, cantidad):
        print(f"Pagando {cantidad}")
        self.saldo-=cantidad
        print(f"Su saldo es de {self.saldo}")

class PayPal:
    def __init__(self, nombre, correo, contraseña, saldo=0):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.saldo = saldo

    def pagar(self, cantidad):
        print(f"Pagando {cantidad} con usuario {self.nombre} con correo {self.correo}...")
        self.saldo-=cantidad
        print(f"Su saldo es de {self.saldo}")