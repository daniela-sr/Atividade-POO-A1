class Conta:

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_id']

    # Atributo de classe para controle do identificador
    identificador = 1

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

        # Atribuindo identificador único
        self._id = Conta.identificador
        Conta.identificador += 1

    # Getter para id
    @property
    def id(self):
        return self._id

    # Getter e Setter para saldo
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    # Getter e Setter para limite
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        if limite < 0:
            print("Limite não pode ser negativo")
        else:
            self._limite = limite

    # Getter para numero
    @property
    def numero(self):
        return self._numero

    # Getter e Setter para titular
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    # Métodos operacionais
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if valor > (self._saldo + self._limite):
            print("Saldo insuficiente")
        elif valor <= 0:
            print("Valor de saque inválido")
        else:
            self._saldo -= valor

    def extrato(self):
        print(f"Conta: {self._numero} | Titular: {self._titular} | Saldo: {self._saldo} | ID: {self._id}")

conta1 = Conta(123, "Anna Clara Santos", 5000)
conta2 = Conta(456, "Bruno Medelho", 1000)
conta3 = Conta(789, "Carla Santoro", 3000)

print(conta1.id)  
print(conta2.id)  
print(conta3.id)  

# Verificando no extrato
conta1.extrato()  
conta2.extrato()  
conta3.extrato()  