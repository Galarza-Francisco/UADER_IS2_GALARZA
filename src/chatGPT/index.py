import openai

# apikey
openai.api_key = 'OPENAI_API_KEY'

def obtener_respuesta(user_input):
    # contexto y tatea
    context = "contexto del usuario"
    usertask = "tarea del usuario"

    #verifica consulta
    if not user_input.strip():
        print("Por favor ingrese una consulta válida.")
        return

    try:
        # llamada api
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": usertask},
                {"role": "user", "content": user_input}
            ],
            temperature=1,
            max_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # respuesta gpt
        print("chatGPT:", response.choices[0].message.content)
    except Exception as e:
        print('error en la respuesta de chat gpt', e)

# ciclo para seguir preguntando
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'salir':
            break

        try:
            obtener_respuesta(user_input)
        except Exception as e:
            print("error durante la consulta", e)

    except Exception as e:
        print("error en la entrada del ususario:", e)