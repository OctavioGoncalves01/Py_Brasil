Tudo = 0
Lula = 0
Marina = 0
Ciro = 0
Danilo = 0
Nulos = 0
Brancos = 0

while True:
    print('Lula = 13\nMarina = 43\nCiro = 12\nDanilo = 69\nVotar Branco = 0\nVotar Nulo = 1\n')
    Voto = int(input('Digite o numero de seu candidato: '))
    if Voto == 0:
        Brancos += 1
    elif Voto == 1:
        Nulos +=1
    elif Voto == 13:
        Lula +=1
    elif Voto == 12:
        Ciro +=1
    elif Voto == 43:
        Marina +=1
    elif Voto == 69:
        Danilo +=1
    else:
        print('Candidato invalido!!')
    
    print('Obrigado por votar!!')
    Continuar = str(input('Encerrar [S/N]: \n')).upper()
    if Continuar == 'S':
        break

Tudo = Lula + Marina + Ciro + Danilo + Nulos + Brancos

print('Total de votos:         ', Tudo)
print('Lula:                   ', Lula)
print('Marina:                 ', Marina)
print('Ciro:                   ', Ciro)
print('Danilo:                 ', Danilo)
print('Brancos e nulos:         ', Brancos, Nulos)
print(f'Porcentagem de votos nulos: {Nulos / Tudo * 100}%')
print(f'Porcentagem de votos brancos: {Brancos / Tudo * 100}%')

Tudo = 0
Lula = 0
Marina = 0
Ciro = 0
Danilo = 0
Nulos = 0
Brancos = 0


#\\\\\\\\\\\\\\