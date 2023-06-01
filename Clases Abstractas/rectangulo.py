from figura_geometrica import  FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho:float=0.0, alto:float=0.0):
        super().__init__(ancho=ancho, alto=alto)


    def __str__(self):
        return f'Rectangulo [alto = {self.alto}, ancho = {self.ancho}]'

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return self.alto * 2 + self.ancho * 2

if __name__ == '__main__':
    r1 =  Rectangulo(ancho=4, alto=6)
    print(r1)
    print(f'El área del Rectangulo es: {r1.calcular_area()}')
    print(f'El perimetro del Rectangulo es: {r1.calcular_perimetro()}')