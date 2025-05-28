from conta import Conta

# Criação de contas
conta1 = Conta('123-4', 'João', 120.0, 1000.0)
conta2 = Conta('567-8', 'Maria', 500.0, 1500.0)

# Teste de métodos
print("Extrato da conta1:")
conta1.extrato()

print("\nDepositando 50.0 na conta1:")
conta1.deposita(50.0)
conta1.extrato()

print("\nSacando 20.0 da conta1:")
conta1.saca(20.0)
conta1.extrato()

print("\nTransferindo 100.0 da conta1 para conta2:")
conta1.transfere_para(conta2, 100.0)
print("Extrato da conta1 após transferência:")
conta1.extrato()
print("Extrato da conta2 após receber transferência:")
conta2.extrato()

# Testando tentativa de saque maior que saldo
print("\nTentando sacar 1000.0 da conta1:")
resultado = conta1.saca(1000.0)
print("Saque realizado?" , resultado)
conta1.extrato()
