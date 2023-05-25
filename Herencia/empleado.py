from persona import Persona



class Empleado(Persona):
    def __init__(self, id:int=None, sueldo:float=0.0, cedula:str='', email:str=None, nombre:str=None, apellido:str=None
                 , genero:str=None, ocupacion:str=None):
        super().__init__(cedula=cedula, email=email, nombre=nombre, apellido=apellido, genero=genero
                         , ocupacion=ocupacion)
        self._id = id
        self._sueldo = sueldo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
                             email='lp@mail.com', id=1, sueldo=1000)
    print(objEmpleado.__str__())
    objEmpleado.cedula = '1234567890'
    objEmpleado.ocupacion = 'Licenciado'
    print(objEmpleado)