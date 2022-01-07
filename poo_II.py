class Persona():
    __nombre =""    #en python se encapsula con "_" o "__" antes del nombre de la variable o el método, según el nivel de 
    #de encapsulamiento requerido a diferencia de otros lenguajes no hay modificadores de acceso, se hace por convenciones
    apellido=""
    __edad=0
    genero="sin definir"

    def __init__(self, nombre, apellido, genero):
        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero

    def setEdad(self, laEdad):
        if laEdad<0 or laEdad>100:
            print ("Error en la edad")
        else:
            self.__edad=laEdad
            return self.__edad

    def hablar(self):

        return "La persona que se llama " + self.__nombre + "está hablando"
    
    def camina(self):

        return "La persona que se llama " + self.__nombre + "está caminando"

    def getDatos(self):

        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad " + str(self.__edad) + " Género: " + self.genero



p1=Persona("juan", "diaz", "masculino")

p1.setEdad(7)



print(p1.getDatos())

p1.__nombre="alicia"

print(p1.getDatos())


#p2=Persona("ana", "martin", 35, "femenino")