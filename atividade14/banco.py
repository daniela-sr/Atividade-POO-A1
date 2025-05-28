from collections.abc import MutableSequence
import csv


# ---------------- EXCEÇÕES ----------------
class SaldoInsuficienteError(RuntimeError):
    pass


# ---------------- CLASSES DE CONTA ----------------
class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
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
        print(f"Titular: {self._titular} | Número: {self._numero} | Saldo: {self._saldo:.2f}")

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa


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


# ---------------- CLASSE CONTAS (MUTABLESEQUENCE) ----------------
class Contas(MutableSequence):
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if isinstance(valor, Conta):
            self._dados[posicao] = valor
        else:
            raise TypeError("Valor atribuído não é uma Conta.")

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if isinstance(valor, Conta):
            self._dados.insert(posicao, valor)
        else:
            raise TypeError("Valor inserido não é uma Conta.")


# ---------------- PROGRAMA PRINCIPAL ----------------
if __name__ == '__main__':
    contas = Contas()

    try:
        with open('contas.txt', 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                # linha[0] -> número da conta
                # linha[1] -> titular
                # linha[2] -> saldo
                # linha[3] -> limite
                conta = ContaCorrente(linha[0], linha[1], float(linha[2]), float(linha[3]))
                contas.append(conta)

    except FileNotFoundError:
        print("❌ Arquivo contas.txt não encontrado.")
        exit()
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
        exit()

    print('Saldo - Imposto')

    for c in contas:
        print(f'{c.saldo} - {c.get_valor_imposto()}')

    # (Opcional) Atualizando os saldos com uma taxa de 0.01
    print('\nSaldo atualizado:')
    for c in contas:
        c.atualiza(0.01)
        print(f'{c.saldo}')