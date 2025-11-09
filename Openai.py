from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))
# Missatge inicial del sistema
messages = [{"role": "system", "content": "Ets un assistent útil i amable."}]

# Pregunta com vols ser tractat
rol = str(input("Com vols que et tractin? (de tu o de vosté): ")).lower()

# Adapta el to segons la resposta
if rol == "vosté":
    messages[0]["content"] = "Ets un assistent formal i respectuós que tracta l'usuari de vosté."
else:
    messages[0]["content"] = "Ets un assistent proper i simpàtic que tracta l'usuari de tu."

print("🤖 ChatGPT està llest! Escriu 'exit' per acabar.\n")

# Bucle principal del xat
while True:
    user_input = input(f"{rol}: ")

    if user_input.lower() == "exit":
        print("ChatGPT: Adéu! 👋")
        break

    # Afegim el missatge de l’usuari a la conversa
    messages.append({"role": "user", "content": user_input})

    try:
        # Petició a l’API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000
        )

        # Mostra la resposta
        reply = response.choices[0].message.content
        print(f"ChatGPT: {reply}\n")

        # Desa la resposta per mantenir el context
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ S'ha produït un error:", e)