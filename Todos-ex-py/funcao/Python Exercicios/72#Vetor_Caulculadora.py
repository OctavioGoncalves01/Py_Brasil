Vet=[]

Num=int(input('Digite um numero: '))

for X in range(1,11):
    Vet.append(Num*X)
for C in Vet:
    print(f'[{C:3.0f}]')