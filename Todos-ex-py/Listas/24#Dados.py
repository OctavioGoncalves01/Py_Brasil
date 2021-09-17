import random

Quantidade = [0, 0, 0, 0, 0, 0]
Valores = []
Contador = 0

while  Contador != 100:
    DADO = random.randint(1,6)
    Valores.append(DADO) 
    Contador += 1
    
for C in Valores:
    if C == 1:
        Quantidade[0] = Quantidade[0] +1
    if C == 2:
        Quantidade[1] = Quantidade[1] +1
    if C == 3:
        Quantidade[2] = Quantidade[2] +1
    if C == 4:
        Quantidade[3] = Quantidade[3] +1
    if C == 5:
        Quantidade[4] = Quantidade[4] +1
    if C == 6:
        Quantidade[5] = Quantidade[5] +1
    
print('Valores Jogados:')
print(Valores)
print('-----------------')
print('Quantidade em cada posicao:')
for C in range(1, 7):
    print(f'N°{C} == {Quantidade[C-1]} Vezes')