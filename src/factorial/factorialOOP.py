import sys

class Factorial:
    def calcular_factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            for i in range(2, num + 1):
                fact *= i
            return fact

    def run(self, min_num, max_num):
        if min_num > max_num:
            print("El número mínimo del rango debe ser menor o igual al máximo.")
            return

        for num in range(min_num, max_num + 1):
            print("Factorial de", num, "! es", self.calcular_factorial(num))

factorial = Factorial()

if len(sys.argv) == 3:
    min_num = int(sys.argv[1])
    max_num = int(sys.argv[2])
else:
    min_num = int(input("Debe ingresar el número mínimo del rango: "))
    max_num = int(input("Debe ingresar el número máximo del rango: "))

factorial.run(min_num, max_num)
