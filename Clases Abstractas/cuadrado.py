from figura_geometrica import  FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado:float=0.0):
        super().__init__(ancho=lado, alto=lado)

    def __str__(self):
        return f'Cuadrado [lado = {self.alto}]'

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return 4 * self.alto

if __name__ == '__main__':
    c1 =  Cuadrado(lado=4)
    print(c1)
    print(f'El área del Cuadrado es: {c1.calcular_area()}')
    print(f'El perimetro del Cuadrado es: {c1.calcular_perimetro()}')