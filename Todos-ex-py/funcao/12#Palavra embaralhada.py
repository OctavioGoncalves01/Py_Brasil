import random

def FuncaoEmbaralhar(X):
    Embaralha = random.sample(X, len(X))
    PalavraEmbaralhada = ''.join(Embaralha)
    print(PalavraEmbaralhada)

Palavra = input('Diigite uma palavra: ').upper()

FuncaoEmbaralhar(Palavra)

#https://wiki.python.org.br/ExerciciosFuncoesSolucoes