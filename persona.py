'''
Clase Persona permite crear objetos de tipo persona
'''


class Persona:
    '''
    Constructor o metodo que inicializa una objeto
    '''
    def __init__(self, cedula:str='', email:str=None, nombre:str=None, apellido:str=None
                 , genero:str=None, ocupacion:str=None):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email
        self._genero = genero
        self._ocupacion = ocupacion


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_cambiado):
        self._nombre = nombre_cambiado

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        if len(cedula) == 10:
            self._cedula = cedula

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, ocupacion):
        self._ocupacion = ocupacion

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    '''
    Redefinición del metodo STR
    '''
    def __str__(self):
        # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
        return f'Persona: {self.__dict__.__str__()}'
    '''
    Display name
    '''
    def nombre_mostrar(self, mostrar_correo):
        if mostrar_correo:
            print(f'{self._nombre} {self._apellido}, emial: {self._email}')
        else:
            print(f'{self._nombre} {self._apellido}')

    def obtener_nombre_mostrar(self):
        return f'{self._nombre} {self._apellido}'



if __name__ == '__main__':
    objetoPersona1 = Persona(nombre='Luis', genero='Masculino', ocupacion='Estudiante', apellido='Perez',
                             email='lp@mail.com')
    print(objetoPersona1.__str__())


    objetoPersona1._nombre = 'Carlos' # no es correcto
    objetoPersona1._email = 'cp@mail.com' # no es correcto
    print(objetoPersona1._nombre) # no es correcto


    objetoPersona1.nombre = 'Felipe' # si es correcto
    print(objetoPersona1.nombre) # si es correcto
    print(objetoPersona1.apellido)
    objetoPersona1.email = 'fp@mail.com'
    print(objetoPersona1.email)


    print(objetoPersona1.__str__())
    print('*'.center(100,'*'))


    objP2 = Persona(cedula='0123456799')
    print(objP2)

    objP3 = Persona(cedula=123456799)
    print(objP3)
    objP3.cedula = '0123456789'
    print(objP3)

