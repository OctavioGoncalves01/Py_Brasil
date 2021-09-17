Soma = 0
Maior = 0
Menor = 999999999999999999999999999999999

for X in range(1,6):
    Num = int(input('Digite um núemro: '))
    Soma+=Num

    if Num > Maior:
        Maior = Num
    if Num < Menor:
        Menor = Num

print('')
print('A soma dos números é:', Soma)
print(f'O maior número digitado foi: {Maior}, e o menor foi: {Menor}.')


#\\\\\\\\\\\\\\
    