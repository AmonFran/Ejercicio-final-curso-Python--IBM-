# Las clases las tenia en archivos separados, como deberia estar, pero como solo puedo subir un archivo esta todo en el mismo codigo


# Aqui empieza el codigo de las clases
# Clase Producto
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


# Clase Inventario
class Inventario:
    # Creo que no hay mucho que comentar en este codigo, los nombres de los metodos dejan claro que hacen
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


# Aqui empieza el codigo del programa
# Se crea la instancia de Inventario
lista = Inventario()
print("Bienvenido al programa.")
# Ponemos la tarea a realizar a 0 para ejecutar el programa
tarea = 0
while tarea != 6:
    # Empezamos pidiendo la accion, con un try en un bucle para comprobar que se introduce un numero
    print("Introduzca el numero de la accion que desee realizar.")
    aceptado = False
    while aceptado == False:
        try:
            tarea = int(
                input(
                    "1. Agregar un producto. \n2. Actualizar un producto. \n3. Eliminar un producto. \n4. Mostrar inventario. \n5. Buscar un producto. \n6. Salir\n"
                )
            )
        except ValueError:
            print("No has introducido un numero, vuelve a intentarlo")
        except:
            print("Ocurrio un error, vuelva a introducir un numero")
        else:
            aceptado = True
    # Hasta aqui el bucle que comprueba el numero de la accion a realizar
    # Agregar producto
    if tarea == 1:
        nombreProducto = input("Nombre del producto a introducir:")
        categoriaProducto = input("Categoria del producto a introducir:")
        # Bucle para comprobar que el numero introducido es un numero y positivo
        valido = False
        precioProducto = 0
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
        # Bucle para comprobar que el numero introducido es un numero y positivo
        valido = False
        stockProducto = 0
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
        # Se añade el producto
        print(
            lista.agregarProducto(
                Producto(
                    nombreProducto.capitalize(),
                    categoriaProducto.capitalize(),
                    precioProducto,
                    stockProducto,
                )
            )
        )

    # Actualizar producto
    elif tarea == 2:
        nombreProducto = input("Nombre del producto a actualizar:")
        productoBuscado = lista.buscarProducto(nombreProducto)
        if productoBuscado != -1:
            print("Producto encontrado -> {0}".format(productoBuscado))
            print("Que quieres actualizar")
            modificacion = 0
            valido = False
            while valido == False:
                try:
                    modificacion = int(
                        input("1. Modificar precio. \n2. Modificar stock\n")
                    )
                except ValueError:
                    print("No has introducido un numero, vuelve a intentarlo")
                except:
                    print("Ocurrio un error, vuelva a introducir un numero")
                else:
                    valido = True
                    if modificacion != 1 and modificacion != 2:
                        valido = False
                        print("No has introducido ninguno de las opciones propuestas")

            if modificacion == 1:
                # Bucle para comprobar que el numero introducido es un numero y positivo
                valido = False
                precioProducto = 0
                while valido == False and precioProducto <= 0:
                    try:
                        precioProducto = int(input("Nuevo precio:"))
                    except:
                        valido = False
                        print("No has introducido un numero")
                    else:
                        if precioProducto <= 0:
                            print("Numero no valido")
                        else:
                            valido = True
                # Cierre bucle de comprobacion
                lista.modificarProducto(
                    productoBuscado.getNombre(),
                    precioProducto,
                    productoBuscado.getStock(),
                )
            elif modificacion == 2:
                # Bucle para comprobar que el numero introducido es un numero y positivo
                valido = False
                stockProducto = 0
                while valido == False and stockProducto <= 0:
                    try:
                        stockProducto = int(input("Nuevo stock:"))
                    except:
                        valido = False
                        print("No has introducido un numero")
                    else:
                        if stockProducto <= 0:
                            print("Numero no valido")
                        else:
                            valido = True
                # Cierre bucle de comprobacion
                lista.modificarProducto(
                    productoBuscado.getNombre(),
                    productoBuscado.getPrecio(),
                    stockProducto,
                )
        else:
            print("Producto no encontrado")

    # Eliminar producto
    elif tarea == 3:
        nombreProducto = input("Nombre del producto a eliminar:")
        print(lista.eliminarProducto(nombreProducto))

    # Mostrar inventario
    elif tarea == 4:
        if len(lista.getLista()) > 0:
            lista.mostrarInventario()
        else:
            print("No hay productos en el inventario")

    # Buscar producto
    elif tarea == 5:
        nombreProducto = input("nombre del producto a buscar:")
        productoBuscado = lista.buscarProducto(nombreProducto)
        if productoBuscado != -1:
            print("Producto encontrado -> {0}".format(productoBuscado))
        else:
            print("Producto no encontrado")

    # Terminar programa
    elif tarea == 6:
        print("Saliendo del programa...")

    # Mensaje de numero distinto
    else:
        print("El numero introducido no equivale a ninguna accion")
