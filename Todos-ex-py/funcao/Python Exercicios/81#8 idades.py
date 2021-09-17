#Idade separando individuos:

def Cab():
    print('-------------------------')

#Variaveis:
Idades=[]
Posi=0
Id25=[]
IM=0

#Inicio do laco for para adicionar as idades:
print('Bem vindo')
for I in range(0,8):
    Idades.append(int(input(f'Digite uma idade para a posicão {I}°: ')))

for V in Idades:
    if V >=25:
        Id25.append(Posi)
    Posi+=1

for V in Idades:
    if V>IM:
        IM=V

Cab()        
print('A maior idade digitada foi: ', IM)
print('A media das idades é: ', sum(Idades)/len(Idades))
print(f'A posicao da idade de pessoas com mais de 25 anos é: {Id25}')
print(f'{Idades.index(IM)} esta é a posicao da maior idade digitada!!')
print('Fim do programa!!')


#\\\\\\\\\\\\\\