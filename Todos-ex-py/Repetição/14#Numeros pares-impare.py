Par = 0
Impar = 0

for P in range(1,11):
    Num = int(input(f'Digite o {P}° número:  '))
    if Num % 2 == 0:
        Par+=1
    elif Num % 2 != 0:
        Impar+=1

print('')
print('Foram digitados ', Par,' numeros par. E ', Impar, 'numeros impar.')


#\\\\\\\\\\\\\\