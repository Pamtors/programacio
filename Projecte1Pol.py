# Variables de estado
palanca1_activada = False
palanca2_activada = False
ha_muerto = False
juego_terminado = False

print("Estás frente a un misterioso laberinto.")
opcion = input("¿Quieres entrar por la primera puerta? (s/n): ").lower()

if opcion != 's':
    print("Decides no entrar al laberinto. Fin del juego.")
    juego_terminado = True

# Bucle principal del juego
ubicacion = "entrada"

while not juego_terminado:
    
    if ubicacion == "entrada":
        print("\nEstás en un pasillo con dos puertas.")

        if palanca1_activada:
            print("La puerta de la izquierda está bloqueada. Solo puedes ir por la derecha.")
            opcion = '2'
        else:
            print("1. Puerta de la izquierda")
            print("2. Puerta de la derecha")
            opcion = input("¿Qué puerta eliges? (1/2): ")

        if opcion == '1' and not palanca1_activada:
            print("\nHas entrado por la puerta de la izquierda.")
            opcion = input("¿Quieres entrar al pasillo? (s/n): ").lower()
            if opcion == 's':
                ubicacion = "pasillo_izquierda"
            else:
                ubicacion = "entrada"

        elif opcion == '2':
            print("\nHas entrado por la puerta de la derecha.")
            opcion = input("¿Quieres seguir por el pasillo o volver? (seguir/volver): ").lower()
            if opcion == "seguir":
                ubicacion = "pasillo_derecha"
            else:
                ubicacion = "entrada"
        else:
            print("Opción no válida.")

    elif ubicacion == "pasillo_izquierda":
        print("\nEstás en un pasillo con dos puertas.")
        print("1. Puerta de la izquierda (puede haber algo útil)")
        print("2. Puerta de delante (¿seguro?)")
        print("3. Volver al inicio")
        opcion = input("¿Qué haces? (1/2/3): ")

        if opcion == '1':
            if not palanca1_activada:
                print("\nHas entrado en una sala. Hay una palanca.")
                print("Activas la palanca 1. Escuchas un ruido en la distancia...")
                palanca1_activada = True
            else:
                print("\nYa activaste esta palanca.")
        elif opcion == '2':
            print("\nHas entrado en una habitación oscura...")
            print("De repente, el suelo desaparece y caes en un pozo sin fin.")
            print("Has muerto. Fin del juego.")
            ha_muerto = True
            juego_terminado = True
        elif opcion == '3':
            ubicacion = "entrada"
        else:
            print("Opción no válida.")

    elif ubicacion == "pasillo_derecha":
        print("\nSigues caminando por el pasillo...")
        opcion = input("¿Quieres seguir caminando o volver? (seguir/volver): ").lower()
        if opcion == "seguir":
            ubicacion = "dos_puertas_finales"
        elif opcion == "volver":
            ubicacion = "entrada"
        else:
            print("Opción no válida.")

    elif ubicacion == "dos_puertas_finales":
        print("\nLlegas a dos puertas al fondo del pasillo.")
        print("1. Puerta de la izquierda")
        print("2. Puerta de la derecha")
        opcion = input("¿Cuál eliges? (1/2): ")

        if opcion == '1':
            if not palanca2_activada:
                print("\nEncuentras otra sala con una palanca.")
                print("Activas la palanca 2.")
                palanca2_activada = True
            else:
                print("\nYa activaste esta palanca.")
        elif opcion == '2':
            if palanca1_activada and palanca2_activada and not ha_muerto:
                print("\nHas llegado a una gran puerta...")
                print("¡Se abre gracias a que activaste ambas palancas!")
                print("¡Felicidades, has completado el laberinto con éxito!")
                juego_terminado = True
            else:
                print("\nLa puerta no se abre.")
                if not palanca1_activada and not palanca2_activada:
                    print("Parece que no has activado ninguna palanca.")
                elif not palanca1_activada:
                    print("Te falta activar la palanca 1.")
                elif not palanca2_activada:
                    print("Te falta activar la palanca 2.")
                print("Deberías seguir explorando el laberinto.")
        else:
            print("Opción no válida.")
