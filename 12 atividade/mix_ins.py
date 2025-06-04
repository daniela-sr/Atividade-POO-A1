class TributavelMixIn: #Define uma classe Mix In
    def get_valor_imposto(self):
        raise NotImplementedError("Subclasses devem implementar get_valor_imposto") #Indica que o método é obrigatório


class Conta: #Conta Comum
    def __init__(self, numero, titular, saldo=0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    def deposita(self, valor): #Adiciona um valor ao saldo e precisa ser positivo
        if valor < 0:
            raise ValueError("Valor do depósito deve ser positivo.")
        self._saldo += valor

    def saca(self, valor): #Subtrai o valor do saldo e tem 2 validações
        if valor < 0:
            raise ValueError("Valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise RuntimeError("Saldo insuficiente.")
        self._saldo -= valor

    def get_saldo(self): #Retorna o saldo atual
        return self._saldo

    def __repr__(self): #Define como a conta será exibida
        return f"Conta({self._titular}, {self._numero}, saldo={self._saldo})"


class ContaCorrente(Conta, TributavelMixIn): #Cria a classe conta corrente e herda de Conta e TributavelMixIn
    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaInvestimento(Conta, TributavelMixIn): #Cria a classe conta investimento e herda de Conta e TributavelMixIn
    def get_valor_imposto(self):
        return self._saldo * 0.03


class ContaPoupanca(Conta): #Cria a classe conta poupança e herda de conta 
    pass  # Não é tributável


class SeguroDeVida(TributavelMixIn): #Armazena o valor do seguro
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self): #Implementa o valor do seguro
        return 50 + self._valor * 0.05

    def __repr__(self):
        return f"SeguroDeVida({self._titular}, {self._numero_apolice})"


class ManipuladorDeTributaveis: #Classe responsável por calcular o imposto total
    def calcula_impostos(self, objetos):
        total = 0
        for obj in objetos:
            if isinstance(obj, TributavelMixIn):
                total += obj.get_valor_imposto()
            else:
                print(f"{obj} não é tributável.")
        return total


if __name__ == "__main__": #Cria uma conta corrente, investimento e pouoança
    cc = ContaCorrente("123-4", "João", 1000.0)
    ci = ContaInvestimento("456-7", "Ana", 2000.0)
    cp = ContaPoupanca("789-0", "Maria", 1500.0)  # não é tributável

    seguro1 = SeguroDeVida(100.0, "José", "345-77") #Cria dois seguros de vida
    seguro2 = SeguroDeVida(300.0, "Carlos", "555-11")

    lista = [cc, ci, cp, seguro1, seguro2]

    manipulador = ManipuladorDeTributaveis() #Cria um manipulador e calcula o total de impostos 
    total = manipulador.calcula_impostos(lista)

    print(f"\nTotal de impostos: R${total:.2f}") #Exibe o resultado com duas casas decimais
