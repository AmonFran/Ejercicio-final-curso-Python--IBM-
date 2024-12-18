from Producto import Producto
from Inventario import Inventario

lista = Inventario()

nombreProducto = input("Nombre del producto a introducir:")
categoriaProducto = input("Categoria del producto a introducir:")
valido = False
precioProducto = 0
# Bucle para comprobar que el numero introducido es un numero y positivo
while valido == False and precioProducto <= 0:
    try:
        precioProducto = int(input("Precio del producto a introducir:"))
    except:
        valido = False
        print("No has introducido un numero")
    else:
        if precioProducto <= 0:
            print("Numero no valido")
        else:
            valido = True
#
valido = False
stockProducto = 0
# Bucle para comprobar que el numero introducido es un numero y positivo
while valido == False and stockProducto <= 0:
    try:
        stockProducto = int(input("Stock del producto a introducir:"))
    except:
        valido = False
        print("No has introducido un numero")
    else:
        if stockProducto <= 0:
            print("Numero no valido")
        else:
            valido = True


print(
    lista.agregarProducto(
        Producto(nombreProducto, categoriaProducto, precioProducto, stockProducto)
    )
)
lista.mostrarInventario()
