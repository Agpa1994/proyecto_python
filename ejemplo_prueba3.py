participante_avanzado = 0 
participante_inicial = 0 

while True:
    try:
        cantidad_participantes = int(input("Ingrese la cantidad de participantes: "))
        if cantidad_participantes <= 0:
            print("cantidad inválida, debe ser un número entero positivo")
        else:
            print("Se han agregado ", cantidad_participantes, " participantes")
            break
    except:
        print("cantidad inválida, debe ser un número entero positivo")

for i in range(cantidad_participantes):
    print(i + 1, "° participante")
    while True:
        nombre = input("Ingrese el nombre del participante: ")
        if not nombre:
            print("El nombre no puede estar vacío")
            continue
        break
    #Alias 
    while True:
        alias = input("Ingrese el alias del participante (min 5 caracteres, sin espacio): ").strip()
        if len(alias) < 5 or ' ' in alias:
            print("El alias debe tener al menos 5 caracteres y no debe contener espacios")
            continue
        else:
            break
    #Edad 
    while True:
        try: 
                edad = int(input("Ingrese la edad del participante: "))
                if edad <= 0:
                    print("Edad inválida, debe ser un número entero positivo")
                else:
                    break
        except:
                print("Edad inválida, debe ser un número entero positivo")

    #Puntaje obtenido
    while True:
        try: 
            puntaje_obtenido = int(input("Ingrese el puntaje obtenido por el participante: ")) 
            if puntaje_obtenido < 0:
                print("Puntaje inválido, debe ser un número entero positivo")
            else:
                if puntaje_obtenido >= 70:
                    print("El participante ", nombre, " con alias ", alias, " y edad ", edad, " obtuvo un puntaje de ", puntaje_obtenido, " y es un participante avanzado")
                    participante_avanzado = participante_avanzado + 1
                else:
                    print("El participante ", nombre, " con alias ", alias, " y edad ", edad, " obtuvo un puntaje de ", puntaje_obtenido, " y es un participante inicial")
                    participante_inicial = participante_inicial + 1
  
            break
        except:
            print("Puntaje inválido, debe ser un número entero positivo")
    

#salida final
print("Cantidad de participantes avanzados: ", participante_avanzado)
print("Cantidad de participantes iniciales: ", participante_inicial)