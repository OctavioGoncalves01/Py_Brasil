from fractions import Fraction

H = 0 
Cima = 1
Baixo = 1
N = int(input('Digite o  final da fracao: '))

for F in range(1, N+1):
    Fracao = (Fraction(Cima, Baixo))
    print(Fracao)
    H += Fracao
    Baixo += 1

print(H)


#\\\\\\\\\\\\\\