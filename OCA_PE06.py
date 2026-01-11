import random

#CONSTANTS
FINAL = 63
OQUES = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
PONTS = [6, 12]

#INICI
def tirar_daus(posicio):
#Tira un o dos daus segons la posició
    if posicio >= 60:
        dau = random.randint(1, 6)
        return dau, 0, dau
    else:
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1, d2, d1 + d2

def seguent_oca(posicio):
    for oca in OQUES:
        if oca > posicio:
            return oca
    return posicio


def altre_pont(posicio):
    return PONTS[1] if posicio == PONTS[0] else PONTS[0]


# PROGRAMA
def main():
    print("L'OCA")

    # Nombre de jugadors
    while True:
        try:
            num_jugadors = int(input("Introdueix el nombre de jugadors (2-4): "))
            if 2 <= num_jugadors <= 4:
                break
            else:
                print("El nombre ha d'estar entre 2 i 4.")
        except ValueError:
            print("Introdueix un número vàlid.")

    # Jugadors
    noms = []
    posicions = [0] * num_jugadors
    penalitzacions = [0] * num_jugadors
    primera_tirada = [True] * num_jugadors

    # for i in range()
    for i in range(num_jugadors):
        nom = input(f"Nom del jugador {i + 1}: ")
        noms.append(nom)

    torn = 0
    guanyador = False

    

    # BUCLE PRINCIPAL DEL JOC

    while not guanyador:
        print("\n" + "_" * 50)
        print(f"És el torn del jugador {torn + 1}, {noms[torn]}")

        # Penalització de torn
        if penalitzacions[torn] > 0:
            penalitzacions[torn] -= 1
            print("Perds el torn. Penalització restant:", penalitzacions[torn])
            torn = (torn + 1) % num_jugadors
            continue

        input(">> Escriu 'tiro' per llançar els daus ")

        d1, d2, avanc = tirar_daus(posicions[torn])
        if d2 == 0:
            print(f"Has obtingut un {d1}")
        else:
            print(f"Has obtingut un {d1} i un {d2} = {avanc}")

        # Daus especials a la primera tirada
        # Fem Servir el sorted() per ordenador de menor a major, no importa el ordre
        if primera_tirada[torn]:
            if sorted([d1, d2]) == [3, 6]:
                posicions[torn] = 26
                print("De dau a dau i tiro perquè m'ha tocat (casella 26)")
                primera_tirada[torn] = False
                continue
            if sorted([d1, d2]) == [4, 5]:
                posicions[torn] = 53
                print("De dau a dau i tiro perquè m'ha tocat (casella 53)")
                primera_tirada[torn] = False
                continue

        primera_tirada[torn] = False
        nova_posicio = posicions[torn] + avanc

        # Rebot si es passa de 63
        if nova_posicio > FINAL:
            nova_posicio = FINAL - (nova_posicio - FINAL)

        posicions[torn] = nova_posicio
        print(f"Avances fins a la casella {nova_posicio}")


        # CASELLES ESPECIALS
        if nova_posicio in OQUES:
            print("Oca: De oca en oca i tiro perquè em toca")
            posicions[torn] = seguent_oca(nova_posicio)
            print(f"Avances fins a la casella {posicions[torn]}")
            continue

        if nova_posicio in PONTS:
            print("Pont: De pont a pont i tiro perquè em porta la corrent")
            posicions[torn] = altre_pont(nova_posicio)
            print(f"Vas fins a la casella {posicions[torn]}")
            continue

        if nova_posicio == 19:
            print("Fonda: perds un torn")
            penalitzacions[torn] = 1

        elif nova_posicio == 31:
            print("Pou: perds dos torns")
            penalitzacions[torn] = 2

        elif nova_posicio == 42:
            print("Laberint: tornes a la casella 39")
            posicions[torn] = 39

        elif nova_posicio == 52:
            print("Presó: perds tres torns")
            penalitzacions[torn] = 3

        elif nova_posicio == 58:
            print("La mort: tornes a l'inici")
            posicions[torn] = 0

        elif nova_posicio == 63:
            print(f"{noms[torn]} ha guanyat el joc!")
            guanyador = True
            break

        torn = (torn + 1) % num_jugadors



if __name__ == "__main__":
    main()
