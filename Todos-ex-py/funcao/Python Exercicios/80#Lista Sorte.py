import random
Lista=[]
Posi=0
Vezes=0

for C in range(1,31):
    Lista.append(random.randrange(1,15))

NumUso=int(input('Digite um numero entre 1 a 15:\n'))

print('----------')
for N in Lista:
    if N == NumUso:
        print(f'A posição do numero digitado é:{Posi}')
        Vezes+=1
    Posi+=1
print(f'O numero digitado foi encontrado {Vezes} vez(es).')
print('')
print('----------')
print(Lista)


#\\\\\\\\\\\\\\