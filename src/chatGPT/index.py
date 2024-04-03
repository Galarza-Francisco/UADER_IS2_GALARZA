import openai
import sys

# apikey
openai.api_key = 'API_KEY'

# Variable para almacenar consultas
bufferConsulta = []

def obtener_respuesta(user_input):
    global bufferConsulta

    # Dcontexto y tarea 
    context = "contexto del usuario"
    usertask = "tarea del usuario"

    # verifica consulta
    if not user_input.strip():
        print("Por favor ingrese una consulta válida.")
        return

    try:
        # Llamada API
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

        # respuesta GPT
        print("chatGPT:", response.choices[0].message.content)
        bufferConsulta.append(response.choices[0].message.content)
    except Exception as e:
        print('Error en la respuesta de chat GPT:', e)

# Verifica argumento --convers
conversacion = '--convers' in sys.argv

# Ciclo para seguir preguntando
while True:
    try:
        user_input = input("You: ")

        if user_input.lower() == 'salir':
            break

        try:
            obtener_respuesta(user_input)

            #si la conv esta activa y no se manda prompt, se usa la ultima consulta del q esta en el buffer

            if conversacion and not user_input.strip() and bufferConsulta:
                user_input = bufferConsulta[-1]
        except Exception as e:
            print("Error durante la consulta:", e)

    except Exception as e:
        print("Error en la entrada del usuario:", e)
