
class Color:
    def __init__(self, color: str = None):
        self._color = color

    def __str__(self):
        return f"Color: {self._color}"

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    def pintar(self, color):
        self.color = color

if __name__ == '__main__':
    # Crear una instancia de Color
    mi_color = Color("Rojo")

    # Acceder al atributo 'color'
    print(mi_color.color)  # Rojo

    # Modificar el atributo 'color'
    mi_color.color = "Azul"

    # Imprimir el objeto utilizando el método __str__
    print(mi_color)