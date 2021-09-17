import time

Posi=0
Num=[]
Par=[]

def Cab():
    print('-----------------')
    time.sleep(0.3)

print('Bem vindo:')
for C in range(1,11):
    Cab()
    Num.append(int(input(f'digite um numero para a {C}° posicao:\n')))

print('Os numeros PARES sao:')
for X in Num:
    Posi+=1
    Cab()
    if X % 2 == 0:
        print(f'[{X}]\nA posicao é {Posi}')

Cab()
print('Fim do programa!!')


#\\\\\\\\\\\\\\    