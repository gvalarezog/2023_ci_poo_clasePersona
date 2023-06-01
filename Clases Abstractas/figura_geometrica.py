from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    def __init__(self, ancho:float=0.0, alto:float=0.0):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho= ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'Figura Geometrica [{self.__dict__.__str__()}]'

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


if __name__ == '__main__':
    pass
    # fg1 = FiguraGeometrica(2,4)
    # print(fg1)
