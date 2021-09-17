Lista_Alunos = []
Altura_Alunos = []

def Maior (X):
    H = max(X)
    Cod = X.index(H)
    return Cod

def Menor (X):
    H = min(X)
    Cod = X.index(H)
    return Cod

for Z in range(1, 11):
    Lista_Alunos.append(int(input('Digite o numero da chamada do aluno: ')))
    Altura_Alunos.append(float(input('Digite a altura dele(a) [Em Cm]:  ')))

Alto = Maior(Altura_Alunos)
Baixo = Menor(Altura_Alunos)

print('Cod do aluno mais alto:' ,Lista_Alunos[Alto],'Altura: ', Altura_Alunos[Alto], 'cm')
print('Cod do aluno mais baixo:' ,Lista_Alunos[Baixo],'Altura: ', Altura_Alunos[Baixo], 'cm')


#\\\\\\\\\\\\\\