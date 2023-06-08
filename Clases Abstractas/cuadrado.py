from figura_geometrica import  FiguraGeometrica
from color import Color

class Cuadrado(Color,FiguraGeometrica ):
    def __init__(self, lado:float=0.0, color:str=None):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self, color=color)


    def __str__(self):
        return f'Cuadrado [lado = {self.alto}, color= {self.color}]'

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return 4 * self.alto

if __name__ == '__main__':
    c1 =  Cuadrado(lado=4, color='Rojo')
    print(c1)
    c1.pintar('Negro')
    print(f'El área del Cuadrado es: {c1.calcular_area()} y su color es {c1.color}')
    print(f'El perimetro del Cuadrado es: {c1.calcular_perimetro()}')
    print(Cuadrado.mro())