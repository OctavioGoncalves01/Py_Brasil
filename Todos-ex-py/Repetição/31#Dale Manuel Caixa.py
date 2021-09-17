import time

def Cab():
    print('---------------------------')
    time.sleep(0.25)

Produto = []

while True:
    while True:
        Cab()
        print('Lojas Tabajara:')
        for P in range(0,99999999999):
            Pro = float(input('Digite o valor do produto: R$'))

            if Pro == 0:
                break
            Produto.append(Pro)

        Soma = 1    
        Pagar = sum(Produto)
        Cab()        
        print(f'O valor da compra foi de R${Pagar:2.2f}')        
        Dinheiro = float(input('Valor: R$'))

        Cab()
        print('-----[Nota Fiscal:]-----')
        for c in Produto:
            print(f'Produto {Soma}:                    R${c:2.2f}')
            Soma+=1
        print(f'Total das compras:            R${Pagar:2.2f}')
        print(f'Dinheiro:                     R${Dinheiro}')
        print(f'Troco:                        R${Dinheiro-Pagar:2.2f}')
        print(f'Obrigado pela preferencia!!')
        Cab()
        print('')
        
        Produto.clear()
        Dinheiro = 0


#\\\\\\\\\\\\\\