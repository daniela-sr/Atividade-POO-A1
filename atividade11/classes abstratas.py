import abc


class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._tipo = 'Conta'  # Atributo opcional de tipo

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

    @property
    def tipo(self):
        return self._tipo

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

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def __str__(self):
        return (f"Tipo: {self._tipo}\n"
                f"Numero: {self._numero}\n"
                f"Titular: {self._titular}\n"
                f"Saldo: {self._saldo:.2f}\n"
                f"Limite: {self._limite:.2f}")


# ---------- Conta Corrente ----------
class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self._tipo = 'Conta Corrente'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10


# ---------- Conta Poupança ----------
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self._tipo = 'Conta Poupança'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


# ---------- Conta Investimento ----------
class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self._tipo = 'Conta Investimento'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        return self._saldo


# ---------- Testes ----------
if __name__ == '__main__':
    # Tentando instanciar uma Conta diretamente (gera erro)
    try:
        c = Conta('000-0', 'Teste', 1000.0)
    except TypeError as e:
        print(f"Erro ao criar Conta diretamente: {e}")

    print("\n--- Testando ContaCorrente e ContaPoupanca ---")
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)

    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(cc)
    print(cp)

    print("\n--- Testando ContaInvestimento ---")
    ci = ContaInvestimento('123-6', 'Maria', 1000.0)
    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print(ci)