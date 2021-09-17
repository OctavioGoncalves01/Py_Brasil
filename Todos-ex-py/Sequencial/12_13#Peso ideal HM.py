def PesoIdealF(A):
    Peso= (62.1*A) - 44.7
    return Peso

def PesoIdealM(A):
    Peso=(72.7*A) - 58
    return Peso


Nome=input('Digite seu nome: ')
Sexo=input('Sexo: F/M:\n')
if Sexo=='F':
    Altura=float(input('Digite sua altura:\n[EM METROS] '))
    print(f'O peso ideal é {PesoIdealF(Altura):2.2f}')
elif Sexo=='M':
    Altura=float(input('Digite sua altura:\n[EM METROS] '))
    print(f'O peso ideal é {PesoIdealM(Altura):2.2f}')
else:
    print('Digite a opção correta!!')



#\\\\\\\\\\\\\\