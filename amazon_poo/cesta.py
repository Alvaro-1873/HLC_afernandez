#Alvaro Fernandez Payo
#19-01-2023

from Pagos import Tarjeta_debito, Bizum, Tarjeta_credito, PayPal

tarjetadebi_1=Tarjeta_debito("Paco",1234567890,"10/26",123,10000)
tarjetadebi_2=Tarjeta_debito("Juan",1234567890,"10/26",123,10000)
tarjetadebi_3=Tarjeta_debito("Manolo",1234567890,"10/26",123,10000)
tarjetadebi_4=Tarjeta_debito("Raul",1234567890,"10/26",123,10000)

class ShoppingCart:
    def __init__(self):
        self.cliente = cliente #type: ignore
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
            Tarjeta_debito.activar()
            Tarjeta_debito.pagar(25)
        elif metodo == "Tarjeta_credito":
            Tarjeta_credito.pagar(25)
        elif metodo == "paypal":
            PayPal.pagar(25)
        else:
            raise ValueError("Metodo de pago invalido")

#ShoppingCart.checkout("Tarjeta_debito")