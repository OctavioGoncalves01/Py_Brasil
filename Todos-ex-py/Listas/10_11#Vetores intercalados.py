import random

A = []
B = []
C = []
D = []

for L in range(1,11):
    A.append((random.randint(0, 11)))
    B.append((random.randint(20, 31)))
    C.append((random.randint(40, 51)))

for L in range(10):
    D.append(A[L])
    D.append(B[L])
    D.append(C[L])

print(D)
print(A, B, C)


#https://intranet.ifs.ifsuldeminas.edu.br/matheus.vilasboas/2019-1oSemestre/Programacao_de_Scripts/Trabalhos/Resolu%C3%A7%C3%A3o/ex16.py
#Copiei 2/8/21