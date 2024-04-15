
#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

class Component(): #la interface de base define las operaciones que pueden modificarse por decoradores

    def operation(self) -> str:
        pass


class Number(Component): # los componentes dan implementaciones predeterminadas para las operaciones

    def __init__(self, number: int) -> None:
        self._number = number

    def operation(self) -> str:
        return str(self._number)


class Decorator(Component): #la clase decoratos sigue la misma interface que los otros componentes

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component: 

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class DecoratorSuma(Decorator): #decorador para sumarle 2 

    def operation(self) -> str:
        return f"Suma({int(self.component.operation()) + 2})"


class DecoratorMultiplicar(Decorator): #decorador para multiplicar x 2


    def operation(self) -> str:
        return f"Multiplicar({int(self.component.operation()) * 2})"


class DecoratorDividir(Decorator): #decorador para dividir

    def operation(self) -> str:
        return f"Dividir({int(self.component.operation()) / 3})"


if __name__ == "__main__":
    
    numero = Number(input('ingresar un numero '))
    print("Número a decorar: ", numero.operation())
    print("\n")

    decorator1 = DecoratorSuma(numero)
    decorator2 = DecoratorMultiplicar(numero)
    decorator3 = DecoratorDividir(numero)

    print("Resultado de las operaciones con el número:")
    print("\n")
    print("Suma:", decorator1.operation())
    print("Multiplicación:", decorator2.operation())
    print("División:", decorator3.operation())
