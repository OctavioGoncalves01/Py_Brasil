import time

def Cab():
    print('-------------------------')
    time.sleep(0.35)

def Padrao(D, Buy, Pa, T, VP):
    print(f'Valor da Dívida:             R${D:2.2f}')
    print('')
    print(f'Valor dos Juros:             R${T:2.2f}')
    print('')
    print(f'Quantia de parcelas:         Qnt {Pa}')
    print('')
    print(f'Valor Total da divida:       R${Buy:2.2f}')
    print('')
    print(f'Valor por parcelas:          R${VP:2.2f}')

Cab()
Divida = float(input('Digite o valor da divida: R$'))
Parcelas = int(input('Digite a quantia de parcelas: '))

if Parcelas == 0:
    print(Divida)

elif Parcelas == 3:
    Pagar = (Divida*1.1)
    ValorPorParcela = Pagar/Parcelas
    Taxa = (Divida*10/100)

elif Parcelas == 6:
    Pagar = (Divida*1.15)
    ValorPorParcela = Pagar/Parcelas
    Taxa = (Divida*15/100)
    
elif Parcelas == 9:
    Pagar = (Divida*1.2)
    ValorPorParcela = Pagar/Parcelas
    Taxa = (Divida*20/100)

elif Parcelas == 12:
    Pagar = (Divida*1.25)
    ValorPorParcela = Pagar/Parcelas
    Taxa = (Divida*25/100)

else:
    print('Valor das parcelas incorreto!!')

Cab()
Padrao(Divida, Pagar, Parcelas, Taxa, ValorPorParcela )


#\\\\\\\\\\\\\\