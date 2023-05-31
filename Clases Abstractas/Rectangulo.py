from figura_geometrica import  FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho:float=0.0, alto:float=0.0):
        super().__init__(ancho=ancho, alto=alto)


    def __str__(self):
        return f'Rectangulo [alto = {self.alto}, ancho = {self.ancho}]'

if __name__ == '__main__':
    r1 =  Rectangulo(ancho=4, alto=6)
    print(r1)