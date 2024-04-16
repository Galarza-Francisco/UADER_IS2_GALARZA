
#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------


class SingletonMeta(type): #constructor 
    _instances = {}  #se define la instancia
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances: # si la instancia está vacia significa q es la primera vez q se lo llama
            instance = super().__call__(*args, **kwargs) #llama al super constructor
            cls._instances[cls] = instance 
        return cls._instances[cls]


class Factorial(metaclass=SingletonMeta):

    def getFactorial(self,num):
        if num < 0:
            print("No existe factorial de nro negativo")    
        elif num == 0:
            return 1 
        else:
            fact = 1
            while (num > 1):
                fact *= num
                num -=1
            return fact



if __name__ == "__main__":
    s1 = Factorial()
    s2 = Factorial() #se crean los obj
    num = int(input('ingresar un numero '))
    if id(s1) == id(s2):
        print ("Factorial: ", s1.getFactorial(num))
    else:
        print("las variables tienen instancias diferentes")