class Vehiculo:
    def __init__(self, marca: str = None, modelo: str = None, color: str = None, precio: float = None):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._precio = precio

    def __str__(self):
        return f"Marca: {self._marca}\nModelo: {self._modelo}\nColor: {self._color}\nPrecio: {self._precio}"

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, marca: str):
        if not isinstance(marca, str):
            raise ValueError("El atributo 'marca' debe ser de tipo str.")
        self._marca = marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, modelo: str):
        if not isinstance(modelo, str):
            raise ValueError("El atributo 'modelo' debe ser de tipo str.")
        self._modelo = modelo

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        if not isinstance(color, str):
            raise ValueError("El atributo 'color' debe ser de tipo str.")
        self._color = color

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, precio: float):
        if precio is not None and not isinstance(precio, float):
            # raise ValueError("El atributo 'precio' debe ser de tipo float.")
            print('El atributo "precio" debe ser de tipo float.')
        else:
            self._precio = precio


# Crear una instancia de Vehiculo con atributos opcionales
mi_vehiculo = Vehiculo(marca="Toyota", modelo="Camry", color="Rojo", precio=30000.0)

# Modificar el atributo 'precio' con un tipo no válido
mi_vehiculo.precio = 25000 # Lanza una excepción ValueError

# Imprimir el objeto utilizando el método __str__
print(mi_vehiculo)
