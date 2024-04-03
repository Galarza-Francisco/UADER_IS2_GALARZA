"""
Este archivo brinda la conexion con openAI para poder usar su chat con inteligencia artificial
"""


import sys
import openai #librerias

# apikey
openai.api_key = 'API_KEY'

# Variable para almacenar consultas
bufferConsulta = []

#definicion de la funcion para la respuesta desde la ia
def obtener_respuesta(user_input):

    """
    Descripción de lo que hace esta función.
    
    Args:
        param1: Prompt de entrada proporcionado por el usuario, para el chat.
    
    Returns:
        la respuesta de la IA para el usuario
    """


    # contexto Usuario
    context = "contexto del usuario"
    #tarea Usuario
    usertask = "tarea del usuario"

    # verifica consulta
    if not user_input.strip():
        print("Por favor ingrese una consulta válida.")
        return

    try:
        #Llamada API
        response = openai.ChatCompletion.create( #crea el metodo y manda una solicitud
            model="gpt-3.5-turbo-0125", #modelo de IA implementado
            messages=[
                {"role": "system", "content": context}, #contexto del sistema
                {"role": "user", "content": usertask},  #tarea del usuario
                {"role": "user", "content": user_input} #contenido del prompt
            ],
            temperature=1,#controla la aleatorieidad de las respuestas
            max_tokens=100,#maxima cantiad de tokens en la respuesta generada
            top_p=1,   #controla la prob. acumulada denerando tokens
            frequency_penalty=0, # pesalizaciones para evitar respuestas repetitivas
            presence_penalty=0
        )

        # respuesta GPT
        print("chatGPT:", response.choices[0].message.content)
        bufferConsulta.append(response.choices[0].message.content)
    except ValueError as e:
        print('Error en la respuesta de chat GPT:', e)

# Verifica argumento --convers
conversacion = '--convers' in sys.argv

# Ciclo para seguir preguntando
while True:
    try:
        user_input = input("You: ")
        #pregunta para salir de la conversacion
        if user_input.lower() == 'salir':
            break

        try:
            obtener_respuesta(user_input)

            #si no hay prompt se usa la ultima consulta en buffer
            if conversacion and not user_input.strip() and bufferConsulta:
                user_input = bufferConsulta[-1]
        except ValueError as error:
            print("Error durante la consulta:", error)
    except TypeError as error:
        print("Error en la entrada del usuario:", error)
