import time

def Cab():
    print('----------------------')
    time.sleep(0.3)

def Com(H, M):
    if (H > 12) and (H != 24):
        cont=1
        for X in range(H):
            if X > 12:
                cont+=1
        print(f"As horas convertida é {cont}:{M}pm")
    elif H == 24:
        print(f"As horas convertida é 0:{M}am")
    else:
        print(f"As horas convertida é {H}:{M}am")

Pergunta='s'

while Pergunta == 's':
    Cab()
    Hour=int(input('Digite as Horas: '))
    Min=str(input('Digite os minutos: '))
    Cab()
    Com(Hour, Min)
    Cab()
    Pergunta=input('Deseja continuar? s/n\n')
Cab()
print('Obrigdo por usar!!')


#\\\\\\\\\\\\\\