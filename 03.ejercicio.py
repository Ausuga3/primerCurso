
print ("INVENTARIO")

i = True 

producto=[]
cantidad=[]
precio=[]


while i:

    menu = int (input(" 1:Crear producto \n 2: Buscar Producto \n 3: Actualizar producto \n 4: Borrar producto \n 5: Mostrar inventario \n 6: Organizar inventario \n 7: Invertir inventario \n 8: Borrar inventario \n 9: Salir \n Elegir Opcion: "))
    
    if menu == 1:

        Nproducto = input ("Nombre del producto: ").capitalize()
        Pcantidad = int   (input ("Cantidad del producto: ")) 
        Pprecio   = float (input("Precio del producto: "))

        producto.append(Nproducto)
        cantidad.append(Pcantidad)
        precio.append(Pprecio)
    
        print (f"Producto creado correctamente: {producto}")

    elif menu == 2:

        buscarProducto = input("Cual producto desea buscar: ").capitalize()

        if buscarProducto in producto:

            element = producto.index(buscarProducto)

            print (f"-----Producto: {producto[element]} \n Cantidad: {cantidad[element] } \n Precio {precio[element]}-----")
        else:
            print ("No se encontro producto")

    elif menu == 3:

        buscarProducto = input ("Ingrese el producto que desea actualizar: ").capitalize()

        if buscarProducto in producto:

            element = producto.index(buscarProducto)

            productoActualizado = input("Ingrese el producto nuevo: ").capitalize()
            cantidadActualizado : int = input("Ingrese cantidad nueva: ")
            precioActualizado : float = input ("Ingrese el precio nuevo: ")

            producto[element] = productoActualizado
            cantidad[element] = cantidadActualizado
            precio[element]   = precioActualizado

            print (f"Producto actualizado: {producto}, \n {cantidad} \n {precio} ")
        else:
            print ( "Producto no encontrado")

    elif menu == 4:

        buscarProducto = input ("Ingrese el producto que desea eliminar: ").capitalize()

        if buscarProducto in producto:

            element = producto.index(buscarProducto) 

            producto.pop(element)
            cantidad.pop(element)
            precio.pop(element)

            print ("Producto eliminado exitosamente ")
        else:
            print(f"Producto no encontrado: {buscarProducto} ")
    elif menu == 5:
        
        for p,c,pr in zip(producto,cantidad,precio):
            print(f"Producto {p} \n Cantidad {c} \n Precio {pr}")

    elif menu == 6:

        producto, cantidad, precio = zip (*sorted(zip(producto,cantidad,precio)))

        for p,c,pr in zip(producto,cantidad,precio):
            print(f"Producto {p} \n Cantidad {c} \n Precio {pr}")

    elif menu == 7:

        producto, cantidad, precio = zip (*reversed(list(zip(producto,cantidad,precio))))

        for p,c,pr in zip(producto,cantidad,precio):
            print(f"Producto {p} \n Cantidad {c} \n Precio {pr}")
    elif menu == 8:

        seguroEliminarP = input (f"Seguro que desea eliminar inventario? \n SI   \n NO").capitalize()

        if seguroEliminarP =="Si":

            producto.clear(), cantidad.clear(), precio.clear() 
        else:
            print ("No se puedo eliminar inventario")

    elif menu == 9:

        print ("Muchas gracias") 

        i=False
           