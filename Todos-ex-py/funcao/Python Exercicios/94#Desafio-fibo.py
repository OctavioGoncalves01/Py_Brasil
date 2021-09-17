def Fibo(X):
    PT=1
    ST=1
    TT=PT+ST

    for C in range(1,X+1):
        print(f'--{PT}--', end='')
        PT=ST
        ST=TT
        TT=ST+PT
    print(f'--Fim!!--', end='')

Num=int(input('Digite a quantidade de termos da sequencia de fibinacci para mostrar:'))   
Fibo(Num)

