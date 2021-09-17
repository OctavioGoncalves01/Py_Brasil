def Quadrado(B,A):
    Area=B*A
    Area*=2
    return Area

Base=float(input('Digite a base do quadrado: '))
Altura=float(input('Digite a altura: '))

print(f'A area do quadrado multiplicado por 2 é: {Quadrado(Base, Altura):3.2f}')


#\\\\\\\\\\\\\\