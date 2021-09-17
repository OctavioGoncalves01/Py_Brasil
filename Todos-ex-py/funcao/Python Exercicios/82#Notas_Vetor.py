#Notas:

def Cab():
    print('-------------------------')

#Variaveis:
Notas=[]
Posi=0
MaiorMe=[]
IM=0

#Inicio do laco for para adicionar as idades:
print('Bem vindo')
for I in range(0,10):
    Notas.append(int(input(f'Digite a {I}° nota: ')))
media=sum(Notas)/len(Notas)

for N in Notas:
    if N >=media:
        MaiorMe.append(Posi)
    Posi+=1

for V in Notas:
    if V>IM:
        IM=V

Cab()        
print('A maior nota: ', IM)
print('A media da turma é: ', media)
print(f'A posicao das maiores notas: {MaiorMe}')
print(f'{Notas.index(IM)} esta é a posicao da maior nota!!')
print('Fim do programa!!')


#\\\\\\\\\\\\\\