import math

from figura_geometrica import  FiguraGeometrica

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio:float=0.0, diametro=0.0):
        super().__init__(alto=radio)
        self._diametro = diametro

    @property
    def diametro(self):
        return self._diametro

    @diametro.setter
    def diametro(self, diametro):
        self._diametro = diametro


    def __str__(self):
        return f'Circunferencia [radio = {self.alto}]'

    def calcular_area(self):
        return math.pi * self.alto * self.alto

    def calcular_perimetro(self):
        return 2 * math.pi * self.alto

if __name__ == '__main__':
    cir1 = Circunferencia(radio=6)
    print(cir1)
    print(f'El área de la Circunferencia es: {cir1.calcular_area()}')
    print(f'El perimetro de la Circunferencia es: {cir1.calcular_perimetro()}')