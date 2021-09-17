Esfera = 0
Limpeza = 0
Cabo = 0
Inutilizado = 0
EstadoRato = []

while True:
    Rato = int(input('Qual o estado do mouse:\n1-Necessita da esfera; 2-Necessita de limpeza; 3-Necessita troca do cabo ou conector; 4-Quebrado ou inutilizado:\n'))
    if Rato == 0:
        break
    while Rato > 4:
        print('Valor Invalido!!')
        Rato = int(input('Qual o estado do mouse:\n1-Necessita da esfera; 2-Necessita de limpeza; 3-Necessita troca do cabo ou conector; 4-Quebrado ou inutilizado:\n'))
    EstadoRato.append(Rato)


for C in EstadoRato:
    if C == 1:
        Esfera += 1
    if C == 2:
        Limpeza += 1
    if C == 3:
        Cabo += 1
    if C == 4:
        Inutilizado += 1

EstadoTotal = [Esfera, Limpeza, Cabo, Inutilizado]

print(EstadoRato)

print('Resulado:')
print(f'Quantidade de mouses:              {len(EstadoRato)} Uni.')
print(f'Situacao:                          Estado')

print(f'Esfera:                            {EstadoTotal[0]} == {Esfera/len(EstadoRato) * 100:.2f}%')
print(f'Limpeza:                           {EstadoTotal[1]} == {Limpeza/len(EstadoRato) * 100:.2f}%')
print(f'Cabo:                              {EstadoTotal[2]} == {Cabo/len(EstadoRato) * 100:.2f}%')
print(f'Inutilidavel:                      {EstadoTotal[3]} == {Inutilizado/len(EstadoRato) * 100:.2f}%')


#\\\\\\\\\\\\\\