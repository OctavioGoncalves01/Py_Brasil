#funcao Python
import time

Num=int(input('Digite um numero: '))

for X in range(1, Num+1):
    for C in range(1, X+1):
        time.sleep(0.2)
        print(C)
    print('~~~~~~~~~~~~')


#\\\\\\\\\\\\\