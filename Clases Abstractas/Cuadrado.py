from figura_geometrica import  FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado:float=0.0):
        super().__init__(ancho=lado, alto=lado)

    def __str__(self):
        return f'Cuadrado [lado = {self.alto}]'

if __name__ == '__main__':
    c1 =  Cuadrado(lado=4)
    print(c1)