import matplotlib.pyplot as plt  # libreria para graficar


def collatz(n):
    iteraciones = 0
    while n != 1:   
        if n % 2 == 0:   
            n //= 2      
        else:
            n = 3 * n + 1  
        iteraciones += 1   
    return iteraciones   

# calculo collatz
def calcular_collatz_entre_1_y_10000():
    resultado = []  
    for i in range(1, 10001): 
        iteraciones = collatz(i)  # Calculamos la secuencia de Collatz para el número actual
        resultado.append((i, iteraciones)) 
    return resultado   

# graficar los resultados
def graficar_collatz(resultado):
    #el numero de iteraciones es el eje x y los valores los numeros iniciales son el eje y
    valores = [result[0] for result in resultado]
    iteraciones = [result[1] for result in resultado]
    
    plt.scatter(iteraciones, valores)
    # Añadimos título y etiquetas de los ejes
    plt.title('Número de Collatz para números entre 1 y 10000')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número inicial (n)')
    plt.show()      # Mostramos el gráfico

# se calcula la secuencia
resultado = calcular_collatz_entre_1_y_10000()

# Grafica
graficar_collatz(resultado)
