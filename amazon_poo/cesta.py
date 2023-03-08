#Alvaro Fernandez Payo
#19-01-2023

from Pagos import Tarjeta_debito, Bizum, Tarjeta_credito, PayPal

class ShoppingCart:
    def __init__(self,cliente):
        self.cliente = cliente
        self.objetos = []
        self.total = 0

    def add_objeto(self, objeto):
        self.objetos.append(objeto)

    def remove_objeto(self, objeto):
        self.objetos.remove(objeto)

    def get_total(self):
        total = 0
        for objeto in self.objetos:
            total += objeto.precio
        return total

    def pagotarjeta(self, metodo):
        for productos in self.objetos:
            print(productos)
        print(f"El total de la cesta es {self.get_total()}")
        print(f"Ha realizado el pago con la tarjeta de {metodo.nombre} con numero de cuenta {metodo.numero_tarjeta}")
        metodo.activar()
        metodo.pagar(self.get_total())

    def pagobizum(self, metodo):
        for productos in self.objetos:
            print(productos)
        print(f"El total de la cesta es {self.get_total()}")
        print(f"Ha realizado el pago con el bizum de {metodo.nombre} con numero {metodo.numero_telefono}")
        metodo.pagar(self.get_total())

    def pagopaypal(self, metodo):
        for productos in self.objetos:
            print(productos)
        print(f"El total de la cesta es {self.get_total()}")
        print(f"Ha realizado el pago con el paypal de {metodo.nombre} con el correo {metodo.correo}")
        metodo.pagar(self.get_total())