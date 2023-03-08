#Alvaro Fernandez Payo
#19-01-2023

from Pagos import Tarjeta_debito, Bizum, Tarjeta_credito, PayPal

class ShoppingCart:
    def __init__(self):
        #self.cliente = cliente #type: ignore
        self.objetos = []

    def add_objeto(self, objeto):
        self.objetos.append(objeto)

    def remove_objeto(self, objeto):
        self.objetos.remove(objeto)

    def get_total(self):
        total = 0
        for objeto in self.objetos:
            total += objeto.precio
        return total
 
"""
    def checkout(metodo):
        total = self.get_total()
        if metodo == "bizum":
            Bizum.pagar(25)
        elif metodo == "Tarjeta_debito":
            Tarjeta_debito.activar()
            Tarjeta_debito.pagar(25)
        elif metodo == "Tarjeta_credito":
            Tarjeta_credito.pagar(25)
        elif metodo == "paypal":
            PayPal.pagar(25)
        else:
            raise ValueError("Metodo de pago invalido")
"""