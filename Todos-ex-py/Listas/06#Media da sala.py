import time

NotasSala = []
Soma = 0
ContaMedia7 = 0

def Cab():
    print('[--=--=--=--=--=--=--=--=--=--=--=--]')
    time.sleep(0.25)

while True:
    Cab()
    for N in range(1,5):
        Nota = float(input(f'Digite a {N}° Nota: '))
        Soma+=Nota
    
    Media = Soma/4
    NotasSala.append(Media)
    
    Media = 0
    Soma = 0
    
    Pergunta = input('Deseja continuar: ').upper()
    if Pergunta == 'N':
        break

for N in NotasSala:
    if N >= 7:
        ContaMedia7 += 1

Cab()
print('Resultados: ')
print(f'A media da sala foi: {sum(NotasSala)/len(NotasSala):2.2f}')
print('Alunos com mais de 7:', ContaMedia7, 'alunos')


#\\\\\\\\\\\\\\