Numeros = []
Soma = 0
Mult = 1

for C in range(1,6):
    N = int(input('Digite um numero: '))
    Numeros.append(N)

Soma = sum(Numeros)

for L in Numeros:
    Mult *= L

print(Mult, Soma, Numeros)


#\\\\\\\\\\\\\\