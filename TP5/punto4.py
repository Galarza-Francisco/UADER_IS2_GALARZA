import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

    def tune_to_memory(self, memory):
        frequency = self.memories.get(memory)
        if frequency:
            print("Sintonizando... Frecuencia {} almacenada en memoria {}".format(frequency, memory))
        else:
            print("La memoria {} está vacía".format(memory))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
        self.memories = {"M1": None, "M2": None, "M3": None, "M4": None}

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
        self.memories = {"M1": None, "M2": None, "M3": None, "M4": None}

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def tune_to_memory(self, memory):
        self.state.tune_to_memory(memory)

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions += [lambda: radio.tune_to_memory("M1"), lambda: radio.tune_to_memory("M2"), lambda: radio.tune_to_memory("M3"), lambda: radio.tune_to_memory("M4")]
    actions *= 2


    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
