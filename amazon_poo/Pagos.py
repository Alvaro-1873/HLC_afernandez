#Alvaro Fernandez Payo
#19-01-2023

class Tarjeta_debito:
    def __init__(self, nombre, numero_tarjeta, fecha_de_caducidad, cvv, activa, saldo):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta
        self.fecha_de_caducidad = fecha_de_caducidad
        self.cvv = cvv
        self.activa = False
        self.saldo = 0

        def activar(self):
            if not self.activa:
                self.activa = True
                print(f"Activando la tarjeta con número {self.numero}")
            else:
                print(f"La tarjeta con con número {self.numero} ya estaba activada")
    
        def pagar(self, cantidad):
            if self.activa:
                print(f"Pagando {cantidad} con la tarjeta {self.numero}...")
            else:
                print(f"ERROR al pagar con la tarjeta {self.numero}. TARJETA INACTIVA")

        def anular(self):
            if self.activa:
                print(f"Anulando la tarjeta {self.numero}")
                self.activa = False
            else:
                print(f"La tarjeta {self.numero} ya estaba desactivada.")

class Tarjeta_credito(Tarjeta_debito):
    def __init__(self, nombre, numero_tarjeta, fecha_de_caducidad, cvv, activa, saldo, credito):
        super().__init__(nombre, numero_tarjeta, fecha_de_caducidad, cvv, activa, saldo)
        self.credito = 1000

class Bizum:
    def __init__(self, nombre, numero_telefono):
        self.nombre = nombre
        self.numero_telefono = numero_telefono
    def pagar(cantidad):
        print(f"Pagando {cantidad}")

class PayPal:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
    def pagar(self, cantidad):
        print(f"Pagando {cantidad} con usuario {self.nombre} con correo {self.correo}...")