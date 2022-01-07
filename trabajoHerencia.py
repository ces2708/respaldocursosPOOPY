class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    
    def getDatosPeronales(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)


    def habla(self):

        return "Estoy hablando"

    def piensa(self):

        return "Estoy pensando"
    
    def camina(self):

        return "Estoy caminando"

    def come(self):

        return "Estoy comiendo"

class Estudiante(Persona):   #en python se hereda poniendo entre el parentesis a la superclase

    def __init__(self, nombre, apellido, edad, escuela):
        Persona.__init__(self, nombre, apellido, edad)

        self.escuela=escuela

    def getDatosPeronales(self):
        return super().getDatosPeronales() + " escuela: " + self.escuela

    def estudia(self):

        return "Estoy estudiando"

    
class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):
        Persona.__init__(self, nombre, apellido, edad)

        self.empresa=empresa

    def getDatosPeronales(self):
        return super().getDatosPeronales() + " empresa: " + self.empresa

    def tabaja(self):

        return "Estoy trabajando"


class Director(Trabajador, Estudiante):    #herencia multiple el orden en el que indicas implica preferencia

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)

        self.bonus=bonus

    def getDatosPeronales(self):
        return super().getDatosPeronales() + " Bonus: " + str(self.bonus)

    def dirige(self):

        return "Estoy dirigiendo"



persona1=Persona("ana", "gomez", 35)

estudiante1=Estudiante("Juan", "Diaz", 21, "San Javier")

# print(persona1.getDatosPeronales())
# print(estudiante1.getDatosPeronales())

trabajador1=Trabajador("antonio", "lopez", 55, "C Cope")
print(trabajador1.getDatosPeronales())

director1=Director("juan M", "Rubio", 21, "Pildoras Informaticas", "san javier", 1500)

print(director1.getDatosPeronales())