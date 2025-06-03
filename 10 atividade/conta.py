class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

    def extrato(self):
        print(f"Numero: {self.numero}\nSaldo: {self.saldo:.2f}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            return True

if __name__ == '__main__':
    from conta import Conta  #Pode remover se estiver no mesmo arquivo

    #Criação de duas contas
    conta1 = Conta('123-4', 'João Pedro Pascuti', 120.0, 1000.0)
    conta2 = Conta('567-8', 'Maria Flor Santos', 500.0, 1500.0)

    print(conta1.numero)
    print(conta1.titular)

    conta1.deposita(50.0)
    conta1.extrato()

    conta1.saca(30.0)
    conta1.extrato()

    #Transfere da conta1 para conta2
    sucesso = conta1.transfere_para(conta2, 100.0)

    if sucesso:
        print("Transferência realizada com sucesso!")
    else:
        print("Transferência não realizada!")

    #Extratos finais
    conta1.extrato()
    conta2.extrato()

    #Teste simples
    conta = Conta('123-4', 'joão', 1200.0, 1000.0)
    print(conta.titular)