# Variables de estado
palanca1_activada = False
palanca2_activada = False
ha_muerto = False

def inicio():
    print("Estás frente a un misterioso laberinto.")
    opcion = input("¿Quieres entrar por la puerta principal? (s/n): ").lower()
    if opcion == 's':
        pasillo_entrada()
    else:
        print("Decides no entrar al laberinto. Fin del juego.")

def pasillo_entrada():
    global palanca1_activada

    print("\n Estás en un pasillo con dos puertas.")
    if palanca1_activada:
        print("La puerta de la izquierda está bloqueada. Deberías volver por la puerta de la derecha.")
        puerta_derecha()
        return

    print("1. Puerta de la izquierda")
    print("2. Puerta de la derecha")
    opcion = input("¿Qué puerta eliges? (1/2): ")

    if opcion == '1':
        puerta_izquierda()
    elif opcion == '2':
        puerta_derecha()
    else:
        print("Opción no válida.")
        pasillo_entrada()

# CAMINO POR LA IZQUIERDA
def puerta_izquierda():
    print("\nHas entrado por la puerta de la izquierda.")
    opcion = input("¿Quieres entrar al pasillo? (s/n): ").lower()
    if opcion == 's':
        pasillo_izquierda()
    else:
        pasillo_entrada()

def pasillo_izquierda():
    print("\nEstás en un pasillo con dos puertas.")
    print("1. Puerta de la izquierda (puede haber algo útil)")
    print("2. Puerta de delante (¿seguro?)")
    print("3. Volver al inicio")
    opcion = input("¿Qué haces? (1/2/3): ")

    if opcion == '1':
        activar_palanca1()
    elif opcion == '2':
        morir()
    elif opcion == '3':
        pasillo_entrada()
    else:
        print("Opción no válida.")
        pasillo_izquierda()

def activar_palanca1():
    global palanca1_activada
    if not palanca1_activada:
        print("\nHas entrado en una sala. Hay una palanca.")
        print("Activas la palanca 1. Escuchas un ruido en la distancia...")
        palanca1_activada = True
    else:
        print("\nYa has activado esta palanca.")
    pasillo_izquierda()

# CAMINO POR LA DERECHA
def puerta_derecha():
    print("\nHas entrado por la puerta de la derecha.")
    opcion = input("¿Quieres seguir por el pasillo o volver? (seguir/volver): ").lower()

    if opcion == 'volver':
        pasillo_entrada()
    elif opcion == 'seguir':
        pasillo_profundo()
    else:
        print("Opción no válida.")
        puerta_derecha()

def pasillo_profundo():
    print("\nSigues caminando por el pasillo...")
    opcion = input("¿Quieres seguir caminando o volver? (seguir/volver): ").lower()

    if opcion == 'volver':
        pasillo_entrada()
    elif opcion == 'seguir':
        dos_puertas_finales()
    else:
        print("Opción no válida.")
        pasillo_profundo()

def dos_puertas_finales():
    print("\nLlegas a dos puertas al fondo del pasillo.")
    print("1. Puerta de la izquierda")
    print("2. Puerta de la derecha")
    opcion = input("¿Cuál eliges? (1/2): ")

    if opcion == '1':
        activar_palanca2()
    elif opcion == '2':
        final()
    else:
        print("Opción no válida.")
        dos_puertas_finales()

def activar_palanca2():
    global palanca2_activada
    if not palanca2_activada:
        print("\nEncuentras otra sala con una palanca.")
        print("Activas la palanca 2.")
        palanca2_activada = True
    else:
        print("\nYa has activado esta palanca.")
    dos_puertas_finales()

def final():
    if palanca1_activada and palanca2_activada and not ha_muerto:
        print("\nHas llegado a una gran puerta...")
        print("¡Se abre gracias a que activaste ambas palancas!")
        print("¡Felicidades, has completado el laberinto con éxito!")
    else:
        print("\nLa puerta no se abre.")
        if not palanca1_activada and not palanca2_activada:
            print("Parece que no has activado ninguna palanca.")
        elif not palanca1_activada:
            print("Parece que te falta activar la palanca 1.")
        elif not palanca2_activada:
            print("Parece que te falta activar la palanca 2.")
        print("Deberías regresar y seguir explorando el laberinto.")
        dos_puertas_finales()

def morir():
    global ha_muerto
    ha_muerto = True
    print("\n Has entrado en una habitación oscura...")
    print("De repente, el suelo desaparece y caes en un pozo sin fin.")
    print("Has muerto. Fin del juego.")

# Iniciar el juego
inicio()
