#programa para calcular o salario liquido de um funcionario

#Funcoes e importacoes
import time

def Cab():
    print('-----------------------')
    time.sleep(0.3)

def SalarioBruto(HT,GH):
    S=HT*GH
    return S

def Leao(S):
    L=S*11/100
    return L

def INSS(S):
    I=S*8/100
    return I

def sindicato(S):
    Sind=S*5/100
    return Sind

#inicio do programa:
Cab()
print('--[Bem vindo]--')
Cab()
HorasTrabalhadas=int(input('Digite a quantia de horas trabalhadas: '))
GanhoHoras=float(input('Digite a quantia que ganha por hora: R$'))
#Calculo do salario
SB=(SalarioBruto(HorasTrabalhadas, GanhoHoras))
Imp=(Leao(SalarioBruto(HorasTrabalhadas, GanhoHoras)))
Inss=(INSS(SalarioBruto(HorasTrabalhadas, GanhoHoras)))
Sindi=(sindicato(SalarioBruto(HorasTrabalhadas, GanhoHoras)))
Sl=SB-(Imp+Inss+Sindi)

#Resultado:
Cab()
print('')
print(f'Salario Bruto: R${SB}')
print('')
print('DESCONTOS')
print(f'- Imposto de renda: R${Imp}')
print(f'- INSS: R${Inss}')
print(f'- Sindicato: R${Sindi}')
print('')
print(f'Salario Final:')
print(f'Salario Liquido: R${Sl}')


#\\\\\\\\\\\\\\