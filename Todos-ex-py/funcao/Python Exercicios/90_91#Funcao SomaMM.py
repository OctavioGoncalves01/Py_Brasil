def Soma(X,Y):
    Z=X+Y
    return Z

def Maior(X,Y):
    if X<Y:
        print(f'{X} é menor que {Y}')
    elif X>Y:
        print(f'{X} é maior que {Y}')
    else:
        print(f'Tem o mesmo valor')

N1=int(input('Digite um numero: '))
N2=int(input('Digite outro numero: '))

print(Soma(N1, N2))
Maior(N1,N2)


#\\\\\\\\\\\\\\