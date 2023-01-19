class Tarjeta: # PLANTILLA PARA CREAR OBJETOS
    # Atributos de clase

    # Constructor -> Inicializa el objeto
    def __init__(self,entidad,titular,numero,caducidad,cvv):
        self.entidad = entidad  # Atributos de instancia (del objeto)
        self.titular = titular
        self.numero = numero
        self.caducidad = caducidad
        self.cvv = cvv
        self.activa = False 
        self.saldo = 0
    
    def __str__(self):
        return f"Entidad: {self.entidad}, Titular: {self.titular}, Numero: {self.numero}"

    # Métodos -->  COMPORTAMIENTO DE LOS OBJETOS
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
    
    def recargar(self, importe):
        self.saldo+=importe





