#Alvaro Fernandez Payo
#19-01-2023

from Pagos import Bizum

class ShoppingCart:
    def __init__(self):
        self.cliente = cliente
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
    
    def checkout(metodo):
        #total = self.get_total() + coste_envio
        if metodo == "bizum":
            Bizum.pagar(25)
        elif metodo == "Tarjeta_debito":
            pass
        elif metodo == "Tarjeta_credito":
            pass
        elif metodo == "paypal":
            pass
        else:
            raise ValueError("Metodo de pago invalido")

ShoppingCart.checkout("bizum")