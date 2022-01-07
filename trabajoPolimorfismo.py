from types import MappingProxyType


class Persona():

    def hablar(self):
        return "hablo como una persona"

class Trabajador(Persona):

    def hablar(self):
        return "hablo con un trabajador"

class Director(Trabajador):

    def hablar(self):
        return "hablo como un director"

def hazlesHablar(objeto):

    print(objeto.hablar())





    # for persona in listaDePersonas:

    #     print(persona.hablar())

Antonio=Persona()
Maria=Trabajador()
Ana=Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("-----------------------------------------------")


hazlesHablar(Maria)