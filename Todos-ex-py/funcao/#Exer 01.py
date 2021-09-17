#Exer 01
PriTer=1
SegTer=1
Novo=0

Num=int(input('Digite um numero:\n'))
print('-------------------------')

for X in range(1,Num+1):
    print(PriTer)
    Novo=PriTer+SegTer
    PriTer=SegTer
    SegTer=Novo

print('Fim do programa')
#\\\\\\\\\\\\\\