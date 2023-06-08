from Herencia.cajero import Cajero
from Herencia.cliente import Cliente
from Herencia.empleado import Empleado

def enviar_correo(persona, asunto):
    if isinstance(persona, Empleado):
        print('Enviado correo a empleado')
    elif isinstance(persona, Cliente):
        print('Enviado correo a cliente')
    elif isinstance(persona, Cajero):
        print('Enviado correo a cajero')
    print(f'A: {persona.email}\n'
          f'Asunto: {asunto}\n'
          f'Cuerpo: {persona}')

#lista de personas que pueden ser clientes o empleados
e1 = Empleado(nombre='Luis', email='lp@mail.com')
c1 = Cliente(nombre='Maria', email='mpaz@mail.com')
e2 = Empleado(nombre='Jose', email='jl@mail.com')
c2 = Cliente(nombre='Alejandra', email='ag@mail.com')
cajero = Cajero(email='caja@mail.com')

personas = list()
personas.append(e1)
personas.append(c1)
personas.append(e2)
personas.append(c2)
personas.append(cajero)

# print(personas)

# for persona in personas:
#     print(persona)

for persona in personas:
    enviar_correo(asunto='Asunto', persona=persona)
    print('*'.center(50,'*'))

