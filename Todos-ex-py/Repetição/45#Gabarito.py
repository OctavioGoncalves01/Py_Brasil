Gabarito = []
Gabarito_Aluno = []
NotasMedia = []
Pergunta = 'S'
Nota = 0

print('Gabarito')
for C in range(1, 11):
    Gabarito.append(input(f'digite a {C} resposta da prova: '))


while Pergunta == 'S':
    
    for C in range(1,11):
        Resposta = input(f'Pergunta {C}: --> Resposta: ').upper().strip()
        Gabarito_Aluno.append(Resposta)
    if Gabarito_Aluno[0] == Gabarito[0]:
        Nota += 1 
    if Gabarito_Aluno[1] == Gabarito[1]:
        Nota += 1
    if Gabarito_Aluno[2] == Gabarito[2]:
        Nota += 1 
    if Gabarito_Aluno[3] == Gabarito[3]:
        Nota += 1
    if Gabarito_Aluno[4] == Gabarito[4]:
        Nota += 1 
    if Gabarito_Aluno[5] == Gabarito[5]:
        Nota += 1
    if Gabarito_Aluno[6] == Gabarito[6]:
        Nota += 1 
    if Gabarito_Aluno[7] == Gabarito[7]:
        Nota += 1
    if Gabarito_Aluno[8] == Gabarito[8]:
        Nota += 1 
    if Gabarito_Aluno[9] == Gabarito[9]:
        Nota += 1
    print('Sua nota é : ', Nota)
    NotasMedia.append(Nota)
    
    Pergunta = input('Deseja continuar [S/N]: ').upper()
     

MediaSala = sum(NotasMedia)/len(NotasMedia)
TotalAlunos = len(NotasMedia)
MaiorNota = max(NotasMedia)
MenorNota = min(NotasMedia)

print(f'A Media da sala foi de {MediaSala:2.2f}')
print(f'A Maior nota da sala foi {MaiorNota}')
print(f'A Menor nota da sala foi de {MenorNota}')
print(f'O total de alunos é de {TotalAlunos}')


#Meu melhor atualmente
#31/07/2021