from collections.abc import MutableSequence

class SaldoInsuficienteError(RuntimeError):
    pass
#Define uma exceção personalizada

class Conta: #Conta comum
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self): #Retorna o saldo
        return self._saldo

    def deposita(self, valor): #Adiciona o valor ao saldo, desde que seja positivo
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo.')
        self._saldo += valor

    def saca(self, valor):#Retira valor do saldo, se houver saldo suficiente; lança exceção se não houver
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor:
            raise SaldoInsuficienteError('Saldo insuficiente.')
        self._saldo -= valor

    def extrato(self): #imprime informações da conta
        print(f"Titular: {self._titular} | Número: {self._numero} | Saldo: {self._saldo:.2f}")

    def atualiza(self, taxa): #Atualiza saldo com base numa taxa
        self._saldo += self._saldo * taxa


class ContaCorrente(Conta): #Herdeira da classe conta, com algumas modificações
    def atualiza(self, taxa): #Aplica a taxa em dobro no saldo
        self._saldo += self._saldo * taxa * 2

    def saca(self, valor): #Desconta R$ 0,10 adicional por operação de saque
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor + 0.10:
            raise SaldoInsuficienteError('Saldo insuficiente.')
        self._saldo -= (valor + 0.10)

    def get_valor_imposto(self): #Retorna 1% do saldo, simulando um imposto
        return self._saldo * 0.01


class Contas(MutableSequence): #Representa uma coleção personalizada de contas bancárias. Herda valores de "MutableSequence"
    def __init__(self):
        self._dados = []

    def __len__(self): #Retorna o número de contas
        return len(self._dados)

    def __getitem__(self, posicao): #Retorna a conta na primeira posição
        return self._dados[posicao]

    def __setitem__(self, posicao, valor): #Substitui uma conta, validando se é do tipo Conta
        if isinstance(valor, Conta):
            self._dados[posicao] = valor
        else:
            raise TypeError("Valor atribuído não é uma Conta.")

    def __delitem__(self, posicao): #Remove uma conta
        del self._dados[posicao]

    def insert(self, posicao, valor): #Insere uma nova conta em uma posição, validando o tipo
        if isinstance(valor, Conta):
            self._dados.insert(posicao, valor)
        else:
            raise TypeError("Valor inserido não é uma Conta.")

if __name__ == '__main__':
    contas = Contas() #Cria uma instância de Contas
    import csv

    try:
        with open('contas.txt', 'r', encoding='utf-8') as arquivo: #Tenta abrir o arquivo "contas.txt" com dados de contas no formato CSV.
            leitor = csv.reader(arquivo)

            for linha in leitor:
                conta = ContaCorrente(linha[0], linha[1], float(linha[2]), float(linha[3]))
                contas.append(conta) 

    except FileNotFoundError:
        print(" Arquivo contas.txt não encontrado.") 
        exit() 
    except Exception as e:
        print(f" Ocorreu um erro: {e}")
        exit()

    print('Saldo - Imposto')

    for c in contas:
        print(f'{c.saldo} - {c.get_valor_imposto()}') #Exibe o saldo e o valor na tela
