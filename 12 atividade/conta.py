import abc

class TributavelMixIn:
    def get_valor_imposto(self):
        """Método que obriga as classes filhas a implementarem cálculo de imposto."""
        pass

class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._tipo = 'Conta'

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

class ContaCorrente(Conta, TributavelMixIn):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self._tipo = 'Conta Corrente'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self._tipo = 'Conta Poupança'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo

class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self._tipo = 'Conta Investimento'

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        return self._saldo

class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

    def __str__(self):
        return (f"Seguro de Vida:\n"
                f"Títular: {self._titular}\n"
                f"Valor: {self._valor:.2f}\n"
                f"Número Apólice: {self._numero_apolice}")