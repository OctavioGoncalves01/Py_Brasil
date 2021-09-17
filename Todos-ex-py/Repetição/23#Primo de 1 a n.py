Cont=0
ListaNum=[]
N = int(input('digite '))

while True:
    for Numero in range(1, N+1):
        for P in range(1,Numero+1):
            if Numero % P == 0:
                Cont+=1
                ListaNum.append(P)
        if Cont == 2 :
            print(Numero, 'é primo!!')
        else:
            print(Numero, 'nao é primo!!')
            print('Numeros divisiveis: ', ListaNum)
    if Numero == N:
        break


# FAll
#\\\\\\\\\\\\\\
