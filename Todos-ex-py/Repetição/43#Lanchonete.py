import time

Soma = 0

def Cab():
    print('------------------')
    time.sleep(0.25)

print('--- Bem vindo ---')
Cab()
print('\nCardapio:\n')
print('Especificação   Código  Preço')
print('Cachorro Quente 100     R$ 1,20')
print('Bauru Simples   101     R$ 1,30')
print('Bauru com ovo   102     R$ 1,50')
print('Hambúrguer      103     R$ 1,20')
print('Cheeseburguer   104     R$ 1,30')
print('Refrigerante    105     R$ 1,00')
print('')

while True:
    Cab()
    Pedido=(str(input('Digite o código do pedido: ')))
    Quantidade=(int(input('Digite a quantidade do pedido: ')))
    
    if Pedido == '100':    
       Soma += (Quantidade*1.2)
    elif Pedido == '101':
        Soma += (Quantidade*1.3)
    elif Pedido == '102':
        Soma += (Quantidade*1.5)
    elif Pedido == '103':
        Soma += (Quantidade*1.2)
    elif Pedido == '104':
        Soma += (Quantidade*1.3)
    elif Pedido == '105':
        Soma += (Quantidade*1.0)

    Cab()
    Continuar = str(input('Deseja continuar  [S/N]: ')).upper()
    if Continuar == 'N':
        break

Cab()
print(f'O valor da compra é :           R${Soma:2.2f}')


#\\\\\\\\\\\\\\