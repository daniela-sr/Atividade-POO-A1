class Conta:

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', 'identificador']
    _id = 1

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self.identificador = Conta._id
        Conta._id += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite
    
    @property
    def identificador(self):
        return self._identificador

    @limite.setter
    def limite(self, limite):
        if limite < 0:
            print("Limite não pode ser negativo")
        else:
            self._limite = limite

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            return True
        else:
            return False

    def extrato(self):
        print(f"Número: {self._numero}")
        print(f"Titular: {self._titular}")
        print(f"Saldo: {self._saldo}")

conta = Conta('123-4', 'João', 500.0, 1000.0)

print(conta._numero)  # ⚠️ Funciona, mas não é recomendado
conta._numero = '999-9'  # ⚠️ Funciona, mas quebra o encapsulamento
print(conta._numero)

print(conta.saldo)       # ✅ Acesso controlado
conta.saldo = 600        # ✅ Modifica se válido
conta.saldo = -50        # ❌ Não permite saldo negativo

Conta('123-4', 'João', 500.0, 1000.0).__dict__

c1 = Conta('123-4', 'João', 100.0)
c2 = Conta('567-8', 'Maria', 200.0)
c3 = Conta('999-9', 'José', 300.0)

print(c1.identificador)  # 1
print(c2.identificador)  # 2
print(c3.identificador)  # 3