ListaSalario = []
Contador = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def SalarioSemanal(X):
    Salario = 200 + (X*9/100)
    return Salario

while True:
    Comissao = float(input('Digite a Comissão: R$'))
    ListaSalario.append(SalarioSemanal(Comissao))
    
    Pergunta = str(input('Deseja continuar [S/N]:')).upper()
    if Pergunta == 'N':
        break

for S in ListaSalario:
    if (S > 200) and (S < 299):
        C = Contador[0]
        C1 = C+1
        Contador.insert(C1)


print(ListaSalario)
print(Contador)


#Não sei como proceder 04/08/2021