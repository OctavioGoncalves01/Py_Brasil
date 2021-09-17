Lista=[]

A = int(input('Digite o primeiro termo: '))
B = int(input('Digite o segundo termo: '))

for N in range(A+1, B):
    Lista.append(N)
    print(N)

print('A soma da sequencia dos numeros é:',sum(Lista))


#\\\\\\\\\\\\\\