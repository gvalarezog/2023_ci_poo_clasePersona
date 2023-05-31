from figura_geometrica import  FiguraGeometrica

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio:float=0.0):
        super().__init__(alto=radio)


    def __str__(self):
        return f'Circunferencia [radio = {self.alto}]'

if __name__ == '__main__':
    cir1 = Circunferencia(radio=6)
    print(cir1)