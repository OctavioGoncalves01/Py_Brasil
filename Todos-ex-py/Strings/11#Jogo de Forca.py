import random

DicPalavras = {1:'gato', 2:'cama', 3:'carro', 4:'banana', 5:'camisa'}
DicDica = {1:'Animal', 2:'Móvel', 3:'Transporte', 4:'Fruta', 5:'Roupa'}

Erro = 0
Sorteio = random.randint(1,5) 
Palavra = []
for p in DicPalavras[Sorteio]:
    Palavra.append(p) 
PalavraCorreta = [0, len(Palavra)]

print(DicPalavras[Sorteio], DicDica[Sorteio], Palavra)

while True:
    
    while True:
        print(Erro)
        Letra = str(input('\nDigite um letra: '))
        for L in Palavra:
            if L == Letra:
                print(PalavraCorreta)
                print(L, end='')
                PalavraCorreta.insert(Palavra.index[L], L)
            else:
                print('_', end='')
                print(PalavraCorreta)
        if Letra in Palavra == False:
            Erro += 1

        if Erro >= 6:
            break
#Meu Maximo Agora 11/8/21