from fractions import Fraction

Soma = 0
Num = int(input('Digite um numero para o final da sequencia: '))
Cima = 1
Baixo = 1

for F in range(1, Num+1):
    Fracao = Fraction(Cima, Baixo)
    print(Fracao)
    Soma += Fracao
    Cima += 1
    Baixo += 2

print(Soma)


#\\\\\\\\\\\\\\