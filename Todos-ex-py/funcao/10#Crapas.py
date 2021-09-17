import random
Soma = 0


def Crapa(S): 
    if (S == 11) or (S == 7):
        print('Voce Ganhou\nNatural ==', S)

    elif (S == 2) or (S == 3) or (S == 12):
        print('Voce Perdeu\nCrapa ==', S)    

    else:
        print('Ganhou um ponto\nPonto ==', S)


while True:
    jogar = str(input('Jogar [S/N]')).upper()
    while jogar == 'N':
        break

    Dado1 = random.randint(1,6)
    Dado2 = random.randint(1,6)
    Soma = Dado2+ Dado1

    Crapa(Soma)
    Soma = 0