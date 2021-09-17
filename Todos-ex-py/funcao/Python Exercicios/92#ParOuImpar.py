def ParOuImpar(X):
    if X %2 == 0:
        print(f'{X} é PAR')
    elif X %2 != 0:
        print(f'{X} é IMPAR')

Num=int(input('Digite um numero: '))

ParOuImpar(Num)