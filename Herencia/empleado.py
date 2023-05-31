from Herencia.persona import Persona



class Empleado(Persona):
    contador_empleado = 0
    def __init__(self, sueldo:float=0.0, cedula:str='', email:str=None, nombre:str=None, apellido:str=None
                 , genero:str=None, ocupacion:str=None):
        super().__init__(cedula=cedula, email=email, nombre=nombre, apellido=apellido, genero=genero
                         , ocupacion=ocupacion)
        # Empleado.contador_empleado = Empleado.contador_empleado + 1
        Empleado.contador_empleado += 1
        self._id = Empleado.contador_empleado
        self._sueldo = sueldo

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, id):
    #     self._id = id

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: {self.__dict__.__str__()}'

if __name__ == '__main__':
    objEmpleado = Empleado(nombre='Luis', genero='Masculino', ocupacion='Estudiante', apellido='Perez',
                             email='lp@mail.com', sueldo=1000)
    print(objEmpleado)
    empleado2 = Empleado()
    print(empleado2)
    empleado3 = Empleado()
    print(empleado3)