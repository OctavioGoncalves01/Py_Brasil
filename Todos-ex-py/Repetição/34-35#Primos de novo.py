Num = int(input('Digite um numero: '))
Conta = 0

for P in range(1, Num+1):
    if Num % P == 0:
        Conta += 1


if Conta == 2:
    print(f'{Num} é primo!!')
else: 
    print(f'{Num} não é primo!!')


#\\\\\\\\\\\\\\
#35 não fiz de novo