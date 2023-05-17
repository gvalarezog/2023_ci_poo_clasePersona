'''
Clase Persona permite crear objetos de tipo persona
'''


class Persona:
    '''
    Constructor o metodo que inicializa una objeto
    '''
    def __init__(self, cedula=None, email=None, nombre=None, apellido=None, genero=None, ocupacion=None ):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email
        self._genero = genero
        self._ocupacion = ocupacion


    '''
    Redefinición del metodo STR
    '''
    def __str__(self):
        # return f'Persona [nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'
        return f'Persona: {self.__dict__.__str__()}'



if __name__ == '__main__':
    objetoPersona1 = Persona(nombre='Luis', genero='Masculino', ocupacion='Estudiante', apellido='Perez', email='lp@mail.com')
    # print(f'Nombre: {objetoPersona1._nombre}')
    # print(f'Apellido: {objetoPersona1._apellido}')
    # print(f'Genero: {objetoPersona1._genero}')
    # print(f'Ocupación: {objetoPersona1._ocupacion}')
    # print(f'Email: {objetoPersona1._email}')
    print(objetoPersona1.__str__())
    # print('*'.center(__width=50,__fillchar='*'))
    objetoPersona2 = Persona(genero='Femenino', ocupacion='Doctor', nombre='Maria', apellido='Paz', email='mp@mail.com')
    # print(f'Nombre: {objetoPersona2._nombre}')
    # print(f'Apellido: {objetoPersona2._apellido}')
    # print(f'Genero: {objetoPersona2._genero}')
    # print(f'Ocupación: {objetoPersona2._ocupacion}')
    # print(f'Email: {objetoPersona2._email}')
    print(objetoPersona2)

    objPersona3 =  Persona()
    # print(f'Nombre: {objPersona3._nombre}')
    # print(f'Apellido: {objPersona3._apellido}')
    # print(f'Genero: {objPersona3._genero}')
    # print(f'Ocupación: {objPersona3._ocupacion}')
    # print(f'Email: {objPersona3._email}')
    print(objPersona3)
