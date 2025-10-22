def inicio():
    print("Estás frente a un laberinto.")
    opcion = input("¿Quieres entrar por la primera puerta? (s/n): ").lower()
    if opcion == 's':
        pasillo_inicial()
    else:
        print("Decides no entrar al laberinto. Fin del juego.")

def pasillo_inicial():
    print("\nEstás en un pasillo con dos puertas.")
    print("1. Puerta de la izquierda")
    print("2. Puerta de la derecha (volver)")
    opcion = input("¿Qué puerta eliges? (1/2): ")
    if opcion == '1':
        pasillo_interior()
    elif opcion == '2':
        inicio()
    else:
        print("Opción no válida.")
        pasillo_inicial()

def pasillo_interior():
    print("\nHas entrado al pasillo interior. Hay dos puertas y puedes volver.")
    print("1. Puerta de la izquierda (activar palanca)")
    print("2. Puerta de delante (peligro)")
    print("3. Volver al pasillo inicial")
    opcion = input("¿Qué puerta eliges? (1/2/3): ")
    if opcion == '1':
        activar_palanca()
    elif opcion == '2':
        morir()
    elif opcion == '3':
        pasillo_inicial()
    else:
        print("Opción no válida.")
        pasillo_interior()

def activar_palanca():
    print("\nEntras en la sala, activas la palanca y vuelves al pasillo interior.")
    pasillo_interior()

def morir():
    print("\nHas entrado en la puerta de delante... ¡Es una trampa! Has muerto.")
    print("Fin del juego.")

# Inicia el juego
inicio()
