#Vetor Par

Vet=[]
Par=0

for X in range(1,8):
    Vet.append(int(input('Digite um numero: ')))
for X in range(1,7):
    if X%2 == 0:
        Par+=1
    print(Vet[X])
print(Par)