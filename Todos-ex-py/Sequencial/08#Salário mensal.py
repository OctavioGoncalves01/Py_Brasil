def Salario(HT, GH):
    S=HT*GH
    return S

Horas=int(input('Digie a quantia de horas trabalhadas: '))
GanhoPHoras=float(input('Digite a quantia que é ganho por hora: R$'))

print(f'O salário desse mês é: R${Salario(Horas, GanhoPHoras):4.2f}.')


#\\\\\\\\\\\\\\