Saltos = []

def MediaSaltos(S):
    S.remove(max(S))
    S.remove(min(S))
    
    Media = sum(S) / len(S)
    return Media

while True:
    Nome = str(input('Digite o nome do atleta: ').upper())
    for Sal in range(1, 6):
        s = float(input(f'Digite a distancia do {Sal}°: '))
        Saltos.append(s)

    print('Resultados: ')
    print('Nome:', Nome)
    for C in Saltos:
        print('Saltos: ', C)
    print(f'Media: {MediaSaltos(Saltos)}')
     
    Pergunta = str(input('Deseja Sair [S/N]: ')).upper()
    if Pergunta == 'N':
        break

#\\\\\\\\\\\\\\