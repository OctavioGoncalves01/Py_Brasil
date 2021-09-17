QuantidadePaes = int(input('Digite a quantidade de paes: '))

for C in range(1, 51):
    Pagar =QuantidadePaes * 0.18
    
    if Pagar == C*0.18:
        print(f'[Pães {C}  :   R${C*0.18:2.2f}]')
        break
    else:
        print(f'Pães {C}  :   R${C*0.18:2.2f}')


#\\\\\\\\\\\\\\