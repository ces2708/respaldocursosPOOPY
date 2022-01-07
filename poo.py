class Coche():
    ruedas=4 #propiedades
    largoChasis=260
    anchoChasis=130
    arrancado=False

    

    def arrancar(self): #método
        self.arrancado=True

    def estado(self):
        if(self.arrancado):
            return "El coche está funcionando"
        else:
            return "El coche está parado"

mazda=Coche() #instancia de clase (objeto?)

renault=Coche()

print("tu coche tiene " + str(renault.ruedas) + " ruedas") #accediendo a las propeidades de un objeto

renault.arrancar()

print(mazda.estado())