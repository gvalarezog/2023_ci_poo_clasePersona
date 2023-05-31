from Herencia.cliente import Cliente
from Herencia.empleado import Empleado
from Herencia.persona import Persona

# persona1 = Persona()
cliente1 = Cliente()
empleado1 =  Empleado()
empleado2 =  Empleado()
# print(persona1)
print(cliente1)
print(empleado1)
print(empleado2)
print(Empleado.contador_empleado)

# empleado1.id = 2000
empleado1._id = 2000
print(empleado1)