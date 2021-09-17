ListaNum = []
Cont=0
Soma=0

for C in range(1, 6):
    ListaNum.append(int(input(f'Digite um numero para a posição {C}°:\n')))

for n in ListaNum:
    Soma+=n
    Cont+=1

print(f'A soma dos números digitados é {Soma}.\nE a media é {Soma/Cont}')


#\\\\\\\\\\\\\\