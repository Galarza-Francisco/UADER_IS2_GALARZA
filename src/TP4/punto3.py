from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC): #clase base que declara operaciones comunes para todos los objetos

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Pieza(Component): #clase que representa una pieza componente

    def operation(self) -> str:
        return "Pieza"

class Archivo(Component): # clase que representa un archivo en la estructura del directorio
  
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def operation(self) -> str:
        return f"Archivo: {self.nombre}"

class Composite(Component): #clase que representa un direactorio compuestp por archivos y otros directorios

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Directorio/{' - '.join(results)}"

def client_code(component: Component) -> None: #funcion para mostrar la estructura del directorio
   
    print(component.operation())
    if isinstance(component, Composite):
        for child in component._children:
            client_code(child)

if __name__ == "__main__":
    # crea el directorio principal
    print("Creando el directorio principal")
    directorio_principal = Composite()

    # muestra el directorio principal
    print('')
    print("Directorio principal:")
    client_code(directorio_principal)
    print('')

    # crea carpeta Documentos con algunos archivos
    print("Creando un subdirectorio 'Documentos' con algunos archivos")
    documentos = Composite()
    documentos.add(Archivo("documento1.txt"))
    documentos.add(Archivo("documento2.txt"))
    documentos.add(Archivo("documento3.txt"))

    # agrega el subdirectorio 'Documentos' al directorio principal
    directorio_principal.add(documentos)

    # crea carpeta Imágenes con algunos archivos
    print("Creando un subdirectorio 'Imágenes' con algunos archivos")
    imagenes = Composite()
    imagenes.add(Archivo("imagen1.jpg"))
    imagenes.add(Archivo("imagen2.jpg"))
    imagenes.add(Archivo("imagen3.jpg"))
    print()
    # agrega el subdirectorio 'Imágenes' al directorio principal
    directorio_principal.add(imagenes)
    print()
    # muestro el directorio principal actualizado con los subdirectorios y archivos
    print('')
    print("Directorio principal con subdirectorios y archivos:")
    print('')
    client_code(directorio_principal)
