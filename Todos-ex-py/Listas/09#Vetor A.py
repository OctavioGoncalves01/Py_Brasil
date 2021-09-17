import random
Soma = 0

A = []
for C in range(1,11):
    A.append(int(random.randrange(1, 11)))

for S in A:
    print(S, Soma)
    Soma += S**2 

print(A, Soma)