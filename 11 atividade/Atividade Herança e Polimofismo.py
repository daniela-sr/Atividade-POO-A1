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

    def atualiza(self, taxa):
        """Atualiza a conta com a taxa fornecida"""
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        return f"Dados da Conta:\nNumero: {self._numero}\nTitular: {self._titular}\nSaldo: {self._saldo:.2f}\nLimite: {self._limite:.2f}"


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10  # Desconta 10 centavos do depósito


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        print(f"\nSaldo Inicial da Conta {conta.numero}: {conta.saldo:.2f}")
        saldo_atualizado = conta.atualiza(self._selic)
        print(f"Saldo Atualizado da Conta {conta.numero}: {saldo_atualizado:.2f}")
        self._saldo_total += saldo_atualizado

if __name__ == '__main__':
    # Criando contas
    c = Conta('123-4', 'Joao', 1000.0, 1000.0)
    cc = ContaCorrente('123-5', 'Jose', 1000.0, 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0, 1000.0)

    # Atualizando as contas com taxa de 1% (0.01)
    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print("\nSaldos após atualização individual:")
    print(c.saldo)    # Saldo atualizado com 1%
    print(cc.saldo)   # Saldo atualizado com 2%
    print(cp.saldo)   # Saldo atualizado com 3%

    # Testando __str__()
    print("\n Impressão")
    print(cc)

    # Testando AtualizadorDeContas
    print("\n Atualizador de Contas")
    atualizador = AtualizadorDeContas(0.01)

    atualizador.roda(c)
    atualizador.roda(cc)
    atualizador.roda(cp)

    print(f"\nSaldo Total nas Contas após atualização: {atualizador.saldo_total:.2f}")