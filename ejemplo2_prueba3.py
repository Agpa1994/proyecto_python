
print("--- Bienvenido al sistema de gestión de salas de reuniones de DUOC UC ---")

def menu():

    print("Menú principal")
    print("1. Salas disponibles")
    print("2. Reservar sala")
    print("3. Liberar salas")
    print("4. Historial")
    print("5. Salir")    

while True:
    
    menu()
    try:
        opcion = int(input("Ingrese una opción del menú: "))
        if opcion == 1:
            print("Salas disponibles", Salas)

        elif opcion == 2:
            while True:
                try:
                    cantidad_salas_reservar = int(input("Ingrese la cantidad de salas que desea reservar: "))
                    if cantidad_salas_reservar <= 0:
                        print("cantidad inválida, debe ser un número entero positivo")
                    elif cantidad_salas_reservar > len(Salas):
                        print("No hay suficientes salas disponibles para reservar")
                    else:
                        print("Se han reservado ", cantidad_salas_reservar, " salas")
                        break
                except:
                    print("cantidad inválida, debe ser un número entero positivo")

        elif opcion == 3:
            print("Ha seleccionado la opción 3: Liberar salas")
        elif opcion == 4:
            print("Ha seleccionado la opción 4: Historial")
        elif opcion == 5:
            print("Ha seleccionado la opción 5: Salir") 
            break
        else: 
            print("Ha seleccionado la opción ", opcion)
    except: 
        print
       


#Salas disponibles
Salas = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
print("Salas disponibles: ", Salas)

#reservar salas
while True:
    try:
        cantidad_salas_reservar = int(input("Ingrese la cantidad de salas que desea reservar: "))
        if cantidad_salas_reservar <= 0:
            print("cantidad inválida, debe ser un número entero positivo")
        elif cantidad_salas_reservar > len(Salas):
            print("No hay suficientes salas disponibles para reservar")
        else:
            print("Se han reservado ", cantidad_salas_reservar, " salas")
            break
    except:
        print("cantidad inválida, debe ser un número entero positivo")


#3 Liberar salas
while True:
    try:
        cantidad_salas_liberar = int(input("Ingrese la cantidad de salas que desea liberar: "))
        if cantidad_salas_liberar <= 0:
            print("cantidad inválida, debe ser un número entero positivo")
        elif cantidad_salas_liberar > cantidad_salas_reservar:
            print("No hay suficientes salas reservadas para liberar")
        else:
            print("Se han liberado ", cantidad_salas_liberar, " salas")
            break 
    except:
        print("Cantidad inválida, debe ser un número entero positivo")
