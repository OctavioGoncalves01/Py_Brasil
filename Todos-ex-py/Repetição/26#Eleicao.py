import time

def Cab():
    print('--------------------------')
    time.sleep(0.3)

Partido1 = 0
Partido2 = 0
Partido3 = 0


while True:
    Cab()
    Votos = int(input('Voto:\nPartido 1 = 1; Partido 2 = 2; Partido 3 = 3:\n'))

    if Votos != 1 and Votos != 2 and Votos !=3:
        Votos = int(input('Voto:\nPartido 1 = 1; Partido 2 = 2; Partido 3 = 3:\n'))

    if Votos == 1:
        Partido1 =+ 1
    elif Votos == 2:
        Partido2 += 1
    elif Votos == 3:
        Partido3 += 1
    Cab()
    print('Obrigado por votar!!')
    Pergunta = input('Deseja continuar: [S/N]:\n').upper()
    if Pergunta == 'N':
        break

Cab()
print('Resultados:')
print('')
print(f'Votos para o Partido1: {Partido1}')
print('')
print(f'Votos para o Partido2: {Partido2}')
print('')
print(f'Votos para o Partido3: {Partido3}')
Cab()
print('')
if Partido1 > Partido2 and Partido1 > Partido3:
    print('Partido 1 Ganhou!!\nVotos: ', Partido1)
elif Partido2 > Partido1 and Partido2 > Partido3:
    print('Partido 2 Ganhou!!\nVotos: ', Partido2)
elif Partido3 > Partido1 and Partido3 > Partido2:
    print('Partido 3 Ganhou!!\nVotos: ', Partido3)
else:
    print('Empatou!!')


#\\\\\\\\\\\\\\