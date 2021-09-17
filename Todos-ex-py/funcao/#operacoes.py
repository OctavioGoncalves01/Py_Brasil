#operacoes

def Soma(x,y):
    z=x+y
    print(z)

def Subt(x,y):
    z=x-y
    print(z)

def Divis(x,y):
    z=x/y
    print(z)

def Mult(x,y):
    z=x*y
    print(z)


Num1=int(input('Digite um numero: '))
Num2=int(input('Digite outro numero: '))
Escolha=str(input('Escolha:\nAdicao: +\nSubtracao: -\ndivisao: /\nMultiplicacao: *\n'))

if Escolha == '+':
    Soma(Num1,Num2)
elif Escolha == '-':
    Subt(Num1,Num2)
elif Escolha == '/':
    Divis(Num1,Num2)
elif Escolha == '*':
    Mult(Num1,Num2)
else:
    print('Escolha a operacao apropriada')


#\\\\\\\\\\\\\\