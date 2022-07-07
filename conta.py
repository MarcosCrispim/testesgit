class Conta:

    def __init__(self, numero, titular, saldo, limite):
        """quando usamos o __ deixamos o atributo do abj "privado"""""
        print("construindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else
            print("o valor {} passou o limite".format(valor))

    def depositar(self, valor):
        self.__saldo += valor
        return print("Seu novo saldo é de {}".format(self.__saldo))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        return print("Seu novo saldo é de {} sr{}".format(self.__saldo, self.__titular))
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titulo(self):
        return self.__titular

    @property
    def limite(self):
        """usasse o get para retornar um valor qualquer, ao inves de usar pega_limite ou mostra_limita usasse o get"""
        return self.__limite
    @limite.setter
    def limite(self, limite):
        """Se usa o set para alterar um valor qualquer, ao inves de usar altera_limite ou up_limita usasse o get"""
        self.__limite = limite
