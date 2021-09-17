Votos = []
TotalVotos = []

while True:
    V = int(input('Para quem vai seu Voto: '))
    if (V <= 0):
        break
    while V > 23:
        print('Número inválido')
        V = int(input('*Para quem vai seu Voto: *'))
    else:
        Votos.append(V)

for Vo in range(0,24):
    S = Votos.count(Vo)
    TotalVotos.append(S)
    
print(f'O total de votos: {len(Votos)}')
for R in range(1, 24):
    if TotalVotos[R] != 0:
        print('')
        print(f'O jogador {R} teve {TotalVotos[R]} de votos')
        print(f'O percentual de votos deste jogador: {TotalVotos[R]}')
print(f'Jogador da galera: N°{TotalVotos.index(max(TotalVotos))}')
print('Porcentagem dos votos:', max(TotalVotos) / len(Votos) * 100, '%.')        


#\\\\\\\\\\\\\\