NumeroTurmas = int(input('Digita a quantidade de turmas: '))
TotalAlunos = 0

for C in range(1,NumeroTurmas+1):
    NumeroAlunos=int(input(f'Digite a quantidade de alunos da turma {C}: '))
    
    if NumeroAlunos > 40:
        NumeroAlunos=int(input(f'Digite a quantidade de alunos da turma {C}: '))
    
    TotalAlunos+=NumeroAlunos

Media = TotalAlunos/NumeroTurmas
print('O número médio de alunos por turma é : ',Media)


#\\\\\\\\\\\\\\