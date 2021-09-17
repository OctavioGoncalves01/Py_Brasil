def Espaco(F):
    ES = F.count(' ')
    return ES

def Vogais(F):
    A = F.count('A')
    E = F.count('E')
    I = F.count('I')
    O = F.count('O')
    U = F.count('U')

    ListaVogais = [A, E, I, O, U]    
    return ListaVogais

Frase = str(input('Informe uma frase: ')).upper()
L = Vogais(Frase)

print(f'Existe {Espaco(Frase)} espaco(s) na frase.')
print(f'Na frase existem: A = {L[0]}, E = {L[1]}, I = {L[2]}, O = {L[3]}, U = {L[4]}')


#\\\\\\\\\\\\\\