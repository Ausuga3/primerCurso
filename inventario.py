print("Bienvenido al inventario")

producto=[]
cantidad=[]
precio=[]

i= True

while i:
    opcion = int(input("Menù de opciones:\n1--Crear Producto\n2--Buscar Producto\n3--Actualizar Producto\n4--Eliminar Producto\n5--Listar Productos\n6--Ordenar por nombre\n7--Invertir Orden\n8--Limpiar Inventario\n9--Salir\nSelecciona una opcion:  "))

    if opcion == 1:

        print("----CREAR PRODUCTO----")

        nombreProducto = input("Ingresa el nombre del producto: ").capitalize()

        cantidadProducto = int(input("Ingresa la cantidad del producto: "))

        precioProducto = float(input("Ingresa el valor del producto: "))

        producto.append(nombreProducto)
        cantidad.append(cantidadProducto)
        precio.append(precioProducto)

        print("----PRODUCTO CREADO CORRECTAMENTE----")

    elif opcion ==2:

        print("----MENÙ DE BUSQUEDA----")

        buscarProducto= input("Ingrese el nombre del producto que buscas: ").capitalize()

        if buscarProducto in producto:
            print("----Producto Encontrado----")

            elemento = producto.index(buscarProducto)

            print("Nombre: ",producto[elemento])

            print("Cantidad: ",cantidad[elemento])

            print("Precio: ",precio[elemento])
        else:
            print("Este producto no existe en nuestra lista")   

    elif opcion ==3:
        print("----MENÙ ACTUALIZACIÒN----")

        buscarProducto= input("Que producto deses actualizar?:_").capitalize()

        if buscarProducto in producto:
            print("----Producto encontrado----") 

            elemento = producto.index(buscarProducto)

            nuevoNombre=input("Ingresa el nuevo nombre del producto: ").capitalize()

            nuevaCantidad=int(input("Ingresa la nueva cantidad: "))
            
            nuevoPrecio = float(input("Ingresa el nuevo precio: "))

            producto[elemento]= nuevoNombre
            cantidad[elemento]= nuevaCantidad
            precio[elemento]  = nuevoPrecio

            print("Producto actualizado ----correctamente----")

        else:
            print("----Producto no encontrado----")


    elif opcion ==4:
        print("----MENÙ ELIMINAR PRODUCTO----") 

        buscarProducto = input("Que prducto deseas eliminar?: ").capitalize()

        if buscarProducto in producto:
            print("----Producto Encontrado----")
            elemento= producto.index(buscarProducto)

            producto.pop(elemento)
            cantidad.pop(elemento)
            precio.pop(elemento)

            print("----Producto Eliminado correctamente----")
        else:
            print("----Producto no encontrado----")

    elif opcion ==5:     
        print("----INVENTARIO----")   

        if producto:
            for p,c,pr in zip(producto,cantidad,precio):
                print(f"Producto {p}\nCantidad {c}\nPrecio {pr}")
        else:
            print("----El inventario esta vacio----")      


    elif opcion ==6:

        producto,cantidad,precio = zip(*sorted(zip(producto,cantidad,precio)))

        

        print("----Ordenados con exito----")

    elif opcion ==7:

       #producto,cantidad,precio = zip(*reversed(zip(producto,cantidad,precio)))
       producto, cantidad, precio = zip(*reversed(list(zip(producto, cantidad, precio))))


       print("----Productos Invertidos Correctamente----")                            


    elif opcion ==8:
        validacion=input("Estas seguro que deseas borrar todo el inventario SI/NO: ").capitalize()

        if validacion == "SI".capitalize():
            producto.clear()
            cantidad.clear()
            precio.clear()
            print("---LOS PRODUCTOS HAN SIDO BORRADOS CORRECTAMENTE----")
        else:
            print("---LOS PRODUCTOS NO HAN SIDO BORRADOS----")

    elif opcion ==9:
        print("----Hasta pronto----")   
        i=False     