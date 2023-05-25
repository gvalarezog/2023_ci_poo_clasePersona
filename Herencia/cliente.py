from persona import Persona

class Cliente(Persona):
    def __init__(self, cedula:str=None, email:str=None, nombre:str=None, apellido:str=None, genero:str=None
                 , ocupacion:str=None, id:int=None, fechaRegistro:str=None, vip:bool=False):
        # self._nombre = nombre
        # self._apellido = apellido
        # self._cedula = cedula
        # self._email = email
        # self._genero = genero
        # self._ocupacion = ocupacion
        super().__init__(cedula=cedula, email=email, nombre=nombre, apellido=apellido, genero=genero
                         , ocupacion=ocupacion)
        self._id = id
        self._fechaRegistro = fechaRegistro
        self._vip = vip


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self_id = id

    @property
    def fechaRegistro(self):
        return self._fechaRegistro

    @fechaRegistro.setter
    def fechaRegistro(self, fechaRegistro):
        self._fechaRegistro = fechaRegistro

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, vip):
        self._vip=vip

    '''
    Redefinición del metodo STR
    '''
    def __str__(self):
        # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
        return f'Cliente: {self.__dict__.__str__()}'


if __name__ == '__main__':
    objCliente = Cliente(nombre='Luis', genero='Masculino', ocupacion='Estudiante', apellido='Perez'
                             , email='lp@mail.com', id=1, fechaRegistro='24/05/2023', vip=True)
    print(objCliente)
    objCliente.cedula='piedras'
    print(objCliente)