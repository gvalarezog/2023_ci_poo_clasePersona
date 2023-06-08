from empleado import Empleado


class Cajero(Empleado):
    def __init__(self, email):
        super().__init__(email=email)