Notas=[]

def Media(X):
    M=sum(X)/len(X)
    return M

for N in range(1,5):
    Notas.append(float(input(f'Digite a {N}° do aluno: ')))

print(f'A media foi {Media(Notas):2.2f}')


#\\\\\\\\\\\\\\