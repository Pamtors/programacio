import os
import ast
from google import genai
from google.genai import types

MODEL_ID = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = (
    "Ets una eina que només genera llistes Python amb dades de prova. "
    "Respon ÚNICAMENT amb la llista, sense markdown, sense text addicional "
    "ni assignacions de variables."
)

# Aquí tenim el magatzem de memòria de datasets
datasets = {}

# REVISAR DESPRES
def get_client():
    """Configura i retorna el client de l'API de Gemini."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: No s'ha trobat la variable d'entorn 'GEMINI_API_KEY'.")
        print("Configura-la abans de continuar.")
        return None

    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Error inicialitzant el client: {e}")
        return None


def generar_dataset(client):
    """Opció 1. Generar un nou set de dades."""
    print("\n------------------------------")
    print("Generació d'un nou set")
    print("------------------------------")

    nom_set = input("Introdueix un nom per al set de dades: ").strip()
    if not nom_set:
        print("El nom no pot estar buit.")
        return

    if nom_set in datasets:
        print(f"Ja existeix un set amb el nom '{nom_set}'.")
        return

    print("\nQuin tipus de dada vols que sigui?")
    print("1 - Enters")
    print("2 - Decimals")
    print("3 - Text")
    tipus_opcio = input("Tipus de dada: ").strip()

    if tipus_opcio == "1":
        tipus_str = "números enters (int)"
    elif tipus_opcio == "2":
        tipus_str = "números decimals (float)"
    elif tipus_opcio == "3":
        tipus_str = "cadenes de text (string)"
    else:
        print("Opció no vàlida.")
        return

    try:
        quantitat = int(input("Quants elements vols? "))
        if quantitat <= 0:
            print("La quantitat ha de ser més gran que zero.")
            return
    except ValueError:
        print("La quantitat ha de ser un número enter.")
        return

    tema = input("Quines dades necessites que et generi?\n> ").strip()
    if not tema:
        print("La descripció no pot estar buida.")
        return

    # Definim el prompt, IMPORTANT REVISAR DESPRES..
    prompt = (
        f"Genera una llista Python amb {quantitat} elements. "
        f"El tipus de dades ha de ser {tipus_str}. "
        f"El tema de les dades és: '{tema}'. "
        "La sortida ha de ser estrictament una llista Python vàlida."
    )

    print("\nGenerant dades... si us plau, espera.\n")

    # AJUDA
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7
            ),
            contents=[prompt]
        )

        text_resposta = response.text.strip()
        text_resposta = text_resposta.replace("```python", "").replace("```", "").strip()

        llista_generada = ast.literal_eval(text_resposta)

        if isinstance(llista_generada, list):
            datasets[nom_set] = llista_generada
            print(f'Set "{nom_set}" guardat correctament!')
        else:
            print("La resposta no és una llista vàlida.")

    except (SyntaxError, ValueError):
        print("Error: la IA no ha retornat una llista Python vàlida.")
        print("Resposta rebuda:", text_resposta)
    except Exception as e:
        print(f"Error de connexió o generació: {e}")


def visualitzar_datasets():
    """Opció 2: Visualitzar sets de dades."""
    print("\n------------------------------")
    print("Visualitzar Sets de Dades")
    print("------------------------------")

    if not datasets:
        print("No hi ha sets de dades guardats.")
        return

    print("1 - Visualitzar un set concret")
    print("2 - Visualitzar tots els sets")
    opcio = input("Opció: ").strip()

    if opcio == "1":
        print("\nSets disponibles:")
        for nom in datasets:
            print(f"- {nom}")

        nom_triat = input("Quin vols visualitzar? ").strip()
        if nom_triat in datasets:
            llista = datasets[nom_triat]
            print(f"\nSet: {nom_triat}")
            print(f"Dades: {llista}")
            print(f"Numero d'elements: {len(llista)}")
        else:
            print("Aquest set no existeix.")

    elif opcio == "2":
        for nom, llista in datasets.items():
            print(f"\nSet: {nom}")
            print(f"Dades: {llista}")
            print(f"Numero d'elements: {len(llista)}")
    else:
        print("Opció no vàlida.")


def esborrar_datasets():
    """Opció 3: Esborrar sets de dades."""
    print("\n------------------------------")
    print("Esborrar Sets de Dades")
    print("------------------------------")

    if not datasets:
        print("No hi ha sets per esborrar.")
        return

    print("1 - Esborrar un set concret")
    print("2 - Esborrar tots els sets")
    opcio = input("Opció: ").strip()

    if opcio == "1":
        print("\nSets disponibles:")
        for nom in datasets:
            print(f"- {nom}")

        nom_triat = input("Quin vols esborrar? ").strip()
        if nom_triat in datasets:
            del datasets[nom_triat]
            print(f"Set '{nom_triat}' eliminat.")
        else:
            print("Aquest set no existeix.")

    elif opcio == "2":
        datasets.clear()
        print("Tots els sets han estat eliminats.")
    else:
        print("Opció no vàlida.")


def mostrar_menu():
    """Mostra el menú principal."""
    print("\n------------------------------")
    print("Generador de Sets de Dades")
    print("------------------------------")
    print("1. Generar un nou set de dades")
    print("2. Visualitzar un o tots els sets de dades")
    print("3. Esborrar un o tots els sets de dades")
    print("4. Sortir")


def main():
    client = get_client()
    if not client:
        return

    while True:
        try:
            mostrar_menu()
            opcio = input("Tria una opció: ").strip()

            if opcio == "1":
                generar_dataset(client)
            elif opcio == "2":
                visualitzar_datasets()
            elif opcio == "3":
                esborrar_datasets()
            elif opcio == "4":
                print("\nTancant el programa. Fins aviat!")
                break
            else:
                print("Opció no vàlida, torna-ho a provar.")
        except KeyboardInterrupt:
            print("\nPrograma interromput per l'usuari.")
            break
        except Exception as e:
            print(f"Error inesperat: {e}")


if __name__ == "__main__":
    main()
