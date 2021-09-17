Nome=[]
Salario=[]
Sexo=[]
Cont=0
Smaior5=[]

for F in range(0,5):
    Nome.append(input(f'Digite o nome para a posicao {F}: '))
    Sexo.append(input('Sexo: M/F:  '))
    Salario.append(float(input('Digite o salario: R$')))

for C in Salario:
    if C >= 5000:
        Smaior5.append(Cont)
    Cont+=1

for N in Smaior5:
    print(f'Nome: {Nome[N]}, Salario {Salario[N]}')


#\\\\\\\\\\\\\\