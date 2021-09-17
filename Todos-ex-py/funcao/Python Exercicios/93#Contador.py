def Contador(I, F, P):
    for X in range(I, F+1, P):
        print(f'>{X}>', end='')
    print('FIM!!')

Inicio=int(input('Digite o valor para o inicio da contagem: '))
Fim=int(input('Digite o valor para o fim da contagem: '))
Passo=int(input('Digite o valor para o salto da contagem: '))

Contador(Inicio, Fim, Passo)
