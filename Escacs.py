import random

def qui_comença():

    print("ESCACS")

    noms = []

    for i in range(2):
        nom = input(f"Nom del jugador {i + 1}: ")
        noms.append(nom)

    resposta = input("\nHi ha una partida anterior guanyada? (s/n): ").lower()

    if resposta == "s":
        while True:
            guanyador = input("Qui va guanyar l'última partida?: ")
            if guanyador in noms:
                jugador_blanques = noms.index(guanyador)
                break
            else:
                print("Aquest nom no coincideix amb cap jugador.")
    else:
        jugador_blanques = random.randint(0, 1)

    jugador_negres = 1 - jugador_blanques

    print("\n--- INICI PARTIDA ---")
    print(f"Blanques: {noms[jugador_blanques]}")
    print(f"Negres: {noms[jugador_negres]}")

    return jugador_blanques


# TAULER

def crear_tauler():
    return [["-" for _ in range(8)] for _ in range(8)]


def posar_peons(tauler):

    # Peons negres fila 7 (índex 6)
    for col in range(8):
        tauler[6][col] = "pN"

    # Peons blancs fila 2 (índex 1)
    for col in range(8):
        tauler[1][col] = "pB"


def mostrar_tauler(tauler):

    print("\n    A B C D E F G H")

    for fila in range(7, -1, -1):
        print(fila + 1, end="   ")

        for col in range(8):
            print(tauler[fila][col], end=" ")

        print(f"  {fila + 1}")
        
    print("\n") # PRINT per tenir espai, sinó queda lleig.. sense espai.

    

    #tauler = [ "A","B","C","D","E","F","G","H"
              #0 ["-", "-","-", "-", "-", "-", "-", "-"],
              #1 ["PN", "PN","PN", "PN", "PN", "PN", "PN", "PN"],
              #2 ["-", "-","-", "-", "-", "-", "-", "-"],
              #3 ["-", "-","-", "-", "-", "-", "-", "-"],
              #4 ["-", "-","-", "-", "-", "-", "-", "-"],
              #5 ["-", "-","-", "-", "-", "-", "-", "-"],
              #6 ["PB", "PB","PB", "PB", "PB", "PB", "PB", "PB"],
              #7 ["-", "-","-", "-", "-", "-", "-", "-"],
    #]    

num_columna = ["a","b","c","d","e","f","g","h"]
num_fila = ["0","1","2","3","4","5","6","7"]
#col = coords [0]
#fila = coords [1]
peça_a_moure = num_columna + num_fila

def moviment(tauler):

    peça_a_moure = input("Quina peça vols moure? (Has de dir coordenades, EX: A,1): ").lower()
    if num_columna != 
        print("Has de proporcionar un dels següents valors: A, B, C, D, E, F, G, H ")
    
    if num_fila != 
        print("Has de proporcionar un dels següents valors: 0, 1, 2, 3, 4, 5, 6, 7 ")    
    peça_moviment = input("Ara diguem on la vols moure. Ex: A3: ").lower()

#def moviment_peo():
    # LA POSOCIÓ DE PEÇA_A_MOURE ES QUEDARA EN "-"
    # LA POSICIÓ DE ON VA A PARAR LA PEÇA VE EXPLICADA PER PEÇA_MOVIMENT

#def comprovar_moviment():

# ---------------- MAIN ----------------

if __name__ == "__main__":

    torn = qui_comença()

    tauler = crear_tauler()

    posar_peons(tauler)

    mostrar_tauler(tauler)

    moviment(tauler)
