#Saber quais alunos da academia tem maior e menor peso e altura: 

import time

def Cab():
    print('------------------')
    time.sleep(0.35)
    print('')

ListaCod = []
ListaPeso = []
ListaAltura = []

def MaisAlto(X):
    H = 0
    for A in X:
        if A > H:
            H = A
    
    B = ListaAltura.index(H)
    return B

def MaisBaixo(X):
    H = 999999999
    for A in X:
        if A < H:
            H = A
    
    B = ListaAltura.index(H)
    return B

def MaisGordo(X):
    Kg = 0
    for A in X:
        if A > Kg:
            Kg = A
    
    P = ListaPeso.index(Kg)
    return P

def MaisMagro(X):
    Kg = 999999999
    for A in X:
        if A < Kg:
            Kg = A
    
    P = ListaPeso.index(Kg)
    return P

#Inicio do codgo:
Cab()
print('Academia Pesquisa:')

while True:
    Cab()
    Codigo = str(input('Digite seu código: ')).upper()

    if Codigo == '0000':
        break
    else:
        Peso = float(input('Digite seu peso: '))
        Altura = float(input('Digite sua altura: '))

        ListaCod.append(Codigo)
        ListaPeso.append(Peso)
        ListaAltura.append(Altura)

Cab()
print('Resulatdos da pesquisa: ')

Alto = MaisAlto(ListaAltura)
print('Maior Altura: ', ListaAltura[Alto], 'Cod:', ListaCod[Alto])

Baixo = MaisBaixo(ListaAltura)
print ('Menor Altura', ListaAltura[Baixo], 'Cod:', ListaCod[Baixo])

Gordo = MaisGordo(ListaPeso)
print('Maior Peso: ', ListaPeso[Gordo],'Cod:', ListaCod[Gordo])

Magro = MaisMagro(ListaPeso)
print('Menor peso: ', ListaPeso[Magro],'Cod:', ListaCod[Magro])


#\\\\\\\\\\\\\\