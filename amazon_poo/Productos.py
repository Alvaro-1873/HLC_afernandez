#Alvaro Fernandez Payo
#12-01-2023

class producto:
    def __init__(self, nombre, codigo, precio, descripcion):
    self.nombre = nombre
    self.codigo = codigo
    self.precio = precio
    self.descripcion = descripcion

class libros(producto):
    def __init__(self, nombre, codigo, precio, descripcion, genero, autor, ISBN):
        super().__init__(nombre, codigo, precio, descripcion)
        self.genero = genero
        self.autor = autor
        self.ISBN = ISBN

class muebles(producto):
    def __init__(self, nombre, codigo, precio, descripcion, dimensiones, materiales):
        super().__init__(nombre, codigo, precio, descripcion)
        self.dimensiones = dimensiones
        self.materiales =  materiales

class ropa(producto):
    def __init__(self, nombre, codigo, precio, descripcion, talla, genero, temporada):
        super().__init__(nombre, codigo, precio, descripcion)
        self.talla = talla
        self.genero = genero
        self.temporada = temporada

class videojuegos(producto):
    def __init__(self, nombre, codigo, precio, descripcion, desarrolladora, genero, plataforma, edad):
        super().__init__(nombre, codigo, precio, descripcion)
        self.desarrolladora = desarrolladora
        self.genero = genero
        self.plataforma = plataforma
        self.edad = edad