import os


# clase lamina con metodo de fabricaion flexible  (abstraccion)
class Lamina:
    def __init__(self, thickness, width, produce_laminas):
        self._thickness = thickness
        self._width = width
        self._produce_laminas = produce_laminas

    def produce(self): #cuando invoca, la produccion llama al objeto cuyo puntero se guardo al crear
        self._produce_laminas.produce_laminas(self._thickness, self._width)

    def set_produce_laminas(self, produce_laminas):
        self._produce_laminas = produce_laminas

# Implementación: ProduceLaminas (interfaz de implementación)
class ProduceLaminas:
    def produce_laminas(self, thickness, width):
        pass

# abstraccion de implementacion (implementacion especifica)
class ProduceLaminas5mt(ProduceLaminas):
    def produce_laminas(self, thickness, width):
        print(f'Fabricando una lámina de 5 metros con un grosor de {thickness}" y un ancho de {width} metros')

# # abstraccion de implementacion (implementacion especifica)
class ProduceLaminas10mt(ProduceLaminas):
    def produce_laminas(self, thickness, width):
        print(f'Fabricando una lámina de 10 metros con un grosor de {thickness}" y un ancho de {width} metros')

# inicializa una lamina de grosor, ancho y metodo de produc. seleccionado
class LaminaBridge(Lamina):
    def __init__(self, thickness, width, produce_laminas):
        super().__init__(thickness, width, produce_laminas)


if __name__ == "__main__":
    # intancias de implementacion espcificas para c/u
    produce_laminas_5mt = ProduceLaminas5mt()
    produce_laminas_10mt = ProduceLaminas10mt()

    # creacion de laminas con dif especificaciones
    lamina1 = LaminaBridge(0.5, 1.5, produce_laminas_5mt)
    lamina1.produce()

    lamina2 = LaminaBridge(0.5, 1.5, produce_laminas_10mt)
    lamina2.produce()
