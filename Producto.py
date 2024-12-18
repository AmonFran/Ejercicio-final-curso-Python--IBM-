class Producto:

    def __init__(self, nombre, categoria, precio, stock):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__stock = stock

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCategoria(self):
        return self.__categoria

    def setNombre(self, categoria):
        self.__categoria = categoria

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, precio):
        self.__precio = precio

    def getStock(self):
        return self.__stock

    def setStock(self, stock):
        self.__stock = stock

    def __str__(self):
        msg = "Nombre producto: {0}, Categoria: {1}, Precio: {2}, Stock:{3}"
        return msg.format(
            self.getNombre(), self.getCategoria(), self.getPrecio(), self.getStock()
        )
