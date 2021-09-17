class Conta_Corrente:
    def __init__(self, Numero_Conta, Nome_Correntista, Salda_Conta):
        self.Numero_Conta = Numero_Conta
        self.Nome_Correntista = Nome_Correntista
        self.Saldo_Conta = Salda_Conta

    def Saque(self):
        print(f'Nome:{self.Nome_Correntista}\nNúmero da conta {self.Numero_Conta}')
        print(f'Valor disponível para Saque: R${self.Saldo_Conta:2.2f}')
        Retirar = float(input('Quanto deseja retirar: R$'))
        while Retirar >= self.Saldo_Conta:
            print('Valor indisponível')
            Retirar = float(input('Quanto deseja retirar: R$'))
        self.Saldo_Conta -= Retirar
        print(f'Valor Atual: R${self.Saldo_Conta}') 
    
    def Depositar(self):
        print(f'Nome:{self.Nome_Correntista}\nNúmero da conta {self.Numero_Conta}')
        print(f'Valor Atual: R${self.Saldo_Conta:2.2f}')
        Por = float(input('Valor de deposito: R$'))
        self.Saldo_Conta += Por
        print('Valor Atual: R$', self.Saldo_Conta)

    def TrocaNome(self):
        NewName = str(input('Digite o novo nome de usuário: '))
        self.Nome_Correntista = NewName

CC1 = Conta_Corrente(123, 'Octavio Gonçalves', 2500.99)
CC2 = Conta_Corrente(456, 'Mirai', 2500.99)


Num_Usu = int(input('Digite o numero de sua conta: '))
print('Bem Vindo {}:')
Acao = int(input('Deseja:\nVer Saldo = 1\nSacar = 2\nDepositar = 3\nTrocar de Nome = 4'))

if Acao == 1:


CC1.Saque()
CC1.TrocaNome()
CC1.Depositar()


###########################################
#Terminar Terminal de banco Inicio 12/08/21
#\\\\\\\\\\\\\\