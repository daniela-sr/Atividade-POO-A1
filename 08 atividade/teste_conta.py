#Execicio 1: Criando uma conta
#Nesse exercicio foi criado uma conta junto com suas caracteristicas e funcionalidades em um mesmo arquivo.

def cria_conta(numero, titular, saldo, limite):
  conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite} #Variável do tipo dicionário
  return conta

def deposita(conta, valor):#A função adiciona o valor ao saldo da conta
  conta['saldo'] += valor #Otimização no código para não precisar escrever conta['saldo'] novamente

def saca(conta, valor):
  conta['saldo'] -= valor #A função subtrai o valor do saldo da conta

def extrato(conta): #A função imprime o número e o saldo
  print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

conta = cria_conta(123, "João Pedro Pascuti", 120.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)