


class CuentaCorriente():
    noCuenta=""
    titular=""
    saldo=0

    def __init__(self, noCuenta, titular, saldo):
        self.noCuenta=noCuenta
        self.titular=titular
        self.saldo=saldo

    def getInfoCuenta(self):
        return "No. Cuenta: " + self.noCuenta + " Titular: " + self.titular + " Saldo: " + str(self.saldo)

    def inputCuenta(self, dinero):

        self.saldo = self.saldo + dinero

    def outputCuenta(self, gasto):

        self.saldo = self.saldo - gasto

class CuentaJoven(CuentaCorriente):
    bonus_promocion=0

    def __init__(self, noCuenta, titular, saldo, bonus_promocion):
        super().__init__(noCuenta, titular, saldo)
        self.bonus_promocion=bonus_promocion
        self.saldo = self.saldo + self.bonus_promocion
    
    def getBonus(self):

        return "El bonus es por la cantidad de: " + str(self.bonus_promocion)

    # def ingresar(self):
    #     super().inputCuenta

    # def retirar(self):
    #     super().outputCuenta

    def getDatos(self):

        return super().getInfoCuenta() + " Bonus: " + str(self.bonus_promocion)   


Cuenta1 = CuentaCorriente("556087", "Cesar Larios", 55)

Cuenta1.inputCuenta(5)

Cuenta1.outputCuenta(10)

cj=CuentaJoven("12545", "cesar joven", 500, 0)

cj.inputCuenta(200)

cj.outputCuenta(300)

print(cj.getDatos())
