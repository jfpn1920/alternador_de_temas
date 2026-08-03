import random
ids = []
nombres = []
colores_principales = []
colores_secundarios = []
estados = []
fechas = []
observaciones = []
#----------------------------------------#
#--|menu_principal_alternador_de_temas|--#
#----------------------------------------#
while True:
    print("menu principal alternador de temas")
    print("1) crear tema")
    print("2) editar tema")
    print("3) eliminar tema")
    print("4) buscar tema")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------#
    #--|crear_tema|--#
    #----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_tema = 1
        else:
            id_tema = ids[-1] + 1
        nombre = input("nombre del tema: ")
        color_principal = input("color principal: ")
        color_secundario = input("color secundario: ")
        estado = input("estado (activo o inactivo): ")
        fecha = input("fecha de creación: ")
        observacion = input("observación: ")
        ids.append(id_tema)
        nombres.append(nombre)
        colores_principales.append(color_principal)
        colores_secundarios.append(color_secundario)
        estados.append(estado)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("tema registrado correctamente.")
        print("id:", id_tema)
    #-----------------#
    #--|editar_tema|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar tema")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {colores_principales[i]} | {colores_secundarios[i]} | {estados[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {colores_principales[posicion]} | {colores_secundarios[posicion]} | {estados[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del tema: ")
                colores_principales[posicion] = input("nuevo color principal: ")
                colores_secundarios[posicion] = input("nuevo color secundario: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_tema|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar tema")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {colores_principales[i]} | {colores_secundarios[i]} | {estados[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {colores_principales[posicion]} | {colores_secundarios[posicion]} | {estados[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    colores_principales.pop(posicion)
                    colores_secundarios.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_tema|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar tema")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {colores_principales[posicion]} | {colores_secundarios[posicion]} | {estados[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            activos = 0
            inactivos = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {colores_principales[i]} | {colores_secundarios[i]} | {estados[i]} | {fechas[i]} | {observaciones[i]}")
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
            print()
            print("estadísticas alternador de temas")
            print("cantidad de temas:", len(ids))
            print("temas activos:", activos)
            print("temas inactivos:", inactivos)
            print("primer tema:", nombres[0])
            print("último tema:", nombres[-1])
            for i in range(len(estados)):
                estados[i] = "Inactivo"
            posicion = random.randint(0, len(ids) - 1)
            estados[posicion] = "Activo"
            print("alternando tema...")
            print("tema seleccionado:")
            print(nombres[posicion])
            print("color principal:", colores_principales[posicion])
            print("color secundario:", colores_secundarios[posicion])
            print("estado actual:", estados[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el alternador de temas.")
        break
    else:
        print("opción no válida.")