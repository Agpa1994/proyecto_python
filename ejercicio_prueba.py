opcion = 0

while opcion != 2: 
    print("-- MENÚ TIENDA RETAIL --")
    print("1. Registrar compra")
    print("2. Salir") 
   
    try:
        opcion = int(input("Selecciones una opción: "))
    except: 
        print("Error: debe ingresar un número entero.")
        opcion = 0

    if opcion == 1:
        print("Registro de compra")
        monto_valido = False
        while monto_valido == False:
            try: 
                monto = int(input("Ingrese monto de compra: "))
                if monto > 0:
                    monto_valido = True
                else:
                    print("Error: el monto debe ser mayor a cero.")
            except:
                print("Error: debe ingresar un número entero.")
        tipo_cliente = input("Ingrese tipo de cliente (premium/socio/normal): ")
        tipo_cliente = tipo_cliente.lower().strip()
        if tipo_cliente == "premium": 
            porcentaje = 0.20
        elif tipo_cliente == "socio":
            porcentaje = 0.10
        elif tipo_cliente == "normal":
            porcentaje = 0 
        else:
            porcentaje = 0 
            print("Tipo de cliente no reconocido. No se aplicará descuento.")
        descuento = monto * porcentaje
        total = monto - descuento 
        print("Descuento aplicado: ", int(descuento))
        print("Total a pagar: ", int(total))
        
    elif opcion == 2: 
        print("Gracias por usar el sistema.")
    else: 
        print("Opción inválida")
    
    