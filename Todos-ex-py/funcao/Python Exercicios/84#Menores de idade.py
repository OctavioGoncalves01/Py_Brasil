#Separando Menores de idade

import time

def Cab():
    print('-------------------')
    time.sleep(0.3)

Nome=[]
Idade=[]
Cont=0
LPosi=[]

print('Bem vindo')
for x in range(0,3):
    Cab()
    Nome.append(input(f'Digite o nome para a posição {x}: '))
    Idade.append(int(input(f'Digite a idade para a posição {x}: ')))

for I in Idade:
    if I < 18:
        LPosi.append(Cont)
    Cont+=1

for X in LPosi:
    Cab()
    print('Nome:', Nome[X], '\nIdade: ', Idade[X], 'ano(s).')
    

#\\\\\\\\\\\\\\