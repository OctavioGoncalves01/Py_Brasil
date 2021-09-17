Salario = 1000
Aumento = 0.15
AnoProximo = 2021

Salario = Salario+(Salario*1.5)

for c in range(1997, AnoProximo):
    print(f'{Salario:2.2f}')
    Salario = (Salario + (Salario*Aumento))
    Aumento = Aumento*2

    if c == 2005:
        break
#Meu codigo    


salario = 1000
ano = 1996
while ano <= 2020:
    salario *= 1.015
    ano += 1
print("{0:.2f}".format(salario, 2))
#https://pt.stackoverflow.com/questions/432854/c%C3%A1lculo-de-sal%C3%A1rio-precisa-limitar-casas
#Copie

