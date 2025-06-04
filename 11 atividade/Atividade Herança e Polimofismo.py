class Conta: #Define a classe base Conta
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite #Os atributos são privados, dá para identificar através do uso do underscore _

    @property
    def numero(self): #Retorna o número da conta
        return self._numero

    @property
    def titular(self): #Retorna o nome do titular
        return self._titular

    @property
    def saldo(self): #Retorna o saldo
        return self._saldo

    @property
    def limite(self): #Retorna o limite da conta
        return self._limite

    def deposita(self, valor): #Adiciona um valor ao saldo da conta
        self._saldo += valor

    def saca(self, valor): #Tenta realizar um saque
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

    def extrato(self): #Imprime o número e o saldo da conta
        print(f"Numero: {self.numero}\nSaldo: {self.saldo:.2f}")

    def transfere_para(self, destino, valor): #Tenta sacar da conta atual
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor) #Se der certo, deposita na conta destino.
            return True

    def atualiza(self, taxa): #Atualiza do dado da conta
        self._saldo += self._saldo * taxa
        return self._saldo

    def __str__(self):
        return f"Dados da Conta:\nNumero: {self._numero}\nTitular: {self._titular}\nSaldo: {self._saldo:.2f}\nLimite: {self._limite:.2f}"


class ContaCorrente(Conta): #A classe conta corrente herda os métodos e atributos de conta
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10  # Desconta 10 centavos do depósito


class ContaPoupanca(Conta): #Define a classe Conta Paupança
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


class AtualizadorDeContas: #Aplica a taxa de atualização em várias contas
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

    # Atualizando as contas com taxa de 1% 
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
