Idades = []

while True:
    Idades.append(int(input('Digite sua idade: ')))
    Pergunta = str(input('Deseja continuar [S/N}: ')).upper()
    if Pergunta == 'N':
        break

Media = sum(Idades)/len(Idades)


if Media > 0 and Media <=25:
    print(f'Esta Turma é jovem, com a media de {Media}anos.')

elif Media > 25 and Media <=60:
    print(f'Esta Turma é adulto, com a media de {Media}anos.')

elif Media > 60:
    print(f'Esta Turma é idosa, com a media de {Media}anos.')


#//////////////