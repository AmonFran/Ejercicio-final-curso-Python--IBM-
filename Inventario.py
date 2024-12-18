# Creo que no hay mucho que comentar en este codigo, los nombres de los metodos dejan claro que hacen
class Inventario():
    def __init__(self):
        self.__listaProductos = []

    def getLista(self):
        return self.__listaProductos

    def agregarProducto(self, producto):
        for a in self.__listaProductos:
            if a.getNombre().lower() == producto.getNombre().lower():
                return "El producto ya existe"
        self.__listaProductos.append(producto)
        return "El producto ha sido añadido correctamente"

    def modificarProducto(self, nombre, precio, stock):
        for a in self.__listaProductos:
            if a.getNombre().lower() == nombre.lower():
                a.setPrecio(precio)
                a.setStock(stock)
                return "Precio y stock del producto '{0}' modificados".format(nombre)
        return "El producto " + nombre + " no existe"

    def eliminarProducto(self, nombre):
        for a in self.__listaProductos:
            if a.getNombre().lower() == nombre.lower():
                self.__listaProductos.remove(a)
                return "El producto " + nombre + " ha sido eliminado correctamente"
        return "El producto " + nombre + " no existe"

    def mostrarInventario(self):
        # Se que es una mala practica realizar prints en las clases, pero es mas facil imprimir la lista directamente en la clase
        print("----------------Inicio lista----------------")
        for a in self.__listaProductos.copy():
            print(a)
        print("----------------Fin lista----------------")

    def buscarProducto(self, nombre):
        for a in self.__listaProductos:
            if a.getNombre().lower() == nombre.lower():
                return a
        return -1
