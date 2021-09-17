import time

Numeros = []
AcimaMedia = 0
Menor7 = 0

def Cab():
    print('[---=---=---=---=---=---=---=---]')
    time.sleep(0.3)

while True:
    Cab()
    N = float(input('Digite uma nota: '))
    if N < 0:
        break
    else:
        Numeros.append(N)

Media = sum(Numeros) / len(Numeros)
Inverso = [Num for Num in reversed(Numeros)]

for N in Numeros:
    if N > Media:
        AcimaMedia += 1
    if N < 7:
        Menor7 += 1

Cab()
print('Resultados:')
print('')
print(f'A quantidade de notas foi {len(Numeros)}.')
print(f'Os números informados foram:\n', Numeros)

print(f'Os números digitados invertidos são:\n')
for L in Inverso:
    print(L)

print('')
print(f'A média dos números digitado: {Media:2.2f}')
print(f'A quantia de números maior que a média é: {AcimaMedia}')
print(f'A quantia de números menor que sete é: {Menor7}')
print('')
Cab()
print('programa encerrado!!')


#\\\\\\\\\\\\\\