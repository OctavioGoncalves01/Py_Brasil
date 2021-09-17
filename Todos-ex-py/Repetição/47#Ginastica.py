#importacoes usadas
import time
#Variaveis usadas
TodosSaltos = []
Pergunta = ''
Contador = 1

#Funcao para o cabeçalho
def Cab():
    print('--=--=--=--=--=--=--=--=--=--=--=--')
    time.sleep(0.25)

#Funcao para fazer a media
def Media(No):
    TiraMaior = No.remove(max(No))
    TiraMenor = No.remove(min(No))
    Media = sum(No)/len(No)
    return Media

TodasNotas = []
Nome = ''

while True:
    Nome = str(input('Digite o nome do(a) Ginasta: ')).upper()
    for N in range(1,8):
        Nota = float(input(f'Digite a {N}° nota: '))
        if Nota <= 0:
            Nota = float(input(f'Digite a {N}° nota :'))
    
        TodasNotas.append(Nota)

    Cab()
    print('\n')
    print('Resultados:')
    print(f'Nome:                        {Nome}')
    print('')
    print(f'Melhor nota:                 (-){max(TodasNotas)}')
    print(f'Pior nota:                   (-){min(TodasNotas)}')
    print('')
    print('Todas as notas:')
    for T in TodasNotas:
        print(f'{Contador}° nota:                       {T}')
        Contador += 1
    print('')
    Cab()
    print('Resultados Finais:')
    print(f'Media das notas:                   {Media(TodasNotas):2.2f}')

    Cab()
    Pergunta = str(input('Deseja continuar [S/N] ')).upper()
    if Pergunta == 'N':
        break


#\\\\\\\\\\\\\\