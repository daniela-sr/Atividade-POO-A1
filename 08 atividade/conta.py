#Exercicio 2: Primeira classe em python
class Conta:

    def __init__(self, numero, titular, saldo, limite): # Inicializa uma nova conta.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor): #Deposita um valor no saldo da conta.
        self.saldo += valor

    def saca(self, valor): #Realiza um saque na conta se houver saldo suficiente.
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):#Imprime o número da conta e o saldo atual.
        print(f"Numero: {self.numero}\nSaldo: {self.saldo:.2f}")

    def transfere_para(self, destino, valor):#Realiza uma transferência para outra conta.
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            return True