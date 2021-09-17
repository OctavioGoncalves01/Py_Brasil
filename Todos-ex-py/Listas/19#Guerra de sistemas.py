import time

Votos = [0] * 6

def Cab():
    print('--------------------------------------')
    time.sleep(0.35)

print('Inicio da votacao:')

while True:
    Cab()
    Voto = int(input('Voto:\n1- Windows Server; 2- Unix; 3- Linux; 4- Netware; 5- Mac OS; 6- Outro\n'))
    
    while (Voto > 6) or (Voto < 0) :
        print('Opcao invalida!!')
        Voto = int(input('Voto:\n1- Windows Server; 2- Unix; 3- Linux; 4- Netware; 5- Mac OS; 6- Outro\n'))

    Votos[Voto -1] = Votos[Voto - 1] + 1
    
    if Voto == 0:
        break

print('Resultado da votacao: ')
print('Windows Server   : ', Votos[0])
print('Unix             : ', Votos[1])
print('Linux            : ', Votos[2])
print('Netwera          : ', Votos[3])
print('Mac OS           : ', Votos[4])
print('Outros           : ', Votos[5])

print('')
print('Total de Votos   :', sum(Votos))

Cab()
print('Vencedor da votacao:')
print(max(Votos))


#sistemas[opcao - 1] = sistemas[opcao - 1] + 1 = https://github.com/karenyov/exerciciosPythonBrasil/blob/master/4_ExerciciosListas/19.py