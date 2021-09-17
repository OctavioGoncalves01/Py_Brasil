import random
import time

def Cab():
    print('-=-=-=-=-=-=-=-=--=-=-=-=-=-=-')
    time.sleep(0.25)    

Casa = 1000
Lista1 = [1, 2, 3]
Lista2 = [1, 2, 3]
Lista3 = [1, 2, 3]
Resultado = []


while True:
    if Casa <= 100:
        break
    
    Cab()
    Aposta = int(input('Digite o valor da aposta: '))
        
    Resultado.append(random.choice(Lista1))
    Resultado.append(random.choice(Lista2))
    Resultado.append(random.choice(Lista3))

    Cab()    
    print(Resultado)
    if Resultado[0] == Resultado[1] == Resultado[2]:
        Ganho = Aposta*10
        print('Parabens Voce ganhou !!')
        print('Premio == R$:', Ganho)
        Casa -= Ganho
        Resultado.clear()
    elif (Resultado[0] == Resultado[1]) or (Resultado[0] == Resultado[2]) or (Resultado[1] == Resultado[2]):
        Ganho = Aposta*0.5
        print('Perdeu')
        print('Consolacao', Ganho)
        Casa -= Ganho
        Resultado.clear()
    elif Resultado[0] != Resultado[1] != Resultado[2]:
        print('Perdeu!!\nSem premio')
        Casa += Aposta
        Resultado.clear() 
    
    if Casa <= 100:
        break
    Cab()
    Perg = input('Deseja continuar: ').upper()
    if Perg == 'N':
        break
    
print(Casa)