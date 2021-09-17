Tabuada = int(input('Digite um numero: '))
Comeco = int(input('Digite por qual numero comecara: '))
Final = int(input('Final: '))

while Comeco > Final:
    Comeco = int(input('Digite por qual numero comecara: '))
    Final = int(input('Final: '))

print('')
print(f'Vou montar a tabuada de {Tabuada}: \nComeçando em {Comeco} e terminando em {Final}:')
print('')
for N in range(Comeco, Final+1):
    print(f'{Tabuada} x {N} = {Tabuada*N}')


#\\\\\\\\\\\\\\