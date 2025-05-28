from conta import Conta  #Importa a classe Conta do arquivo conta.py

#Criação de duas contas
conta1 = Conta('123-4', 'João Pedro Pascuti', 120.0, 1000.0)
conta2 = Conta('567-8', 'Maria Flor Santos', 500.0, 1500.0)

#Verifica o tipo do objeto
print(type(conta1))

print(conta1.numero)    
print(conta1.titular)   

conta1.deposita(50.0)   
conta1.extrato()        

conta1.saca(20.0)       
conta1.extrato()        

#Transfere da conta1 para conta2
sucesso = conta1.transfere_para(conta2, 100.0)  

#Verifica se a transferência foi realizada
if sucesso:
    print("Transferência realizada com sucesso!")
else:
    print("Transferência não realizada!")

#Verificar os extratos após a transferência
conta1.extrato()  
conta2.extrato()  