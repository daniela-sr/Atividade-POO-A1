import abc


# ---------------- Exceção personalizada ----------------
class SaldoInsuficienteError(RuntimeError):
    """Exceção lançada quando não há saldo suficiente para saque."""
    pass


# ---------------- Interface Tributável ----------------
class Tributavel(abc.ABC):
    """Interface para objetos que são tributáveis."""

    @abc.abstractmethod
    def get_valor_imposto(self):
        """Deve retornar o valor do imposto do objeto."""
        pass


# ---------------- Classe Conta ----------------
class Conta(abc.ABC):
    def __init__(self, titular, numero, saldo=0.0, limite=1000.0):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo.')
        self._saldo += valor

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor:
            raise SaldoInsuficienteError('Saldo insuficiente.')
        self._saldo -= valor

    def extrato(self):
        print(f"Titular: {self._titular}\nNúmero: {self._numero}\nSaldo: {self._saldo:.2f}")

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass


# ---------------- ContaCorrente ----------------
class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor + 0.10:
            raise SaldoInsuficienteError('Saldo insuficiente.')
        self._saldo -= (valor + 0.10)

    def get_valor_imposto(self):
        return self._saldo * 0.01


# ---------------- ContaPoupanca ----------------
class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo.')
        self._saldo += valor


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


# ---------------- Manipulador de Tributáveis ----------------
class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.get_valor_imposto()
            else:
                print(f"{t} não é um tributável")
        return total


# ---------------- Registro das classes como Tributáveis ----------------
Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)
Tributavel.register(ContaInvestimento)


# ---------------- Programa Principal ----------------
if __name__ == '__main__':
    print('--- Testando saques e depósitos com exceções ---')

    cc = ContaCorrente('João', '123-4', 1000.0)

    # Teste saque com valor negativo
    valor = -1000.0
    try:
        cc.saca(valor)
        print(f'Saque de {valor} realizado com sucesso.')
    except ValueError:
        print('O valor a ser sacado deve ser um número positivo.')
    except SaldoInsuficienteError:
        print('Você não possui saldo suficiente para concluir esta operação.')

    print('---')

    # Teste saque com saldo insuficiente
    valor = 5000.0
    try:
        cc.saca(valor)
        print(f'Saque de {valor} realizado com sucesso.')
    except ValueError:
        print('O valor a ser sacado deve ser um número positivo.')
    except SaldoInsuficienteError:
        print('Você não possui saldo suficiente para concluir esta operação.')

    print('---')

    # Teste depósito com valor negativo
    valor = -500.0
    try:
        cc.deposita(valor)
        print(f'Depósito de {valor} realizado com sucesso.')
    except ValueError:
        print('O valor a ser depositado deve ser um número positivo.')

    print('--- Testando impostos ---')

    cc.deposita(1000.0)  # Para garantir saldo positivo
    seguro = SeguroDeVida(100.0, 'José', '345-77')
    ci = ContaInvestimento('Ana', '123-0')
    ci.deposita(100.0)

    cp = ContaPoupanca('Maria', '123-6')

    lista_tributaveis = [cc, seguro, ci, cp]

    mt = ManipuladorDeTributaveis()
    total_impostos = mt.calcula_impostos(lista_tributaveis)
    print(f"Total de impostos calculados: {total_impostos:.2f}")