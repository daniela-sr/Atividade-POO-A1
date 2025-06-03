from tributavel import Tributavel
import abc


# ---------------- Classe Conta ----------------
class Conta(abc.ABC):
    def __init__(self, titular, numero, saldo=0, limite=1000.0):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def extrato(self):
        print(f"Titular: {self._titular}\nNúmero: {self._numero}\nSaldo: {self._saldo:.2f}")

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass


# ---------------- ContaCorrente ----------------
class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def get_valor_imposto(self):
        return self._saldo * 0.01


# ---------------- ContaPoupanca ----------------
class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


# ---------------- ContaInvestimento ----------------
class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def get_valor_imposto(self):
        return self._saldo * 0.03


# ---------------- SeguroDeVida ----------------
class SeguroDeVida:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

    def __repr__(self):
        return f"SeguroDeVida({self._titular}, {self._numero_apolice})"