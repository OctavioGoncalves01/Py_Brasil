def Media(Y, X):
    M=(X+Y)/2
    return M

def Situacao(X):
    if X>=9:
        Z='Parabens, aprovado'
    elif X>=7:
        Z='Aprovado'
    else:
        Z='Reprovado'
    return Z

N1=float(input('Digite a primeira nota: '))
N2=float(input('Digite a segunda nota: '))

print(f'A media desse aluno é: {Media(N1,N2):3.2f}.')
print(Situacao(Media(N1,N2)))
    


#\\\\\\\\\\\\\\