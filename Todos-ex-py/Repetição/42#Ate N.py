ListaNum = []
Cont25 = 0
Cont50 = 0
Cont75 = 0
Cont100 = 0

while True:
    Num = int(input('Digite um número positivo: '))
    if Num < 0:
        break
    else:
        ListaNum.append(Num)

for N in ListaNum:
    if N <= 25:
        Cont25 += 1 
    elif (N > 25) and (N <= 50):
        Cont50 += 1
    elif (N > 50) and (N <= 75):
        Cont75 += 1
    elif (N > 75) and (N <= 100):
        Cont100 += 1
    else:
        break

print(f'Numeros ate 25 {Cont25}.')
print(f'Numeros ate 50 {Cont50}.')
print(f'Numeros ate 75 {Cont75}.')
print(f'Numeros ate 100 {Cont100}.')


#\\\\\\\\\\\\\\