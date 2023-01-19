from tarjeta import Tarjeta
from credito import TarjetaCredito

# Instanciar una clase --> Crear un objeto
tarjeta1=Tarjeta("ING", "Laura Paneque", "1234123412341234","12/24",455) # OBJETO   
tarjeta2=Tarjeta("BBVA", "Pepito Grillo", "23562356223562356","11/25",422) # OBJETO

print(tarjeta1)



# Con el objeto seguido de punto accedemos al contenido del objeto, atributos y métodos

'''print(type(tarjeta1))
tarjeta1.activar() # Invocar un método del objeto tarjeta1
tarjeta1.pagar(50)
tarjeta1.activar() 
tarjeta1.anular()
tarjeta1.pagar(20)
tarjeta1.anular()
print(tarjeta1.titular)
tarjeta1.recargar(1000)
print(tarjeta1.saldo)'''

tarjeta_credito_1=TarjetaCredito("Santander", "Manolito Gafotas", "23562356223562356","11/25",422,500)
print(f"La tarjeta {tarjeta_credito_1.numero} tiene {tarjeta_credito_1.credito} € de crédito")

print(tarjeta_credito_1)

