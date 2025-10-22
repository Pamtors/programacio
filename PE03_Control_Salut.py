import datetime

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Introduir dades")
    print("2. Modificar dades")
    print("3. Visualitzar dades")
    print("4. Sortir")

def llegir_nom():
    nom = input("Nom complet: ").strip()
    if not nom:
        print("Error: El nom no pot quedar buit.")
        return None
    if len(nom) < 2:
        print("Error: El nom ha de tenir almenys 2 caràcters.")
        return None
    if len(nom) > 501:
        print("Error: El nom no pot superar els 501 caràcters.")
        return None
    if not all(c.isalpha() or c.isspace() for c in nom):
        print("Error: El nom només pot contenir lletres i espais.")
        return None
    return nom

def llegir_enter_positiu_max(missatge, max_valor):
    valor_str = input(missatge).strip()
    if not valor_str:
        print("Error: Valor no proporcionat.")
        return None
    try:
        valor = int(valor_str)
        if valor <= 0:
            print("Error: Valor mínim 0.")
            return None
        if valor > max_valor:
            print(f"Error: Valor màxim superat {max_valor}.")
            return None
        return valor
    except ValueError:
        print("Error: Valor ha de ser un enter.")
        return None

def llegir_decimal_positiu(missatge, min_valor=None, max_valor=None):
    valor_str = input(missatge).strip().replace(',', '.')
    if not valor_str:
        print("Error: Valor no proporcionat.")
        return None
    try:
        valor = float(valor_str)
        if valor <= 0:
            print("Error: Valor mínim 0.")
            return None
        if min_valor is not None and valor < min_valor:
            print(f"Error: Valor ha de ser com a mínim {min_valor}.")
            return None
        if max_valor is not None and valor > max_valor:
            print(f"Error: Valor màxim superat {max_valor}.")
            return None
        return valor
    except ValueError:
        print("Error: Valor ha de ser decimal.")
        return None

def llegir_sexe():
    sexe = input("Sexe (H/D): ").strip().upper()
    if not sexe:
        print("Error: Valor no proporcionat.")
        return None
    if sexe not in ["H", "D"]:
        print('Error: Valor a proporcionar "H" o "D".')
        return None
    return sexe

def introduir_dades():
    global usuari
    while True:
        nom = llegir_nom()
        if nom is not None:
            break

    while True:
        edat = llegir_enter_positiu_max("Edat: ", 120)
        if edat is not None:
            break

    while True:
        pes = llegir_decimal_positiu("Pes (kg): ", max_valor=400)
        if pes is not None:
            break

    while True:
        alcada = llegir_decimal_positiu("Alçada (m): ", min_valor=0.5, max_valor=2.5)
        if alcada is not None:
            break

    while True:
        sexe = llegir_sexe()
        if sexe is not None:
            break

    usuari = {
        "nom": nom,
        "edat": edat,
        "pes": pes,
        "alcada": alcada,
        "sexe": sexe
    }
    print("✅ Dades guardades correctament.")

def modificar_dades():
    if not usuari:
        print("⚠️ Primer has d'introduir les dades.")
        return

    print("\n--- MODIFICAR DADES ---")
    print("Dades actuals:")
    for k, v in usuari.items():
        if isinstance(v, float):
            print(f"{k.capitalize()}: {v:.2f}")
        else:
            print(f"{k.capitalize()}: {v}")

    camps_possibles = ["nom", "edat", "pes", "alcada", "sexe"]
    camp = input("Quin camp vols modificar? (nom, edat, pes, alcada, sexe): ").strip().lower()

    if camp not in camps_possibles:
        print("⚠️ Camp no vàlid.")
        return

    if camp == "nom":
        while True:
            nou_nom = llegir_nom()
            if nou_nom is not None:
                usuari[camp] = nou_nom
                break

    elif camp == "edat":
        while True:
            nova_edat = llegir_enter_positiu_max("Edat: ", 120)
            if nova_edat is not None:
                usuari[camp] = nova_edat
                break

    elif camp == "pes":
        while True:
            nou_pes = llegir_decimal_positiu("Pes (kg): ", max_valor=400)
            if nou_pes is not None:
                usuari[camp] = nou_pes
                break

    elif camp == "alcada":
        while True:
            nova_alcada = llegir_decimal_positiu("Alçada (m): ", min_valor=0.5, max_valor=2.5)
            if nova_alcada is not None:
                usuari[camp] = nova_alcada
                break

    elif camp == "sexe":
        while True:
            nou_sexe = llegir_sexe()
            if nou_sexe is not None:
                usuari[camp] = nou_sexe
                break

    print("✅ Dades modificades correctament.")

def normalitzar_nom(nom):
    parts = nom.strip().split()
    parts_normalitzats = [p.capitalize() for p in parts if p]
    return ' '.join(parts_normalitzats)

def calcular_imc(pes, alcada):
    imc = pes / (alcada ** 2)
    return round(imc, 2)

def categoria_imc(imc):
    if imc < 18.5:
        return "pes baix"
    elif imc < 25:
        return "pes normal"
    elif imc < 30:
        return "sobrepès"
    else:
        return "obesitat"

def visualitzar_dades():
    if not usuari:
        print("⚠️ Primer has d'introduir les dades.")
        return

    nom_norm = normalitzar_nom(usuari['nom'])
    edat = usuari['edat']
    pes = usuari['pes']
    alcada = usuari['alcada']
    sexe = usuari['sexe']

    imc = calcular_imc(pes, alcada)
    categoria = categoria_imc(imc)

    fc_max = 220 - edat
    zona_fc_50 = round(fc_max * 0.5)
    zona_fc_85 = round(fc_max * 0.85)

    aigua_litres = round((pes * 35) / 1000, 2)

    any_actual = datetime.datetime.now().year
    any_naix = any_actual - edat

    print(f"\nHola, {nom_norm}!")
    print(f"Edat: {edat} anys | Sexe: {sexe}")
    print(f"Pes: {pes:.2f} kg | Alçada: {alcada:.2f} m")
    print(f"IMC: {imc:.2f} ({categoria})")
    print(f"FC màxima estimada: {fc_max} bpm")
    print(f"Zona FC objectiu: {zona_fc_50}–{zona_fc_85} bpm")
    print(f"Aigua recomanada: {aigua_litres:.2f} L/dia")
    print(f"Any de naixement aproximat: {any_naix}")

# Programa principal
usuari = {}
executant = True

while executant:
    mostrar_menu()
    opcio = input("Selecciona una opció (1-4): ").strip()

    if opcio == "1":
        introduir_dades()
    elif opcio == "2":
        modificar_dades()
    elif opcio == "3":
        visualitzar_dades()
    elif opcio == "4":
        print("👋 Sortint del programa. Fins aviat!")
        executant = False
    else:
        print("⚠️ Opció no vàlida. Intenta-ho de nou.")
