#programa le os saltos e tira a media, porem antes remove o melhor e o pior 

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
def Media(S):
    TiraMaior = S.remove(max(S))
    TiraMenor = S.remove(min(S))
    Media = sum(S)/len(S)
    return Media

#Inicio do programa: 
print('Bem vindo: ')
while True:
    Cab()
    Nome = input('Digite o nome do atleta: ')
    for C in range(1,6):
        Salto = float(input(f'Digite o {C}° do atleta: '))
        TodosSaltos.append(Salto)
    
    #Exibir os resultados 
    Cab()
    print('RESULTADOS DO ATLETA:')
    print('')
    print(f'Nome do participante:                 {Nome}')
    for S in TodosSaltos:
        print(f'{Contador}° salto:                             {S} metros')
        Contador += 1
    print('')
    print(f'Melhor Salto:                         {max(TodosSaltos)}')
    print(f'Pior Salto:                           {min(TodosSaltos)}')
    print('')
    print(f'Media dos saltos:                     {Media(TodosSaltos):2.2f}')

    #Pergunta se deseja continuar: 
    Cab()
    Pergunta = input('Continuar [S/N]:').upper()
    TodosSaltos.clear()
    Contador = 1
    Nome = ''
    if Pergunta == 'N':    
        break


#\\\\\\\\\\\\\\