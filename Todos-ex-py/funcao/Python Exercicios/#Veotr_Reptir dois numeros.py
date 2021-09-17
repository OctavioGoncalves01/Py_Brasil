#Reptir 2 num:

Num1=int(input('digite um numero: '))
Num2=int(input('digite outro numero: '))
vetor=[]

for x in range(1,11):
    if (x % 2 == 0):
        vetor.append(Num1)
    else:
        vetor.append(Num2)

print(vetor)

