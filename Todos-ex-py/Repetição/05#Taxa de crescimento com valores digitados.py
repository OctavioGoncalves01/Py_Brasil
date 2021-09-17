import time

def Cab():
    print('-----------------')
    time.sleep(0.3)

Pergunta = 'S'
Cont = 0

while Pergunta == 'S':
    print('Censo:')
    Cab()
    PaisA = int(input('Digite o tamanha da população do Pais A: '))
    TaxaA = float(input('Taxa populacional: '))
    print('')
    PaisB = int(input('Digite o tamanho da população do Pais B: '))
    TaxaB = float(input('Taxa populacional: '))

    while PaisA < PaisB:
        PaisA+=(PaisA*TaxaA/100)
        PaisB+=(PaisB*TaxaB/100) 
        Cont+=1

    Cab()
    print(f'Vai demorar {Cont} ano(s) para o Pais A passar o Pais B')
    print(f'População de Pais A: {PaisA:2.2f}Hab.\nPopulação de Pais B: {PaisB:2.2f}Hab.')

    Pergunta= str(input('Deseja continuar? [S/N]\n')).upper()
    while Pergunta != 'S' and  Pergunta != 'N':
            Pergunta= str(input('Deseja continuar? [S/N]\n')).upper()
        

#\\\\\\\\\\\\\\