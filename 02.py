print("Bienvenido al inventario")

producto=[]
cantidad=[]
precio=[]

i= True

while i:
    opcion = int(input("Menù de opciones:\n1--Crear Producto\n2--Buscar Producto\n3--Actualizar Producto\n4--Eliminar Producto\n5--Listar Productos\n6--Ordenar por nombre\n7--Invertir Orden\n8--Limpiar Inventario\n9--Salir\nSelecciona una opcion:  "))


    if opcion == 1:
        nombreProducto=input("Ingrese nombre: ").capitalize()
        cantidadProducto=int(input("Ingrese cantidad: "))
        precioProducto=float(input("Ingrese precio: " ))

        producto.append(nombreProducto)
        cantidad.append(cantidadProducto)
        precio.append(precioProducto)

    elif opcion ==2:
        buscarProducto=input("que producto buscas: ").capitalize()

        if buscarProducto in producto:
            elemento = producto.index(buscarProducto)

            print (f"Nombre: {producto[elemento]}")
            print ("Cantidad: ",cantidad[elemento])
            print("Precio: ",precio[elemento])
        else:
            print("No encontre el producto")    


    elif opcion ==3:
        buscarProducto=input("que producto quieres actualizar: ").capitalize()

        if buscarProducto in producto:
            elemento = producto.index(buscarProducto)

            nuevoNombre=input("Ingrese el nuevo nombre: ").capitalize()
            nuevaCantidad=input("Ingrese la nueva cantidad: ")
            nuevoPrecio=input("Nuevo precio: ")

            producto[elemento]=nuevoNombre
            cantidad[elemento]=nuevaCantidad
            precio[elemento]  =nuevoPrecio

            print("Actualizados con exito")

        else:
            print("No encontre el producto")



    elif opcion==4:
        buscarProducto=input("que producto quieres borrar: ").capitalize()

        if buscarProducto in producto:
            elemento = producto.index(buscarProducto)

            producto.pop(elemento)
            cantidad.pop(elemento)
            precio.pop(elemento)
            print("Prodcuto eliminado correctamente")

        else:
            print("No encontre el producto")   


    elif opcion ==5:
        if producto:
            for n,c,p in zip(producto,cantidad,precio):
                print(f"Producto: {n} Cantidad:{c} Precio: {p}")
        else:
            print("inventario vacio")        

    elif opcion ==6:
      producto,cantidad,precio=zip(*sorted(zip(producto,cantidad,precio))) 
      print("Ordenados correctamente, ve a la opcion 5 para visualizarlo")

    elif opcion ==7:
        producto,cantidad,precio=zip(*sorted(zip(producto,cantidad,precio)))
        producto.reverse()
        cantidad.reverse()
        precio.reverse()

        print("Revertidos correctamente")  

    elif opcion ==8:
        producto.clear()
        cantidad.clear()
        precio.clear()

    elif opcion ==9:
        print("adios")
        i=False        