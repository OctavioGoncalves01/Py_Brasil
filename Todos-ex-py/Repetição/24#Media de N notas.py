Notas = []

while True:
    Notas.append(float(input('Nota: ')))
    Pergunta = str(input('Deseja continuar [S/N]: ')).upper()
    if Pergunta == 'N':
        break

Media = sum(Notas)/len(Notas)

print(f'A media da sala é: {Media:2.1f}')


#\\\\\\\\\\\\\\